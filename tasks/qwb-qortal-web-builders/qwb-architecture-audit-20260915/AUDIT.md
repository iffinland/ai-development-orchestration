# QWB architecture audit — summary handoff

Executing agent (registered role of the agent that actually produced this work): **DeepSeek**
Report/handoff writer (if different from the executing agent): same
Executing-agent evidence: the audit was executed by the DeepSeek model through the local Codex CLI
profile; the profile is an orchestration surface and is not the executor
(`GIT-AND-HANDOFF.md`, "Agent identity in reports and handoffs").
Report type: forensics + architecture decision package (read-only; no implementation)
Exact application repository / branch / SHA: **no application repository exists yet**; audited
artifact is the static golden master (no Git metadata). Reference app `iffinland/iffi-vaba-mees-QORTAL`
`main` @ `64f55bf7b6f4a1a093f19413d3a985e61a9fad37`.
Canonical report root:
`/home/iffi/VsCodec-Projects/Qortal/qortal-dev-workspace/docs/qwb-qortal-web-builders/`
(platform reports stay canonical there per `report-storage-policy.md`; this file is the
cross-platform handoff summary and does not replace them).

Status: **AUDIT COMPLETE — IMPLEMENTATION NOT STARTED, NOT AUTHORIZED, NOT CLAIMED AS VERIFIED**

## Reports (canonical, in the Qortal workspace)

| Report | File |
| --- | --- |
| Static-site forensics (+ integrity result) | `docs/qwb-qortal-web-builders/audits/2026-09-15-qwb-static-site-forensics.md` |
| Visual preservation map | `docs/qwb-qortal-web-builders/audits/2026-09-15-qwb-visual-preservation-map.md` |
| Reference owner/editing pattern audit | `docs/qwb-qortal-web-builders/audits/2026-09-15-qwb-iffi-vaba-mees-owner-pattern-audit.md` |
| Platform compatibility + write/delete contract | `docs/qwb-qortal-web-builders/audits/2026-09-15-qwb-qortal-platform-compatibility-and-write-contract.md` |
| Target architecture proposal (stack, owner mode, content, index, UX, phases, decisions) | `docs/qwb-qortal-web-builders/audits/2026-09-15-qwb-target-architecture-proposal.md` |
| SHA-256 manifest (50 files) | `docs/qwb-qortal-web-builders/validation/2026-09-15-qwb-golden-master-sha256.txt` |
| Integrity proof (pre/post identical) | `docs/qwb-qortal-web-builders/validation/2026-09-15-qwb-golden-master-integrity.txt` |
| Project context (created by this task) | `projects/qwb-qortal-web-builders.md` |

## Headline findings

1. **Golden master integrity: PASS.** 50 files / 8,897,400 bytes, all SHA-256 digests identical
   before and after the audit; no directory mtime inside it belongs to this session.
2. **The published site is a 6-page static Bootstrap 5.2.2 site** with a bespoke theme layer, vendored
   jQuery 2.2.3, no build tooling and no data layer; Qortal integration is only `qortal://` deep links.
3. **Verified rendered reality differs from the declared design**: no `<meta name="viewport">` on any
   page; Montserrat/Open Sans/Poppins never load (system sans-serif in practice); a CSS leak from a
   corrupted SCSS tail renders all body copy as capitalised 15 px dark text; `click-scroll.js` throws
   an uncaught TypeError on the "Contact" nav click and on document scroll because `#section_4` does
   not exist. These are artefacts to *not* preserve.
4. **The reference app is a modal-based, owner-only publishing app** (React 19 + Vite, HashRouter) with
   a strong reusable pattern (reader-side publisher gate, fail-closed identity resolution) and clear
   debt (hardcoded owner name, `names[0]` detection, no `_qdn*` usage, optimistic writes, **no delete
   at all**, per-item body fetches for filtering).
5. **Current Qortal facts that shape the design:** no app-accessible QDN delete exists (the only
   delete is a node-local, API-key admin REST call); re-publishing the same
   `(name, service, identifier)` overwrites with last-write-wins and no CAS; gateway context resolves
   interactive actions with an `{error}` object instead of rejecting; hub approval is session-cached
   after the first publish; `_qdnName` is the app's publishing identity and is empty in dev-proxy
   context, so owner mode cannot be tested locally.
6. **Recommended stack: Vite + TypeScript + vanilla DOM component modules** (visual fidelity, low
   bundle cost, bounded interactivity); React is the fallback if the app grows past ~12 views or
   requires complex rich editing. The deciding argument against `qapp-core` is that it is a React +
   MUI library that conflicts with the preserved bespoke visual identity.
7. **Recommended owner architecture:** derive ownership from `_qdnName` ∈ current account's name list
   (via `GET_USER_ACCOUNT` + `GET_ACCOUNT_NAMES`), fail closed, never persist `owner=true`,
   re-verify before every write.
8. **Recommended content/delete model:** `qwb_*`-prefixed entities (singleton `site` + per-entity
   highlights/services/steps/works/prices/optional articles), media in `THUMBNAIL`/`IMAGE`,
   `rev`-verified updates, **logical deletion via tombstones**, bounded prefix discovery with **no
   derived index in v1**.
9. **No migration/import script** — confirmed, and none was written.
10. **Development path reserved:** `/home/iffi/VsCodec-Projects/QWB-Qortal-Web-Builders/qortal-web-builders`
    (empty directory only; no scaffold, no `git init`). GitHub remote verified empty:
    `https://github.com/iffinland/QWB-Qortal-Web-Builders`.

## Evidence by layer

| Layer | Executed | Result |
| --- | --- | --- |
| Static inventory + SHA-256 | yes | 50 files, manifest + integrity proof |
| Static source analysis (HTML/CSS/JS) | yes | forensics report |
| Rendered visual + computed-style runtime | yes (headless Chrome 153, `file://`) | 5 screenshots + computed-style/behaviour probes |
| Reference-app source audit | yes (clean clone @ `64f55bf7`) | owner-pattern report |
| Platform source verification | yes (Core/Hub/qapp-core pins, live fetch gate) | compatibility + write/delete contract report |
| Real Qortal host | **no** | not applicable to an audit; required in implementation Phases 2–4 |
| Live node API / QDN read | **no** | no node-dependent claim was needed |
| QDN write / publish / delete | **no** | explicitly prohibited by the task |
| Workspace validators | yes | `tools/validate-workspace.sh` → PASS (5 pre-existing warnings); `tools/validate_skills.py` → PASS |

## Files changed (all outside the golden master)

- created: 5 audit reports + 2 validation artifacts under
  `Qortal/qortal-dev-workspace/docs/qwb-qortal-web-builders/`
- created: `Qortal/qortal-dev-workspace/projects/qwb-qortal-web-builders.md`
- modified: `AI-Orchestration/PROJECT-REGISTRY.md` (one registry row added — mandated by
  `AGENTS.md` "For an unregistered project … add a registry row")
- created: this task directory (`TASK.md`, `AUDIT.md`, `STATUS.json`)
- created: empty reserved directory `QWB-Qortal-Web-Builders/qortal-web-builders/`
- created: new clean reference clone `github-clones/Qortal/iffi-vaba-mees-QORTAL`
- created (temporary): `/tmp/qwb-audit-shots/` screenshots and probes, `/tmp/qwb-golden-master-sha256.txt`

## Checks not executed and why

- No build/lint/test of any application: no application exists and the task forbids building it.
- No `npm install`/build of the reference clone: unnecessary for a source-level pattern audit.
- No real-host or live-node validation: belongs to implementation phases and needs owner authorization.

## Adversarial self-audit

- Corrected an initial assumption that the inline `body{font-family:Arial}` override applied; the
  computed-style probe proved the opposite, and the reports state rendered reality.
- Corrected an initial claim that `custom.js` throws on scroll (its throwing line is inside an
  unreachable per-item callback) and an initial claim that the reference app's DM envelope is broken
  (current Hub accepts both `recipient` and `destinationAddress`).
- Verified the "no QDN delete" conclusion from three independent places (Core bridge action list,
  Core Java sources, Hub request handlers) before treating it as decisive.
- No claim of runtime PASS, owner acceptance or platform modification is made anywhere.

## External actions (commit/push/tag/release/deploy/QDN write/transaction)

**None.** Read-only `git fetch`/`git clone` of public references and `gh repo view` only. No commit,
push, tag, release, deployment, issue mutation, QDN publication or transaction was performed. The
handoff artifacts are local; `handoff_sync = pending_authorization`.

## Remaining risks and follow-up

- Architecture approval is pending; implementation must not start before the owner answers D1–D9.
- `WEBSITE` vs `APP` service choice changes URLs and routing; decided as D1 with a recommendation.
- Stock photography has unknown provenance/licence (D4).
- Skill harvest is deliberately deferred until owner-runtime PASS.

## Report saved

- Absolute path:
  `/home/iffi/VsCodec-Projects/AI-Orchestration/tasks/qwb-qortal-web-builders/qwb-architecture-audit-20260915/AUDIT.md`
