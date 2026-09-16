# qwb-qortal-web-builders/phase-0-1-20260915: Phase 0–1 repository, tooling and public visual baseline for Qortal Web Builders

Contract: /home/iffi/VsCodec-Projects/AI-Orchestration/AGENTS.md
Executing agent (actual executor; never inferred from this template or a role): **DeepSeek**
  — evidence: the repository scaffold, all source modules, styles, tests, the golden-master
  screenshot comparison, the contrast measurements, the self-audit and the commit contents were
  produced by the DeepSeek model running through the local Codex CLI profile; per
  GIT-AND-HANDOFF.md the orchestration profile is not the executor.
Report/handoff writer: **DeepSeek**
Project ID / exact repo / base SHA / agent branch:
  - project: `qortal/qwb-qortal-web-builders`
  - repository: `git@github.com:iffinland/QWB-Qortal-Web-Builders.git`
    (local `/home/iffi/VsCodec-Projects/QWB-Qortal-Web-Builders/qortal-web-builders`)
  - base SHA: **none** — the repository had no commits before this task (`git init -b main` in Phase 0);
    `git ls-remote origin` returned empty at task start, confirming it was still unpublished
  - agent branch: `agent/qwb/phase-0-1` (also `main`, same commit)
  - head: `18d760d011e956829714e7489432949829fa1840`
  - immutable golden master: `/home/iffi/VsCodec-Projects/QWB-Qortal-Web-Builders/-PUBLISHED-versioon`
    (read-only; byte-identical before and after, verified twice)
Platform session router / canonical project context:
  `/home/iffi/VsCodec-Projects/Qortal/qortal-dev-workspace/AGENTS.md` and
  `/home/iffi/VsCodec-Projects/Qortal/qortal-dev-workspace/projects/qwb-qortal-web-builders.md`
Outcome and measurable exit criterion:
  Phase 0 + Phase 1 implemented and pushed. Exit = (a) a clean development repository with green
  build/lint/test and recorded reference pins + asset attribution; (b) the public visual baseline
  rendered from typed seed content and screenshot-comparable to the golden master with intentional
  deviations documented; (c) no owner controls and no bridge call; (d) implementation branch pushed
  with a verified remote SHA. **All met.** Stopped after Phase 1 as instructed.
In scope / out of scope / invariants:
  - in: Phase 0 (repo, tooling, structure, reference pins, asset/source attribution, initial Git
    history) and Phase 1 (public views, tokens/theme, responsive behaviour, seed content,
    responsive/a11y baseline, tests, docs, commits, push).
  - out (explicitly not implemented): owner recognition, owner controls, add/edit/delete flows, QDN
    reads or writes, migration tooling, deployment/publication, skills promotion.
  - invariants: golden master byte-identical; no QDN read/write; no force-push or history rewrite;
    no secret/credential committed; no other repository's tracked state modified.
Applicable skills (path / maturity / freshness result):
  - **None loaded for Phase 0–1 execution.** The task is a presentation-layer rewrite: it made no
    bridge call, no QDN read and no QDN write, so no platform capability skill applied.
  - Consulted at audit time and **not re-used here** (recorded for continuity):
    `skills/qortal/qdn-derived-index-coherence`, `skills/qortal/bridge-fetch-qdn-resource-normalization`,
    `skills/qortal/private-chat-contact-form`.
  - Reuse-first check: no skill covers a static-site visual rebuild or a golden-master screenshot
    diff; the audit had already rejected a `static-site-to-managed-qapp` skill as non-methodological.
Proven reference implementation to reuse (or exact missing investigation delta):
  Visual source of truth was the golden master itself (its theme CSS `:root` tokens and component
  vocabulary), not a donor app. The reference app `iffinland/iffi-vaba-mees-QORTAL` @
  `64f55bf7b6f4a1a093f19413d3a985e61a9fad37` was **not** reused architecturally, per the audit's
  owner-pattern classification. Platform pins re-verified equal to the audit, so no delta existed.
Required surfaces and real runtime acceptance steps:
  - executed: local production build + `vite preview`; headless Chrome 153.0.8010.36 runtime probes
    (routing, legacy anchors, cross-view anchors, mobile navbar collapse, tab keyboard/ARIA, skip
    link, image loading, fonts, 404 view); screenshot comparison against the golden master at
    1440 px and 390 px; pixel-level contrast measurement; `dist/` dependency and URL audit.
  - pending (owner-only / later phases): real Qortal host render, owner-mode appearance for the
    publishing name's owner vs a visitor, QDN read/write round-trips, owner acceptance.
Reference freshness evidence / environment IDs:
  Re-verified 2026-09-15 14:20 UTC by `git rev-parse HEAD` on each clone; all equal to the audit:
  Core `108bf191d42d710ec617f535af30cfd82fc03c87`, Hub `12a573b27246e8a626b24794830c6bc432d1b05d`
  (branch `develop`), qapp-core `0f9d6ac5134ef2f82c1444a74e78471ddc7eb7df`,
  qapp-templates `143cc7bffd265f543f96ef25bf1b58ef7bb04472`,
  `iffi-vaba-mees-QORTAL` `64f55bf7b6f4a1a093f19413d3a985e61a9fad37`.
  Clones live under `/home/iffi/VsCodec-Projects/github-clones/Qortal/`. No node endpoint was
  queried (no node-dependent claim was made).
Authorized external actions (exact repo, branch, operation; otherwise none):
  - **authorized and performed:** commits and push in `iffinland/QWB-Qortal-Web-Builders` —
    `main` and `agent/qwb/phase-0-1` → `18d760d011e956829714e7489432949829fa1840`
    (verified with `git ls-remote origin`).
  - **not authorized / not performed:** handoff-repository commit or push, tags, releases,
    deployment, QDN publication, signing, transactions, issue mutation.
    `handoff_sync = pending_authorization` for this orchestration repository.
Canonical report path / handoff branch:
  `/home/iffi/VsCodec-Projects/Qortal/qortal-dev-workspace/docs/qwb-qortal-web-builders/implementations/2026-09-15-qwb-phase-0-1-implementation.md`
  (final SHA-256 `3b3e5af213a37f0f139976c36fa35743a92bb1878089ac5e0c84e9aebaab74b8`, 392 lines,
  re-measured at `2026-09-15T14:47:00Z`; supersedes the `577a8780bec6593bbfc0701c5fa0d00179615cff48de96972fd5d7d83d180568`
  body digest — 364 lines — that was recorded here earlier, before the handoff additions to §4/§5
  and the clarified "Report saved" block. Both digests are stated in the report itself.)
  Companion visual evidence (durable, archived from `/tmp/qwb-baseline/`):
  `docs/qwb-qortal-web-builders/implementations/2026-09-15-qwb-phase-1-visual-evidence/`
  — 12 comparison PNGs (golden master left / new build right) plus `SHA256SUMS.txt` and `README.md`.
  Handoff branch: none — these artifacts are prepared locally under
  `tasks/qwb-qortal-web-builders/qwb-phase-0-1-20260915/` and are **not** committed or pushed.
  STATUS: `STATUS.json` (state `review_pending`, `handoff_sync = pending_authorization`); this task
  also carries `IMPLEMENTATION.md`. No `AUDIT.md`: no independent review was performed — the audit
  was the executing agent's own adversarial self-audit, recorded in the report §7.
Owner-only steps or reason owner validation is not applicable:
  Owner validation is **not applicable to Phase 0–1 completion** (the phase delivers a code baseline,
  not a published product), but owner input is required before the next phases:
  1. confirm the three unDraw illustrations' licence position (recorded as *unDraw-assumed*, not
     proven from the files);
  2. decide the one known contrast failure — white navbar links on the gradient at 2.10:1
     (Phase 4 scope; the fix options are design-level);
  3. the D1–D9 decisions the audit already raised remain the entry conditions for Phase 2
     (staging name, dev-override policy, etc.).
Capability-harvest expectation:
  **Project-specific — no skill created or updated.** Phase 0–1 made no bridge call and no QDN
  read/write, so it produced no reusable Qortal capability. The audit's four candidate skills
  (`qortal/registered-name-owner-mode`, `qortal/inline-owner-editing`, `qortal/qdn-content-crud`,
  optional `qortal/qdn-app-asset-strategy`) remain unpromoted; each still requires an owner-runtime
  PASS in a real host.
