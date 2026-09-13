---
name: <stable-skill-name>
description: <what task should cause an agent to load this skill>
---

# <Skill title>

- Platform: `<qortal|qortium|shared>`
- Maturity: `<candidate|verified-reference|verified-runtime|stale|retired>`
- Last checked: `<YYYY-MM-DD>`
- Owner: shared capability library

## Use when

- <trigger>

## Do not use when

- <boundary>

## Authoritative evidence

| Source | Revision | Paths / contract proved |
| --- | --- | --- |
| `<repo>` | `<sha>` | `<paths and exact behavior>` |

Record runtime evidence separately when maturity is `verified-runtime`.

## Reusable contract / procedure

1. <step>
2. <step>

## Freshness and compatibility gate

Before reuse:

1. compare current authoritative revision with the recorded revision;
2. inspect changes touching the relevant contract boundary;
3. run the smallest contract check that can prove compatibility;
4. mark the task's result as `compatible`, `needs-delta-audit`, or `stale`.

Do not redo a full audit if the relevant contract is unchanged.

## Validation

- <static/automated>
- <local runtime>
- <host/bridge/live node>
- <cross-app/runtime when applicable>

## Known failure modes

- <failure and response>

## Non-goals

- <not provided by this skill>

## Harvest / maturity update

State exactly what evidence is required to upgrade or downgrade this skill.
