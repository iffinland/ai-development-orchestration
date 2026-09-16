# Implementation — qortal/qwb-qortal-web-builders/phase-0-1-20260915

Executing agent (actual executor of the work): **DeepSeek**
Report/handoff writer (if different from the executing agent): same (`DeepSeek`)

Executing-agent evidence: the repository scaffold, every source module, style sheet, test, the
golden-master screenshot comparison, the contrast measurements, the self-audit fixes and the commit
contents were produced by the **DeepSeek** model running through the local Codex CLI profile. Per
`AI-Orchestration/GIT-AND-HANDOFF.md` the CLI/orchestration profile is not the executor, so the
executing agent is `DeepSeek`, not `Codex`/`Codex Local`.

Exact application repository / branch / SHA:
- `git@github.com:iffinland/QWB-Qortal-Web-Builders.git`
  (local `/home/iffi/VsCodec-Projects/QWB-Qortal-Web-Builders/qortal-web-builders`)
- branch `agent/qwb/phase-0-1` @ `18d760d011e956829714e7489432949829fa1840` (`main` carries the same
  commit; the repository had no commits before this task, so there is no base SHA)
- remote verified: `git ls-remote origin` → both refs at the SHA above

Verdict and measurable acceptance achieved: **Phase 0 and Phase 1 delivered; the task stopped there.**
- Phase 0 — a clean Vite + TypeScript + vanilla-DOM repository with tooling, structure, reference
  pins, asset/source attribution, documentation and initial Git history; typecheck, ESLint, Prettier,
  47 Vitest tests and the production build are all green.
- Phase 1 — the complete public visual baseline (home with hero, featured pair, tabbed Browse Topics
  strip, step cards, pricing and contact; completed works; article index; article detail; not-found)
  rendered from typed seed content, screenshot-compared against the immutable golden master at
  1440 px and 390 px, with 16 intentional deviations documented and the legacy jQuery/plugin layer and
  audited rendering defects removed. No owner recognition, no owner controls, no add/edit/delete flow,
  no QDN read and no QDN write exist in the code.
- Invariants held: the golden master is byte-identical (50/50 SHA-256 digests, 8,897,400 bytes, 0
  differences, re-verified at handoff); no secret or credential added; no force-push, no history
  rewrite, no destructive Git command; no other repository's tracked state changed.

Changes and preserved owner work:
- New repository content only: 24 files in commit `aa222a9` (Phase 0) and 39 files in `5879136`
  (Phase 1) plus one file in `18d760d` (self-audit contrast token).
- Nothing was moved, deleted or rewritten in any pre-existing repository. The golden master
  `-PUBLISHED-versioon` was never built, formatted, edited, initialised as a Git repository, added as a
  remote/submodule/worktree or copied into the app repository.
- Pre-existing uncommitted work elsewhere was left untouched: the dirty `PROJECT-REGISTRY.md` and the
  untracked `tasks/qwb-qortal-web-builders/` in `AI-Orchestration`, and the untracked report/project
  files in `qortal-dev-workspace`. No commit or push was made in either repository.

Skills used (path / maturity / freshness result): **none applied.**
- Loaded for execution: none — Phase 0–1 makes no bridge call and no QDN read/write, so no platform
  capability skill matched.
- Consulted at audit time, not reused: `skills/qortal/qdn-derived-index-coherence`,
  `skills/qortal/bridge-fetch-qdn-resource-normalization`, `skills/qortal/private-chat-contact-form`.
- Reuse-first check: no skill covers a static-site visual rebuild or a golden-master screenshot diff;
  the audit had already rejected `static-site-to-managed-qapp` as non-methodological.
- Reference freshness: all five pinned revisions re-verified by `git rev-parse HEAD` and equal to the
  audit (Core `108bf191d42d710ec617f535af30cfd82fc03c87`, Hub `12a573b27246e8a626b24794830c6bc432d1b05d`,
  qapp-core `0f9d6ac5134ef2f82c1444a74e78471ddc7eb7df`, qapp-templates
  `143cc7bffd265f543f96ef25bf1b58ef7bb04472`, `iffi-vaba-mees-QORTAL`
  `64f55bf7b6f4a1a093f19413d3a985e61a9fad37`) → no delta to investigate.

Evidence by layer (commands/actions, timestamp, environment, results):
1. Golden-master SHA-256 diff vs the recorded manifest — host, GNU coreutils — 14:38 and 14:43 UTC —
   **PASS**, 0 differences across 50 files / 8,897,400 bytes; manifest digest
   `18e2a960cc126cb34ab68c432c5a8a1331c980fbb187db38f63d7ad063b95a43`.
2. Reference freshness/`git rev-parse HEAD` on the five clones — 14:20 UTC — equal to the audit.
3. Copied-asset verification (`sha256sum` vs manifest) — 10/10 byte-identical.
4. `npx tsc --noEmit`, `npx eslint .`, `npx prettier --check .` — 14:41–14:42 UTC — clean.
5. `npx vitest run` — jsdom/vitest 4.1.11 — **47/47 in 5 files**.
6. `npm run build` — vite 8.3.0 — success; the rebuild reproduces the reviewed `dist` byte-for-byte.
7. Headless Chrome 153.0.8010.36 runtime probes — routing, legacy `#section_*` anchors, cross-view
   anchors, mobile navbar collapse, tab keyboard/ARIA, skip link, fonts, images, 404 view.
8. Visual comparison against the golden master — matched 1440 px and 390 px captures through one
   harness — 12 archived comparison images.
9. Contrast measurement from rendered pixels (WCAG 2.1 relative luminance).
10. `dist` audit — 0 hits for jQuery, Bootstrap's JS bundle, the sticky/click-scroll plugins, React,
    MUI, Emotion and bootstrap-icons; no absolute asset URL.

Required checks not executed and why:
- Real Qortal host render in embedded Hub/Home: nothing is published in Phase 0–1 and a local preview
  never proves host behaviour.
- Owner-mode behaviour (owner vs visitor): owner recognition is out of scope; `_qdnName` is empty in
  the Hub dev proxy anyway.
- QDN read/write round-trips, media publish pipeline, deployment/publication: not implemented and not
  authorized.
- Non-Chromium browsers (Firefox/WebKit) and Windows/macOS rendering: not available in this
  environment; Chromium plus jsdom is what was run.
- Lighthouse/axe: deferred with the Phase 4 accessibility pass.

Self-audit or independent review (identify which): **adversarial self-audit by the executing agent
(`DeepSeek`)**; no independent review was performed. Nine findings were fixed in `18d760d`
(two HIGH: the skip link replaced the page under hash routing, and the home "Completed works" pane
rendered two cards in a three-column row; plus four MEDIUM and three LOW findings). One known
accessibility failure (white navbar links on the gradient at 2.10:1, identical in the golden master)
was deliberately left for the owner-approved Phase 4 contrast pass, with measurements recorded.

Capability harvest (none/project-specific OR exact skill paths + maturity change):
**project-specific — no skill created or updated.** Phase 0–1 produced no reusable Qortal capability
because it made no bridge call and no QDN read/write. The audit's four candidate skills
(`qortal/registered-name-owner-mode`, `qortal/inline-owner-editing`, `qortal/qdn-content-crud`,
optional `qortal/qdn-app-asset-strategy`) remain unpromoted; each still requires an owner-runtime PASS
in a real host.

Remaining findings / next actor / resume condition:
- Owner input requested before the next phases: (a) the licence position of the three bundled unDraw
  illustrations (recorded as *unDraw-assumed*, not proven from the files); (b) the inherited navbar
  link contrast decision; (c) the audit's D1–D9 entry decisions for Phase 2.
- Residual risks: placeholder portfolio covers are the most visible difference from the published
  site until Phase 3 supplies QDN media; smooth scrolling ignores `prefers-reduced-motion`.
- Next actor: the orchestration controller (`codex-local`) for handoff review. State is
  `review_pending`, which means reviewable, not product-ready.
- Resume condition for Phase 2: owner confirmation of the requested inputs plus an explicit
  authorization for the owner-recognition work; no structural rewrite is needed (views are pure
  renderers with a `mount(root, context)` seam, the content model is already write-shaped, and content
  access sits behind `ContentSource`).

Canonical detailed report path / SHA-256 / authorized remote evidence:
- `/home/iffi/VsCodec-Projects/Qortal/qortal-dev-workspace/docs/qwb-qortal-web-builders/implementations/2026-09-15-qwb-phase-0-1-implementation.md`
  — SHA-256 `3b3e5af213a37f0f139976c36fa35743a92bb1878089ac5e0c84e9aebaab74b8` (final 392-line file;
  it supersedes the `577a8780…` body digest recorded inside the report and in TASK.md before the
  handoff additions, which is itself recorded in the report's "Report saved" block)
- Companion visual evidence:
  `/home/iffi/VsCodec-Projects/Qortal/qortal-dev-workspace/docs/qwb-qortal-web-builders/implementations/2026-09-15-qwb-phase-1-visual-evidence/`
  (12 PNGs + `SHA256SUMS.txt` + `README.md`)
- Remote evidence: `git ls-remote origin` → `refs/heads/main` and `refs/heads/agent/qwb/phase-0-1`
  both `18d760d011e956829714e7489432949829fa1840`. The workspace report and this artifact have **no**
  authorized remote copy; they are local files.

Commit and push state / verified remote SHA:
- Application repository: three commits authored with executing-agent attribution in each body
  (`aa222a9`, `5879136`, `18d760d`); both `main` and `agent/qwb/phase-0-1` pushed and verified at
  `18d760d011e956829714e7489432949829fa1840`. No tag, release, deployment or QDN write.
- Orchestration handoff repository: **not committed and not pushed** — no authorization.
  `handoff_sync = pending_authorization`; `TASK.md`, `STATUS.json` and `IMPLEMENTATION.md` are local
  untracked files under `tasks/qwb-qortal-web-builders/qwb-phase-0-1-20260915/`. No `AUDIT.md` was
  created because no independent review happened.
