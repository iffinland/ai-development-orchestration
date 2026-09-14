# Adversarial audit — orchestration/qortal-skill-promotion-20260914

Executing agent: **DeepSeek**. Review type: adversarial self-audit of this task's own
documentation output (not an independent audit). Skills reviewed: the five Qortal skills touched by
this task plus the README index and the capability-harvest routing pointer.

## Findings

| # | Area | Finding | Action |
| --- | --- | --- | --- |
| 1 | Project-specific leakage | `saw_*` identifiers/UI appear in `cross-app-video-publishing`, `subwire-article-publishing` and `qdn-derived-index-coherence` **only** inside explicit "project-local, do not promote" clauses; no `saw_*` value is stated as a contract. | Pass — no change. |
| 2 | Unsupported generalization | `qtube_vid_`, the `_metadata` suffix, SubWire payload/prefix, Quitter namespace/salts and the bridge JSON parsing are all labelled community-app convention or dated revision rather than platform law. | Pass — no change. |
| 3 | Stale revision claim | The first draft set `Last checked: 2026-09-14` while every source/runtime observation is dated 2026-09-13; that would imply a fresh check that was not performed. | **Fixed:** all five skill headers and the README index now record `2026-09-13`. |
| 4 | Over-specific identifier claim | A draft sentence implied the `qtube_vid_<slug>_<id>` inner shape is part of the cross-app contract. | **Fixed:** the skill now states the shared rule is the family plus `_metadata` suffix, and marks the inner shape as Q-Tube's own convention. |
| 5 | Qortal/Qortium contamination | "Qortium" appears in Qortal skills only in `Do not use when` boundaries; the Qortium skills contain no Qortal app names (`qtube`/SubWire/Quitter) — checked by search. | Pass — no change. |
| 6 | Duplicate skill scope | The five skills cover distinct boundaries (video metadata, article document, announcement write, derived index, bridge transport). No near-duplicate overlaps an existing skill. | Pass — no change. |
| 7 | Executor attribution | `TASK.md`/`IMPLEMENTATION.md` name **DeepSeek** with environment evidence (`CODEX_HOME=/home/iffi/.codex-deepseek`, `model_provider=deepseek`) and explicitly state the Codex CLI is only the harness. Skill files carry no executor attribution (correct). | Pass — no change. |
| 8 | Undocumented runtime claims | Skill 1 and 2 were promoted to `verified-runtime`; the evidence is the accepted owner-runtime checkpoint and the live read-only validations, not a new test run. No new runtime test is claimed anywhere. | Pass — recorded in `IMPLEMENTATION.md`. |
| 9 | Pre-existing template drift | `qortium/qdn-resource-discovery`, `qortium/qdn-media-readiness` and `shared/app-bootstrap` do not carry the full canonical heading set (`Use when`/`Do not use when`/`Known failure modes`/…). | Out of scope for this task; recorded as a follow-up recommendation. |
| 10 | Evidence-link durability | Skill/report references are local absolute/relative workspace paths, not remote URLs. They resolve on this host; a remote reader would need the pushed workspace docs branch. | Residual risk; noted, not blocking. |
| 11 | No canonical skills validator | `AI-Orchestration` contains no orchestration/docs/skills validator script. | Residual gap; recommend adding a durable skills-tree validator (follow-up). |

## Checks executed

- Purpose-built structural/link check of the skills tree (frontmatter `name`/`description`,
  `Platform`/`Maturity`/`Last checked`, canonical headings for the five touched skills, and
  resolution of every relative Markdown link including README index links): **PASS**
  (9 skills; 9 README index links; exit 0).
- `git diff --check` on the staged set: **PASS**.
- Qortal workspace documentation/link validator (`qortal-dev-workspace/tools/validate-workspace.sh`):
  **PASS** with its 5 pre-existing human-review warnings, none introduced by this task.
- Leakage searches (`saw_` in Qortal skills; Qortium terms in Qortal skills; Qortal app names in
  Qortium skills; `2026-09-14` stale claims): as recorded above.

## Not verified

- No application source was changed, so no build/test/lint was run.
- No live node or host was contacted in this task; runtime claims are inherited from the accepted
  2026-09-13 checkpoint.
- The audit is a self-audit; it is not an independent review.
