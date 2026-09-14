#!/usr/bin/env python3
"""Validate durable structure and routing invariants for the skills library.

This intentionally checks metadata and discoverability, not the prose of a
skill's technical contract.  It uses only the Python standard library so it is
safe to run in a fresh orchestration checkout.
"""

from __future__ import annotations

import datetime as dt
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
ACTIVE_PLATFORMS = {"qortal", "qortium", "shared"}
MATURITIES = {"candidate", "verified-reference", "verified-runtime", "stale", "retired"}
REQUIRED_HEADINGS = (
    "Use when",
    "Do not use when",
    "Authoritative evidence",
    "Reusable contract / procedure",
    "Freshness and compatibility gate",
    "Validation",
    "Known failure modes",
    "Non-goals",
    "Harvest / maturity update",
)
LINK_RE = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")
INDEX_LINK_RE = re.compile(r"\[[^]]+\]\(([^)]+/SKILL\.md)\)")


class Diagnostics:
    def __init__(self) -> None:
        self.errors: list[str] = []

    def error(self, path: Path, line: int, message: str) -> None:
        self.errors.append(f"{path.relative_to(ROOT)}:{line}: error: {message}")


def line_of(text: str, needle: str) -> int:
    return text[: text.find(needle)].count("\n") + 1 if needle in text else 1


def active_skill_dirs() -> list[tuple[str, Path]]:
    result: list[tuple[str, Path]] = []
    for platform in sorted(ACTIVE_PLATFORMS):
        base = SKILLS / platform
        for directory in sorted(path for path in base.rglob("*") if path.is_dir()):
            if directory.name.startswith("_"):
                continue
            result.append((platform, directory))
    return result


def parse_frontmatter(path: Path, text: str, diag: Diagnostics) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        diag.error(path, 1, "frontmatter must begin with '---'")
        return {}
    try:
        end = lines.index("---", 1)
    except ValueError:
        diag.error(path, 1, "frontmatter is missing its closing '---'")
        return {}
    fields: dict[str, str] = {}
    for number, line in enumerate(lines[1:end], 2):
        match = re.fullmatch(r"([a-z_]+):\s*(.+)", line)
        if not match:
            diag.error(path, number, "frontmatter must use simple 'key: value' fields")
            continue
        key, value = match.groups()
        if key in fields:
            diag.error(path, number, f"duplicate frontmatter field '{key}'")
        fields[key] = value.strip().strip('"')
    return fields


def check_links(path: Path, text: str, diag: Diagnostics) -> None:
    for match in LINK_RE.finditer(text):
        target = match.group(1).strip()
        if target.startswith(("#", "http://", "https://", "mailto:", "qortal:")):
            continue
        target = target.split("#", 1)[0]
        if not target:
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            diag.error(path, line_of(text, match.group(0)), f"relative Markdown link does not resolve: {target}")


def check_skill(platform: str, directory: Path, names: dict[str, Path], diag: Diagnostics) -> None:
    path = directory / "SKILL.md"
    if not path.is_file():
        diag.error(directory, 1, "active skill directory is missing SKILL.md")
        return
    text = path.read_text(encoding="utf-8")
    fields = parse_frontmatter(path, text, diag)

    name = fields.get("name")
    if not name:
        diag.error(path, 1, "missing required frontmatter field 'name'")
    elif name in names:
        diag.error(path, 1, f"duplicate skill name '{name}' (also {names[name].relative_to(ROOT)})")
    else:
        names[name] = path
    if not fields.get("description"):
        diag.error(path, 1, "missing required frontmatter field 'description'")

    metadata: dict[str, str] = {}
    for label, key in (("Platform", "platform"), ("Maturity", "maturity"),
                       ("Last checked", "last_checked"), ("Owner", "owner")):
        match = re.search(rf"^- {re.escape(label)}:\s*`?([^`\n]+)`?\s*$", text, re.MULTILINE)
        if not match:
            diag.error(path, 1, f"missing required metadata field '{key}'")
        else:
            metadata[key] = match.group(1).strip()

    declared_platform = metadata.get("platform")
    if declared_platform not in ACTIVE_PLATFORMS:
        diag.error(path, line_of(text, "- Platform:"), f"platform must be one of {sorted(ACTIVE_PLATFORMS)}")
    elif declared_platform != platform:
        diag.error(path, line_of(text, "- Platform:"), f"platform '{declared_platform}' conflicts with skills/{platform}/ path")

    maturity = metadata.get("maturity")
    if maturity not in MATURITIES:
        diag.error(path, line_of(text, "- Maturity:"), f"maturity must be one of {sorted(MATURITIES)}")

    date_value = metadata.get("last_checked")
    if date_value:
        try:
            dt.date.fromisoformat(date_value)
        except ValueError:
            diag.error(path, line_of(text, "- Last checked:"), "last_checked must be a real YYYY-MM-DD date")

    title_platform = re.search(r"^#\s+(Qortal|Qortium)\b", text, re.MULTILINE)
    if platform in {"qortal", "qortium"}:
        expected = platform.capitalize()
        if not title_platform or title_platform.group(1) != expected:
            diag.error(path, 1, f"{platform} skill title must declare its {expected} boundary")
        expected_prefix = f"{platform}-"
        if name and not name.startswith(expected_prefix):
            diag.error(path, 1, f"{platform} skill name must begin '{expected_prefix}'")

    for heading in REQUIRED_HEADINGS:
        marker = f"## {heading}"
        if marker not in text:
            diag.error(path, 1, f"missing canonical heading '{marker}'")

    if maturity == "verified-runtime":
        freshness = "## Freshness and compatibility gate"
        if freshness not in text or not text.split(freshness, 1)[1].split("\n## ", 1)[0].strip():
            diag.error(path, 1, "verified-runtime skill needs a non-empty freshness/revalidation rule")

    check_links(path, text, diag)


def check_index(expected: set[Path], diag: Diagnostics) -> None:
    path = SKILLS / "README.md"
    text = path.read_text(encoding="utf-8")
    start = text.find("## Skill index")
    end = text.find("\n## ", start + 1)
    section = text[start : end if end != -1 else len(text)] if start != -1 else ""
    if not section:
        diag.error(path, 1, "missing '## Skill index' section")
        return
    links: list[Path] = []
    for match in INDEX_LINK_RE.finditer(section):
        target = match.group(1)
        resolved = (path.parent / target).resolve()
        if not resolved.is_file():
            diag.error(path, line_of(text, match.group(0)), f"index contains dead skill entry: {target}")
        else:
            links.append(resolved)
    counts = Counter(links)
    for skill, count in sorted(counts.items()):
        if count > 1:
            diag.error(path, 1, f"index contains skill more than once: {skill.relative_to(ROOT)}")
    indexed = set(links)
    for skill in sorted(expected - indexed):
        diag.error(path, 1, f"active skill missing from index: {skill.relative_to(ROOT)}")
    for skill in sorted(indexed - expected):
        diag.error(path, 1, f"index points to non-active skill: {skill.relative_to(ROOT)}")
    check_links(path, text, diag)


def main() -> int:
    diag = Diagnostics()
    names: dict[str, Path] = {}
    expected: set[Path] = set()
    for platform, directory in active_skill_dirs():
        path = directory / "SKILL.md"
        if path.is_file():
            expected.add(path.resolve())
        check_skill(platform, directory, names, diag)
    check_index(expected, diag)
    if diag.errors:
        print("Skills validation failed:", file=sys.stderr)
        print("\n".join(diag.errors), file=sys.stderr)
        return 1
    print(f"Skills validation passed: {len(expected)} active skills indexed exactly once.")
    return 0


def self_test() -> int:
    """Exercise representative failures in an isolated disposable copy."""
    cases = (
        ("missing heading", "skills/qortium/qdn-media-readiness/SKILL.md",
         "## Non-goals\n", "missing canonical heading"),
        ("invalid maturity", "skills/qortium/qdn-media-readiness/SKILL.md",
         "`verified-reference`", "maturity must be one of"),
        ("missing index entry", "skills/README.md",
         "| [`skills/qortium/qdn-media-readiness/SKILL.md`](qortium/qdn-media-readiness/SKILL.md) | `qortium` | `verified-reference` | Qortium AUDIO/VIDEO readiness before playback and bounded fetch/poll. | `2026-09-13` |\n",
         "active skill missing from index"),
    )
    for label, relative, original, expected_error in cases:
        with tempfile.TemporaryDirectory(prefix="skills-validator-") as temporary:
            copied_root = Path(temporary) / "repo"
            shutil.copytree(ROOT, copied_root, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            target = copied_root / relative
            content = target.read_text(encoding="utf-8")
            if original not in content:
                print(f"self-test setup failed for {label}: expected fixture text is absent", file=sys.stderr)
                return 1
            target.write_text(content.replace(original, "", 1), encoding="utf-8")
            result = subprocess.run(
                [sys.executable, "tools/validate_skills.py"], cwd=copied_root,
                capture_output=True, text=True, check=False,
            )
            if result.returncode == 0 or expected_error not in result.stderr:
                print(f"self-test failed for {label}", file=sys.stderr)
                print(result.stderr, file=sys.stderr)
                return 1
            print(f"self-test passed: {label} is rejected")
    return 0


if __name__ == "__main__":
    if sys.argv[1:] == ["--self-test"]:
        raise SystemExit(self_test())
    if sys.argv[1:]:
        print("usage: validate_skills.py [--self-test]", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(main())
