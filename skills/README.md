# Reusable capability library

This directory is the canonical cross-project library of reusable development
capabilities for Qortal and Qortium. A skill is not generic advice and it is not
a project diary. It is a compact, reusable procedure or verified platform
contract that prevents agents from rediscovering the same integration on every
application.

## Why this exists

The orchestration workflow previously routed every substantial platform concern
back through source inspection and audit. That is safe but wasteful when the
same capability has already been proven. The new rule is:

```text
new requirement
-> search applicable skills first
-> verify skill freshness against current platform source/runtime
-> reuse when still valid
-> investigate only the missing or changed delta
-> validate the result
-> harvest reusable new knowledge back into the skill library
```

An audit should become a durable investment. A platform fact discovered for one
application must not remain trapped in that application's report when it is
reusable elsewhere.

## Platform boundary

Every skill declares one of:

- `qortal` — Qortal-specific contracts and references;
- `qortium` — Qortium-specific contracts and references;
- `shared` — workflow or application-engineering capability that does not assume
  one network's bridge/API semantics.

Never apply a Qortal skill to Qortium, or the reverse, merely because names and
APIs look similar. Qortal and Qortium source/runtime remain separate authority.

## Maturity

Every skill carries a maturity state:

- `candidate` — promising reusable pattern, but the complete contract has not
  yet passed our own required runtime validation;
- `verified-reference` — current authoritative source and one or more working
  implementations establish the contract, but our own target runtime has not
  yet proven it end to end;
- `verified-runtime` — required source checks and our own real runtime validation
  have passed;
- `stale` — an invalidation trigger fired or a compatibility check found drift;
- `retired` — intentionally superseded; retain only when historical context is
  useful.

A `candidate` can guide investigation but cannot replace validation. A
`verified-reference` can normally replace a full rediscovery audit with a
bounded compatibility check. A `verified-runtime` is the preferred reusable
path until its freshness gate fails.

## Required skill contents

Use [`_template/SKILL.md`](_template/SKILL.md). Each skill must state:

- platform and maturity;
- when to use it and when not to;
- authoritative source revisions and proven donor implementations;
- exact reusable contract/procedure;
- assumptions and invalidation triggers;
- compatibility/freshness check;
- required validation layers;
- known failure modes and non-goals;
- what evidence upgrades or downgrades maturity.

Do not copy large platform source files into this repository. Record the exact
repo, revision, source path, relevant contract and validation evidence.

## Skill selection

At task start, agents read only skills relevant to the outcome. Do not load the
whole library. The task controller records the selected skills and their
freshness result.

If no matching skill exists, investigate from current authoritative source and
working implementations. After validation, run the capability-harvest skill to
decide whether the result should become a new skill or update an existing one.

## Claude readiness

The canonical skill source is this `skills/` tree, not a Claude-only copy.
Current active agents remain ChatGPT, Codex and DeepSeek. `CLAUDE.md` is a thin
future adapter only. When Claude Code is actually enabled, add the minimum
version-current discovery adapter (for example `.claude/skills -> ../skills` if
that remains supported) rather than duplicating the skill contents.
