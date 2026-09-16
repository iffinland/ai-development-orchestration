# Implementation / handoff — qortal/qwb-qortal-web-builders/qwb-phase-4-checkpoint-20260916

Executing agent (actual executor of the work): **DeepSeek**
Report/handoff writer (if different from the executing agent): same (`DeepSeek`)
Executing-agent evidence: the source analysis, the isolated-worktree reproduction, the gate runs and
every documentation edit were produced by the **DeepSeek** model running through the local Codex CLI
profile; per `AI-Orchestration/GIT-AND-HANDOFF.md` the CLI/orchestration profile is not the executor.

## Exact revisions

| Repository | Branch | Base | Head | Remote |
| --- | --- | --- | --- | --- |
| `git@github.com:iffinland/QWB-Qortal-Web-Builders.git` | `agent/qwb/phase-4-runtime-fix` | `741754becb79a131c699f2468fe096fdacd00c19` | `7fd03fc5b2d39d80b20ccaa9c7a07355d85dc94a` | pushed, `git ls-remote` verified |
| `git@github.com:iffinland/qortal-dev-workspace.git` | `agent/qwb-qortal-web-builders/phase-4-checkpoint-docs-20260916` | `b8fd2f6fbfcff88c0ab9bc8fd116d5548679d2d2` (`origin/main`) | `8c16550b729a2c5cc858796c24ee4d35fc6f6a46` | pushed, `git ls-remote` verified |
| this repository | `agent/orchestration/qwb-phase-4-checkpoint-20260916` | `9a611a21af469478a253fc664ab295d8c37f69d4` | recorded in STATUS after push | pushed |

`main` is at `18d760d011e956829714e7489432949829fa1840` in the application repository and at
`b8fd2f6fbfcff88c0ab9bc8fd116d5548679d2d2` (`origin/main`) in the workspace repository: untouched in
both. No merge, no force push, no history rewrite, no tag, no release.

## 1. Production-bootstrap edge case — the answer

**Yes, the defect was real.** At `741754b` the QDN source built every kind's collection as
`emptyBundle(...)` and then replaced it wholesale with the discovered entities
(`withKind(bundle, read)` → `{ ...bundle, highlights: read.entities }`). The full shipped seed bundle
was rendered in exactly one place: the `nothing-published` early return, which requires
`entityCount === 0 && tombstones === 0 && site.site === null && searchErrors === 0 && simplyUnpublished`.
The first published entity makes `entityCount > 0`, so that path can never fire again and every kind
thereafter contains only what discovery returned. A never-published shipped item therefore stopped
rendering after someone else's first write — **and its inline `✎ / 🗑 / ↑ / ↓` controls stopped with
it**, so the approved §6.4 flow ("replace the shipped content one entity at a time") could not
bootstrap the site at all. The `site` singleton is a fixed-identifier read, so the shell survived; the
loss was at entity level across highlights, services, steps, works, prices and articles.

Reproduced, not inferred: the three test cases added by the fix were run unchanged against a detached
worktree of `741754b` (application source untouched, only the test file copied in). Two fail —
`expected [ … ] to have a length of 2 but got 1` after the first write, and a tombstoned shipped item
immediately resurrected.

## 2. The fix (`e7bf3578d8772330f313b468bc808d5c57c8bf22`)

`src/content/qdn-source.ts`: `KindRead` gained `identifiers` (every identifier discovery returned for
the kind after the exact name/service/prefix re-filter, whatever the payload read then did with it),
and `applySeedBaseline(read, shipped)` adds a shipped item **only when discovery did not report its
identifier at all**, and only when that kind's discovery answered without hitting the page budget.
The baseline is per entity, is not a mode or a flag, and terminates by itself once every shipped
identifier has been published or tombstoned. A new diagnostic reports how many shipped items render
this way.

Why this is the smallest correct change: it reuses the existing per-kind read result (no new module,
importer, migration, index or abstraction); duplicates are impossible because the identifier *is* the
entity identity and the editor re-publishes it (`assembleDraft` takes `id: request.id`, the edit flow
passes `id: entity.id`, and no form field can change it); the existing truthfulness invariant is
preserved (a reported identifier — active, tombstoned, invalid or unreadable — is never replaced by
its shipped default); a failed or truncated discovery contributes no default (fail-closed, consistent
with `agents/qortal-architecture-and-data-integrity.md`: partial discovery must not grant authority).

## 3. Validation

Transition validation, `tests/qdn-source.test.ts` → `pre-publication bootstrap baseline`, through the
real bridge wrapper and the real read/publish modules against the scripted node:

| Case | `741754b` | `7fd03fc` |
| --- | --- | --- |
| Untouched shipped items survive zero → first write → reload → second write (2/2 highlights, other kinds intact across both reloads) | FAIL (1/2) | PASS |
| A tombstoned shipped item is never resurrected | FAIL | PASS |
| The baseline contributes nothing once every identifier is reported | PASS | PASS |

Gate at `7fd03fc` (node v20.19.2): `tsc --noEmit` clean, `eslint .` clean, `prettier --check .` clean,
**25 files / 294 tests passed**, `npm run build` succeeded emitting `dist/assets/index-Cc7rTXmF.js`.
`git status --porcelain` empty; `git diff --check 741754b..HEAD` clean.

**Not re-run:** the Qortal Hub 3.0.3 owner-runtime procedure (Phase 4 §14). That is deliberate and
recorded as a residual: the change is a read-path merge rule, no write/owner-mode/inline-editing
contract changed — but the runtime-validated artifact (`741754b`) predates it, and the new rule
visibly changes what renders once content is published. A bounded owner confirmation on staging is
recommended before or at publication (report §6.2). No unrelated validation was re-run, because no
other source changed.

## 4. Documentation synchronization

- Application `README.md` and `docs/architecture.md` — Phase 3 owner-runtime validated; Phase 4 PASS
  and checkpoint closed; the write contract records the real staging run; the read contract documents
  the per-entity bootstrap baseline; the app never republishes the `WEBSITE` bundle and
  `WEBSITE / Qortal Web Builders / default` has never been written (commit `7fd03fc`).
- Workspace `projects/qwb-qortal-web-builders.md` — D1–D9 recorded as owner-approved with the accepted
  (implemented) state per decision; production identity `WEBSITE / Qortal Web Builders / default` and
  staging identity `WEBSITE / Q-Website / default`; `qwb_*` recorded as the shipped, runtime-verified
  model rather than a proposal; the pre-work "not yet decided" list marked answered; stale test counts
  and the "no QDN call exists anywhere in the code" statement corrected; release candidate SHA
  recorded.
- Orchestration `PROJECT-REGISTRY.md` — `qortal/qwb-qortal-web-builders` registered with its canonical
  context (production publication pending).
- Orchestration `skills/README.md` index + the three promoted skills (below).

`python3 tools/validate_skills.py` → `Skills validation passed: 13 active skills indexed exactly once`.

## 5. Capability harvest

Result: **project-specific, no new or updated skill.**

- Promoted and made durable by this task (prepared by the Phase 4 runtime run, uncommitted until now):
  `skills/qortal/qdn-content-crud/SKILL.md`, `skills/qortal/registered-name-owner-mode/SKILL.md`,
  `skills/qortal/inline-owner-editing/SKILL.md` — all `verified-runtime`, last checked `2026-09-16`.
- The bootstrap baseline itself was deliberately **not** promoted: "this application's shipped seed
  content is replaced one entity at a time by its owner" is a product rule of QWB, not a reusable
  Qortal platform contract. Promoting it would create a generic "seed baseline" abstraction the
  library's own rules warn against.
- Nothing was promoted on the strength of unit tests alone.

## 6. Durable handoff / state transition

- Application branch pushed first, then the workspace documentation branch, then this orchestration
  branch — in the order `GIT-AND-HANDOFF.md` requires, with the exact application SHA recorded in
  `STATUS.json`.
- Pre-existing orchestration work that had never been committed is now durable in the same commit:
  the three skills, the `skills/README.md` index rows, the `PROJECT-REGISTRY.md` entry, and the two
  earlier QWB task records (`qwb-architecture-audit-20260915`, `qwb-phase-0-1-20260915`) whose
  `STATUS.json` recorded `handoff_sync = pending_authorization`. That field is updated with a dated
  note; no other historical content was rewritten.
- `handoff_sync = pushed` for this task once the branch is on the remote.

## 7. Residuals and honest limits

- Production publication not performed and not authorized here;
  `WEBSITE / Qortal Web Builders / default` remains the 2026-07-07 placeholder.
- The release candidate's build no longer equals the artifact validated in the Phase 4 owner-runtime
  run (see §3).
- Carried over unchanged from the Phase 4 report: the §14 step 6 failure half was not exercised;
  step 13's literal in-form refusal notice is unreachable in Hub 3.0.3.
- Carried over unchanged and owner-facing, not blocking: the unDraw illustration licence assumption
  and the white-on-gradient navbar contrast (2.10:1, identical to the currently published site).
- `git diff --check` over the workspace documentation commit reports trailing whitespace only inside
  captured evidence artefacts (terminal output, `git format-patch` output, saved DOM dumps). Those
  files are preserved verbatim on purpose; rewriting them would corrupt the evidence.

## Report saved

- `/home/iffi/VsCodec-Projects/Qortal/qortal-dev-workspace/docs/qwb-qortal-web-builders/implementations/2026-09-16-qwb-phase-4-checkpoint.md`
- Evidence: `…/implementations/2026-09-16-qwb-phase-4-checkpoint-evidence/`
