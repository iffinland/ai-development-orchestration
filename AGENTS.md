# Qortal / Qortium orchestration contract

Owner decision: 2026-09-13. Scope is exclusively Qortal and Qortium.
This directory owns shared development coordination and reusable capability
knowledge, not blockchain/platform implementation truth.

## Mandatory session start

Before a new or resumed task:

1. Read [WORKFLOW.md](WORKFLOW.md), resolve the project in
   [PROJECT-REGISTRY.md](PROJECT-REGISTRY.md), then read its platform session
   router and canonical project context.
2. Read your role under `roles/` and
   [GIT-AND-HANDOFF.md](GIT-AND-HANDOFF.md).
3. Search [skills/](skills/README.md) for capabilities relevant to the requested
   outcome. Load only matching skills; record their maturity and freshness.
4. Check [ENVIRONMENT.md](ENVIRONMENT.md) and perform its platform/reference
   freshness gate before platform-dependent design, implementation or
   validation.
5. Use [templates/TASK.md](templates/TASK.md) for one compact controller.

Do **not** start with a full platform audit when a relevant verified skill exists.
Do a bounded compatibility/delta check first. If the skill is stale or absent,
investigate from current authoritative source and working implementations.

## Authority separation

- Owner instructions decide product intent, scope and authorization.
- This contract owns cross-platform roles, handoff, branch/environment
  coordination and reusable capability lifecycle.
- Platform workspaces retain Workflow v2 execution, technical guides, project
  contexts and report-storage policies.
- Current checked-out authoritative source and observed runtime establish
  implemented platform behavior; skills summarize reusable evidence but never
  override fresher source/runtime.
- Application source and durable product documentation remain in their repos.
- Historical reports and donor/reference apps are evidence, never competing
  policy.

Never transfer a Qortal contract to Qortium, or the reverse, just because names
or request shapes are similar. Every skill declares its platform scope.

## Reuse-first engineering

For platform integration use this order:

```text
requirement
-> matching skill?
-> skill freshness/compatibility check
-> current proven donor/reference implementation
-> current platform source
-> smallest missing delta
-> runtime validation
-> capability harvest
```

A reusable finding must not remain trapped in one project's report when it can
prevent repeat work elsewhere. At substantial handoff run
[`capability-harvest`](skills/shared/capability-harvest/SKILL.md) and either
update/create a skill or explicitly record that the result was project-specific.

Do not create a giant universal abstraction merely because code can be shared.
Standardize stable shell/host primitives and verified capabilities. Keep
project-specific domain logic, publication protocols and branding local unless
multiple proven consumers justify promotion.

## Product/layout default

For new applications prefer the
[`functional-app-bootstrap`](skills/shared/app-bootstrap/SKILL.md): establish a
neutral functional shell and prove the important platform/runtime flows before
spending substantial implementation budget on final branding. This is a default,
not a ban on visual-first tasks when visual design is itself the requested
outcome.

## Evidence and safety

The former blanket Qortal “no SSH tunnel” policy is superseded. An explicitly
configured and verified tunnel may provide read-only node access. It does not
prove host/bridge/account behavior, replace real host validation, or authorize
server changes.

Preserve owner work. Do not reset, clean, automatically stash, remove duplicate
files, or relocate linked worktrees. Record unresolved conflicts and propose a
recoverable consolidation plan before destructive cleanup.

No commit, push, merge, tag, release, deploy, QDN publication, signing,
transaction, issue mutation or server change is authorized merely because an
agent has filesystem/network access. Exact authorization stays task-scoped.

These files are an implemented local coordination contract, not a running agent
service or automatically published GitHub standard. A chat without file access
must receive the exact published contract revision; never pretend an inaccessible
local path was read.
