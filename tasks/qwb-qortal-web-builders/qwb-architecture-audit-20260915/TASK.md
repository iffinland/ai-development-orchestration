# qwb-qortal-web-builders/architecture-audit-20260915: forensic audit + architecture decision package for the refreshed Qortal Web Builders app

Contract: /home/iffi/VsCodec-Projects/AI-Orchestration/AGENTS.md
Executing agent (actual executor; never inferred from this template or a role): **DeepSeek**
  — evidence: the analysis, source inspection and validation were produced by the DeepSeek model
  running through the local Codex CLI profile; per GIT-AND-HANDOFF.md the orchestration profile is
  not the executor.
Report/handoff writer: **DeepSeek**
Project ID / exact repo / base SHA / agent branch:
  - project: `qortal/qwb-qortal-web-builders` (newly registered)
  - audited artifact: `/home/iffi/VsCodec-Projects/QWB-Qortal-Web-Builders/-PUBLISHED-versioon`
    (immutable static golden master; **no Git metadata**, so no base SHA exists)
  - reference app: `iffinland/iffi-vaba-mees-QORTAL` `main` `64f55bf7b6f4a1a093f19413d3a985e61a9fad37`
  - application branch: **none** — no development repository exists yet (not authorized to create one)
Platform session router / canonical project context:
  `/home/iffi/VsCodec-Projects/Qortal/qortal-dev-workspace/AGENTS.md` and
  `/home/iffi/VsCodec-Projects/Qortal/qortal-dev-workspace/projects/qwb-qortal-web-builders.md` (created by this task)
Outcome and measurable exit criterion:
  FORENSIC AUDIT + ARCHITECTURE ONLY. Exit = every audit objective (static-site forensics, visual
  golden-master map, reference owner-pattern audit, current-platform compatibility, stack decision,
  owner-recognition architecture, content architecture, index/discovery decision, update/delete
  contract, inline-editing UX, development path, GitHub bootstrap plan, no-migration confirmation,
  phase plan, skill-harvest candidates, owner decisions, exact reference revisions, report paths,
  golden-master integrity proof) answered from source/runtime evidence, with zero implementation.
In scope / out of scope / invariants:
  - in: read-only analysis of the golden master, reference-app audit, current Core/Hub/qapp-core
    source verification, architecture proposal, audit reports in the canonical workspace location.
  - out: building the app, initialising content, migration tooling, QDN writes, deployment, release,
    modifying the golden master or any platform source, creating/promoting skills, claiming runtime PASS.
  - invariants: `-PUBLISHED-versioon` stays byte-identical; the Shadow Archives Studio owner-auth
    architecture is not a reference; Qortal contracts are never inferred from Qortium.
Applicable skills (path / maturity / freshness result):
  - `skills/qortal/qdn-derived-index-coherence` — `verified-runtime`, last checked 2026-09-13;
    freshness: Core/Hub pins unchanged at the gate → **compatible** (used for the index decision).
  - `skills/qortal/bridge-fetch-qdn-resource-normalization` — `verified-runtime`, 2026-09-13;
    freshness: `handleResponse` still JSON-parses `FETCH_QDN_RESOURCE` in Core `108bf191` → **compatible**.
  - `skills/qortal/private-chat-contact-form` — `verified-runtime`, 2026-09-15; cited as the current
    contract for a future contact form (reference app's stale DM envelope noted).
  - Not loaded (no matching need): cross-app-video-publishing, subwire-article-publishing,
    quitter-announcement, qortium/*.
  - No skill was created or updated by this task.
Proven reference implementation to reuse (or exact missing investigation delta):
  `iffinland/iffi-vaba-mees-QORTAL` @ `64f55bf7` re-read from source, every Qortal-dependent pattern
  re-verified against Core `108bf191` / Hub `12a573b2`. Status: no fresh clone existed, so a clean
  clone was created at `/home/iffi/VsCodec-Projects/github-clones/Qortal/iffi-vaba-mees-QORTAL`.
Required surfaces and real runtime acceptance steps:
  - none executed by this audit (read-only). Deferred to the implementation phases: owner mode in a
    real published-app context (impossible via the Hub dev proxy), real host publish/verify/reload,
    tombstone persistence after reload, visitor view without owner controls.
Reference freshness evidence / environment IDs:
  gate run 2026-09-15T12:51Z, live `git fetch`, all clean tracking checkouts equal to upstream:
  Core `108bf191d42d710ec617f535af30cfd82fc03c87`, Hub `12a573b27246e8a626b24794830c6bc432d1b05d`,
  qapp-core `0f9d6ac5134ef2f82c1444a74e78471ddc7eb7df`, qapp-templates `143cc7bffd265f543f96ef25bf1b58ef7bb04472`.
  No node endpoint was queried (no node-dependent claim was needed).
Authorized external actions (exact repo, branch, operation; otherwise none):
  **none.** No commit, push, tag, release, deploy, issue mutation or QDN write. Only read-only
  `git fetch`/`git clone` of public references and read-only `gh repo view` were performed.
Canonical report path / handoff branch:
  `/home/iffi/VsCodec-Projects/Qortal/qortal-dev-workspace/docs/qwb-qortal-web-builders/` (audits + validation)
  handoff branch: none (no push authorization; `handoff_sync = pending_authorization`)
Owner-only steps or reason owner validation is not applicable:
  Owner decisions D1–D9 in the architecture proposal §15 must be answered before implementation.
  Runtime/owner acceptance is not applicable to this task because nothing was implemented or published.
Capability-harvest expectation:
  Candidate skills identified but **not created** (requires owner-runtime PASS first):
  `qortal/registered-name-owner-mode`, `qortal/inline-owner-editing`, `qortal/qdn-content-crud`,
  optionally `qortal/qdn-app-asset-strategy`. Explicitly rejected: `static-site-to-managed-qapp`
  (no migration methodology to reuse).
