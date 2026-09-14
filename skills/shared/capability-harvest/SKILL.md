---
name: capability-harvest
description: Run after any Qortal or Qortium task that discovered, corrected, or validated a reusable platform integration, workflow, app-shell primitive, API/bridge contract, publication pattern, or release procedure.
---

# Capability harvest

- Platform: `shared`
- Maturity: `verified-runtime`
- Last checked: `2026-09-13`
- Owner: shared capability library

## Use when

Run at the end of every substantial investigation, implementation or runtime
validation before handoff.

## Do not use when

- The result is only product-specific branding, copy, or business logic with no
  reusable platform or workflow boundary.
- The evidence is guessed, stale, credential-bearing, or otherwise unsuitable
  for the shared library.

## Authoritative evidence

| Source | Revision | Paths / contract proved |
| --- | --- | --- |
| This orchestration repository | current checked-out revision | [`AGENTS.md`](../../../AGENTS.md) and [`WORKFLOW.md`](../../../WORKFLOW.md) require reuse-first capability capture after substantial work. |

## Decision test

Ask in this order:

1. Would another Qortal/Qortium application plausibly need this capability?
2. Is the finding independent of this project's product-specific business
   logic or branding?
3. Is there evidence stronger than agent memory (current source, working donor,
   tests, live/runtime observation)?
4. Can the reusable boundary be stated without copying the entire donor app?

If 1-3 are yes, create or update a skill. If evidence is incomplete, create a
`candidate` rather than pretending the contract is verified.

## Reusable contract / procedure

## Promotion rules

Promote:

- bridge request/response contracts;
- QDN service/identifier/discovery interoperability;
- source-token or file publication procedures;
- account/name/owner capability handling;
- media readiness/fetch/playback procedures;
- reusable validation/smoke harnesses;
- app-bootstrap primitives and host display contracts;
- deterministic build/version/publish procedures;
- recurring failure patterns with a proven diagnosis method.

Do not promote:

- one app's business rules;
- branding, page copy or product-specific layout;
- a guessed fix that has not passed the required evidence;
- stale historical behavior without an explicit historical label;
- credentials, private infrastructure or user data.

## Procedure

1. Search the existing library for an overlapping skill, using the routing index
   in [skills/README.md](../../README.md#skill-index).
2. Prefer updating one canonical skill over adding a near-duplicate.
3. Record source revisions and exact paths that prove the reusable contract.
4. State invalidation triggers and the smallest future compatibility check.
5. Preserve project-specific detail in the project report, not the global
   skill.
6. Record the skill path and maturity change in the handoff.

## Freshness and compatibility gate

Before applying this procedure, read the current orchestration contract and the
selected skill's own freshness gate. If authority, source, or runtime evidence
has drifted, preserve that uncertainty as `candidate` or `stale` rather than
promoting it from memory.

## Validation

- Confirm the proposed skill has current source/runtime or donor evidence,
  explicit platform scope, maturity, invalidation trigger, and a bounded future
  compatibility check.
- Run the skills validator before handoff; a promotion is incomplete until its
  structural routing and metadata checks pass.

## Known failure modes

- Promoting an app-specific implementation as a universal platform contract.
- Calling unverified source inspection or mocked tests `verified-runtime`.
- Omitting freshness rules, leaving later agents to reuse stale assumptions.

## Non-goals

- Replacing platform source/runtime authority, creating product documentation,
  or publishing an application.

## Harvest / maturity update

The handoff contains one of:

- `skill harvest: none — project-specific only`, or
- exact skill paths created/updated plus their maturity and evidence.
