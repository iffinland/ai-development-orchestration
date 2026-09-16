# qortal/qwb-qortal-web-builders/qwb-rc-7fd03fc-staging-confirmation-20260916: confirm release candidate `7fd03fc` on staging

Contract: /home/iffi/VsCodec-Projects/AI-Orchestration/AGENTS.md
Executing agent (actual executor; never inferred from this template or a role): **DeepSeek**
(evidence in `STATUS.json` → `executing_agent_evidence`)
Project ID / exact repo / base SHA / agent branch:
`qortal/qwb-qortal-web-builders`; `git@github.com:iffinland/QWB-Qortal-Web-Builders.git`
(local `/home/iffi/VsCodec-Projects/QWB-Qortal-Web-Builders/qortal-web-builders`);
base `7fd03fc5b2d39d80b20ccaa9c7a07355d85dc94a`; branch `agent/qwb/phase-4-runtime-fix`
Platform session router / canonical project context:
`/home/iffi/VsCodec-Projects/Qortal/qortal-dev-workspace/docs/qwb-qortal-web-builders/`
(project context `projects/qwb-qortal-web-builders.md`)
Outcome and measurable exit criterion:
Publish the release-candidate build to the staging resource `WEBSITE / Q-Website / default` and
confirm **only** the production-bootstrap fix (`e7bf357`) in the real Hub: (1) the published synthetic
QDN entities still render, (2) the untouched shipped seed items render beside them, (3) those items
still expose the owner inline controls, (4) a hard reload preserves both, (5) no tombstoned item is
resurrected. Exit = all five checks PASS, the staging revision recorded, and `7fd03fc` marked
production-ready. Any defect = stop and report before production publication.
In scope / out of scope / invariants:
In scope — one staging `WEBSITE` publish, the five bounded runtime checks, evidence and documentation.
Out of scope — publishing production; touching `WEBSITE / Qortal Web Builders / default`; repeating
the Phase 4 §14 owner-runtime suite; re-running automated gates for unchanged source; any entity
write; any importer/migration; merging `main`. Invariants — production identity untouched, no node API
key, no force push, no tags/releases, no other project's checkout modified.
Applicable skills (path / maturity / freshness result):
`skills/qortal/qdn-content-crud/SKILL.md` — verified-runtime, last checked 2026-09-16; compatible (the
staging publish and the read-back checks follow its contract).
`skills/qortal/registered-name-owner-mode/SKILL.md` — verified-runtime, last checked 2026-09-16;
compatible (owner mode had to be live for check 3).
`skills/qortal/inline-owner-editing/SKILL.md` — verified-runtime, last checked 2026-09-16; compatible
(it defines the one-entity-at-a-time flow the confirmed fix makes possible).
`skills/shared/capability-harvest/SKILL.md` — verified-runtime, last checked 2026-09-16; used for the
harvest decision.
Proven reference implementation to reuse (or exact missing investigation delta):
Qortal Hub 3.0.3 source at `/home/iffi/VsCodec-Projects/github-clones/Qortal/Qortal-Hub`
(`src/encryption/encryption.ts::publishOnQDN`, `src/qdn/publish/publish.ts::publishData`,
`src/components/Apps/AppPublish.tsx`) and the Phase 4 runtime evidence under
`docs/qwb-qortal-web-builders/implementations/2026-09-16-qwb-phase-4-runtime-evidence/run-2026-09-16-resumed/`.
Required surfaces and real runtime acceptance steps:
Qortal Hub 3.0.3 (Linux/Electron) with the real staging resource in the app iframe; the five checks
above, each read from the live DOM / node, with a hard reload (Hub `refreshApp`) between observations.
Reference freshness evidence / environment IDs:
Mainnet `qortal-6.1.9-108bf19` at `127.0.0.1:24991` and `:24992`, `syncPercent` 100, height 2 725 983
at run start; Hub 3.0.3 (`Chrome/128.0.6613.186`, `Electron/32.3.1`); owner account
`QNwV9VV82UUZmMkDZZbEMAKPpCx7otnnsi`; Hub approval-state and version strings read live.
Authorized external actions (exact repo, branch, operation; otherwise none):
- `git@github.com:iffinland/QWB-Qortal-Web-Builders.git`, branch `agent/qwb/phase-4-runtime-fix` —
  **no new commit** (no source changed); existing commit left untouched.
- `git@github.com:iffinland/qortal-dev-workspace.git`, branch
  `agent/qwb-qortal-web-builders/phase-4-checkpoint-docs-20260916` — commit and push the report,
  evidence directory and the project-context status update.
- `git@github.com:iffinland/ai-development-orchestration.git`, branch
  `agent/orchestration/qwb-rc-7fd03fc-staging-confirmation-20260916` — commit and push this task record.
- QDN: **one** staging `WEBSITE` publish to `WEBSITE / Q-Website / default` (owner-signed through the
  Hub wallet). Production publish **not** authorized.
Canonical report path / handoff branch:
`…/qortal-dev-workspace/docs/qwb-qortal-web-builders/validation/2026-09-16-qwb-rc-7fd03fc-staging-confirmation.md`
(evidence in `…/2026-09-16-qwb-rc-7fd03fc-staging-confirmation-evidence/`);
handoff on `agent/qwb-qortal-web-builders/phase-4-checkpoint-docs-20260916` and
`agent/orchestration/qwb-rc-7fd03fc-staging-confirmation-20260916`.
Owner-only steps or reason owner validation is not applicable:
Not applicable. The confirmation is a staging runtime check performed for the owner; the owner-only
step that remains is the authorization to publish
`WEBSITE / Qortal Web Builders / default`, which belongs to a separate publication task.
Capability-harvest expectation (likely reusable capability or project-specific):
Project-specific / no harvest expected — the checked behaviour is QWB's shipped-seed baseline rule, not
a reusable Qortal platform contract. Any durable learning belongs in the three existing verified-runtime
skills only if a platform-level contract is found to be wrong.
