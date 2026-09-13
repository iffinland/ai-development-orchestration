# Reusable development patterns observed in Qortal / Qortium

Date: 2026-09-13
Purpose: evidence for the orchestration/skills redesign. This is a research
snapshot, not a permanent platform contract.

## 1. Qortium app-fleet reuse is code-level, not merely visual

The public applications listed by `7r15` were compared across the QortiumDev
organization. Multiple apps share identical blob revisions for common shell
components. Examples observed on 2026-09-13:

- `AppIdentity.tsx` is byte-identical across qortium-apps, qortium-library,
  qortium-publish-manager, qortium-chain-explorer, qortium-group-manager,
  qortium-name-manager, qortium-profile-manager and qortium-curate.
- `ColorTokensContext.tsx` is byte-identical across the same group.
- `RatingControl.tsx` is identical across most of that group.
- theme-token files are also shared by a large subset.
- the stack is consistently React + TypeScript + Vite + MUI + Jotai, with
  `vite-plugin-singlefile` in the inspected app set.

The QDN/API modules are not identical across the apps. The available README
files also repeat the same Home display-settings and fork/naming contracts across
multiple apps. Conclusion: standardize shell/host primitives and proven
capabilities, not one universal business/API wrapper.

The wallet changelog additionally shows explicit separation between Qortium
`qdnRequest` and Qortal `qortalRequest` behavior inside one application. That is
another reason not to merge Qortal and Qortium contracts into one assumed API.

## 2. Qortium developers use persistent local agent knowledge

Public Qortium Home/Core PRs authored by QuickMythril repeatedly reference a
local `~/AGENTS/projects/...` knowledge tree for contracts, plans, reviews and
handoffs. Many PR descriptions are generated with Claude Code and show
cross-model review with Codex.

`QortiumDev/qortium-chat` gitignores `CLAUDE.md`, while its public audits refer
to that local file and document multi-agent Claude/Codex audit workflows. This
shows a separation between repository source and persistent local agent guidance.

`QortiumDev/qortium-paint` publicly commits a concrete `CLAUDE.md` containing
build/test commands, architecture boundaries, QDN publication behavior,
feature-gating and QAVS conventions. It explicitly says its bridge wrapper uses
the same pattern as sibling apps.

## 3. Qortal Hub has an explicit skills architecture

At `Qortal/Qortal-Hub` develop revision
`12a573b27246e8a626b24794830c6bc432d1b05d`:

- `CLAUDE.md` is a one-line adapter to `AGENTS.md`;
- `AGENTS.md` states that canonical skill definitions live under
  `.agents/skills/<name>/SKILL.md`;
- Claude discovery is provided through `.claude/` links rather than duplicate
  skill contents;
- the current `i18n` skill is loaded on demand and owns supporting scripts.

This directly supports an agent-neutral canonical skill source plus thin
agent-specific discovery adapters. Qortal also publishes
`Qortal/create-qortal-app`; at main revision
`ea9d720bb31fa42b777659aceccd69ad20393abb` its README describes a CLI that
fetches current predefined templates, so new Qortal apps should inspect the
current official scaffold before creating a base from memory.

## 4. Good reusable capability examples already exist inside apps

`QortiumDev/qortium-radio` at
`870daccb9cd408f175b732e24f56d98e1d63eeeb` records live-tested platform facts
inside application code:

- `LIST_QDN_RESOURCES` was the correct operation for all AUDIO resources from a
  known publisher in the tested scenario; search returned only 1 of 19;
- a fully available resource reports `READY` in the observed live node;
- playback should trigger missing data fetch and wait boundedly for readiness
  before resolving/using the media URL.

These facts should not remain trapped in one radio app. They are initial
Qortium skills in this package.

## 5. Qortal cross-app video interoperability is already intentional

At `Qortal/q-tube` main revision
`68c3ea706c4ab110ffa44a7f55f8e09bdf7e85ff`, the production video identifier
family is `qtube_vid_`; Q-Tube publishes/discovers metadata documents around
that namespace and points them to `VIDEO` resources.

At `Qortal/Subwire` master revision
`a933a6c44d60db19cd219408e36c747aebcce994`, the code deliberately reuses the
same Q-Tube video/playlist identifier prefixes and defines Q-Tube-compatible
video metadata/reference structures.

This is strong evidence that Shadow Archives should investigate and reuse the
existing interoperable convention rather than inventing a private video
namespace. The complete contract remains a candidate until our own cross-app
runtime test proves it.

## Resulting orchestration decision

The shared workflow now has four distinct layers:

```text
governance / roles
        +
project context
        +
reusable capability skills
        +
current authoritative platform source/runtime
```

Skills reduce repeat research; they never override current source/runtime when a
freshness check detects drift.
