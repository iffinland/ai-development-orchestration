# Skill promotion — orchestration/qortal-skill-promotion-20260914

Executing agent (actual executor of the work): **DeepSeek** (via the Codex CLI harness).
Report/handoff writer: DeepSeek.
Executing-agent evidence: `CODEX_HOME=/home/iffi/.codex-deepseek`, `config.toml`
`model = "deepseek-flash"`, `model_provider = "deepseek"`,
`base_url = "https://api.deepseek.com/"`, `DEEPSEEK_API_KEY` set, `CODEX_VERSION=0.154.0`.
The harness is Codex; the work is not attributed to Codex.
Verdict: promote the accepted Shadow Archives Qortal knowledge into the shared library.
Exact repository / branch / base SHA: `/home/iffi/VsCodec-Projects/AI-Orchestration`;
`agent/orchestration/qortal-skill-promotion-20260914`; base
`c2cffde7a48b2495a896297c0634f4303a12bc12`.

## Skills created or updated

| Skill path | Change | Maturity before → after |
| --- | --- | --- |
| `skills/qortal/cross-app-video-publishing/SKILL.md` | Promoted: rewritten from a candidate investigation accelerator into the owner-runtime-verified Q-Tube interoperability contract. | `candidate` → `verified-runtime` |
| `skills/qortal/subwire-article-publishing/SKILL.md` | New. | — → `verified-runtime` |
| `skills/qortal/quitter-announcement/SKILL.md` | New. | — → `verified-runtime` |
| `skills/qortal/qdn-derived-index-coherence/SKILL.md` | New. | — → `verified-runtime` |
| `skills/qortal/bridge-fetch-qdn-resource-normalization/SKILL.md` | New. | — → `verified-runtime` |

## Index / routing changes

- `skills/README.md`: added a `## Skill index` routing table (path, platform, maturity, use-for,
  last checked) covering all nine current skills, plus the Qortal/Qortium non-interchange warning.
- `skills/shared/capability-harvest/SKILL.md`: procedure step 1 now points at that index as the
  canonical routing entry for the search step. No harvest decision rules changed.

## Evidence used

- Accepted owner-runtime checkpoint (2026-09-13):
  `docs/shadow-archives-webportal/handoffs/2026-09-13-owner-runtime-checkpoint.md`.
- `docs/shadow-archives-webportal/validation/2026-09-13-video-qtube-contract-live-read-only-validation.md`
  and `docs/shadow-archives-webportal/implementation/2026-09-13-video-owner-publishing-implementation-report.md`.
- `docs/shadow-archives-webportal/validation/2026-09-13-blog-subwire-quitter-contract-live-read-only-validation.md`
  and `docs/shadow-archives-webportal/implementation/2026-09-13-blog-subwire-quitter-owner-publishing-implementation-report.md`.
- `docs/shadow-archives-webportal/handoffs/2026-09-13-gallery-owner-workflow-index-coherence-owner-handoff.md`
  and `docs/shadow-archives-webportal/runtime/2026-09-13-gallery-host-read-contract-and-media-rendering-report.md`.
- `docs/shadow-archives-webportal/live-evidence/2026-09-13-blog-subwire-quitter-live-read-only.json`
  and `.../2026-09-13-nodes-status.json`.

## Source / runtime pins recorded

`Qortal/q-tube` `main` `68c3ea706c4ab110ffa44a7f55f8e09bdf7e85ff`;
`Qortal/Subwire` `master` `a933a6c44d60db19cd219408e36c747aebcce994`;
`Qortal/Quitter` `master` `4e4246c3283bcbc8e05e683260692ed36144f862`;
`Qortal/qortal` (Core 6.1.9) `master` `108bf191d42d710ec617f535af30cfd82fc03c87`
(live nodes reported `qortal-6.1.9-108bf19`);
`Qortal/Qortal-Hub` `develop` `12a573b27246e8a626b24794830c6bc432d1b05d`;
`Qortal/qapp-core` `master` `0f9d6ac5134ef2f82c1444a74e78471ddc7eb7df`.
Live read-only nodes `127.0.0.1:24991` / `:24992`, heights 2722895–2723000 (2026-09-13).
Verified live identifier prefixes: SubWire `7l1NGsWiY0SgPb-FJVWQM-T60ZadsfPsbLTh-`,
Quitter `MhNiRYdzkaP9dz-kX47dT-XrFXaYetyErMdF-`.
Bridge shim runtime provenance: `/apps/q-apps.js` md5 `3ae7deaa55f353dc0ae4e8d13f3c1034`,
37 604 bytes, byte-identical to the Core `108bf191` clone file.

## Preserved owner work

The pre-existing uncommitted `AGENTS.md`, `GIT-AND-HANDOFF.md`, `WORKFLOW.md` modifications and the
untracked `templates/REPORT.md` were left byte-identical and were not staged or committed.

## Required checks not executed and why

No application build/test/lint is applicable: no application source was changed. No new runtime
test was run; the runtime layer is the already-accepted owner checkpoint, and this task only
records it.
