# Qortal / Qortium development coordination

This repository is the shared orchestration and reusable-capability layer for
AI-assisted Qortal and Qortium development. Application source stays in its own
repository; platform contracts remain authoritative in the Qortal/Qortium
workspaces and current platform source/runtime.

Start with [AGENTS.md](AGENTS.md).

## Core model

```text
owner outcome
-> shared orchestration contract
-> project context
-> relevant reusable skills
-> current platform source/runtime freshness check
-> bounded implementation
-> layered validation
-> capability harvest
-> durable handoff
```

The important change from the original bootstrap is the
[reusable capability library](skills/README.md). Agents must search it before
redoing platform research. New reusable findings are harvested back into it so
future applications pay only for the changed/project-specific delta.

## Main documents

- [Shared contract](AGENTS.md)
- [Workflow](WORKFLOW.md)
- [Reusable capability library](skills/README.md)
- [Project registry](PROJECT-REGISTRY.md)
- [Environment and reference freshness](ENVIRONMENT.md)
- [Git and durable handoff](GIT-AND-HANDOFF.md)
- [Agent roles](roles/)
- [Task and handoff templates](templates/)
- [2026-09-13 external-pattern research](research/2026-09-13-reusable-development-patterns.md)
- [Historical Phase 1 audit](reports/2026-09-13-phase-1-audit.md)
- [Phase 2 skills redesign report](reports/2026-09-13-phase-2-skills-redesign.md)

## Active agent set

Current operating set:

```text
ChatGPT -> architecture / controller / review
Codex    -> local orchestration / bounded independent audit / escalation
DeepSeek -> primary cost-efficient local implementation
```

Claude is not currently required. [CLAUDE.md](CLAUDE.md) is intentionally only
a thin future adapter so Claude Code can later join the same canonical rules and
skills without creating a second knowledge base.

## UI/product bootstrap decision

New applications may start from a neutral functional shell for platform,
routing, auth, QDN, cache, error/loading, accessibility and validation
primitives. Final branding/layout remains project-specific and is normally
applied after the important runtime flows work. This does **not** standardize all
owner applications into one visual design.

Local branch in the supplied package: `agent/orchestration/bootstrap`; no commit
or remote publication is implied by this package.
