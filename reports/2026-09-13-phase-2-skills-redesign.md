# Phase 2 — reusable capability / skills redesign

Date: 2026-09-13
Scope: local `AI-Orchestration` documentation package only
External mutations: none

## Outcome

The original orchestration bootstrap had strong role, environment, Git/handoff
and platform-source-of-truth rules but no first-class reusable capability layer.
That gap meant a new application could still repeat expensive audits of platform
behavior that had already been established elsewhere.

This redesign adds a canonical `skills/` library and changes task execution from
"audit first" to "reuse first, then investigate the delta" without weakening the
source/runtime freshness requirements.

## External patterns inspected

Read-only GitHub inspection included:

- `7r15`'s public Qortium application fleet;
- `QortiumDev` Home/Core/apps, including qortium-radio and qortium-paint;
- QuickMythril-authored Qortium PRs and their references to persistent local
  `~/AGENTS/projects/...` plans/reviews/contracts;
- `Qortal/Qortal-Hub`, including its current `AGENTS.md`, `CLAUDE.md` and
  `.agents/skills/i18n/SKILL.md` architecture;
- current `Qortal/q-tube` and `Qortal/Subwire` video/QDN conventions.

Detailed evidence is in
`research/2026-09-13-reusable-development-patterns.md`.

## Key findings

1. The 7r15 Qortium apps share actual shell/theme/component code across many
   repositories, not just a similar appearance. Their app-specific QDN/API
   modules still diverge. We therefore standardize stable shell/host primitives,
   not one universal application wrapper.
2. QuickMythril's public work shows a persistent local agent-knowledge layer plus
   Claude/Codex cross-review and real runtime evidence.
3. Qortal Hub currently uses the exact architectural pattern we wanted:
   unconditional agent guidance plus on-demand skills, with canonical skill
   content separated from Claude's discovery adapter.
4. Useful reusable QDN facts are currently trapped inside app source. The
   qortium-radio list-vs-search and READY/fetch-before-playback findings are
   concrete examples converted into initial skills here.
5. Q-Tube and Subwire intentionally share the `qtube_vid_` public-video
   convention. A Shadow Archives cross-app publication skill is therefore
   created as `candidate`, not yet `verified-runtime`.

## Architecture after the change

```text
AGENTS / WORKFLOW / roles        governance and orchestration
PROJECT-REGISTRY + platform ctx  project truth and routing
skills/                          reusable capability knowledge
current platform source/runtime  final implementation authority
```

Skills use maturity states:

- candidate
- verified-reference
- verified-runtime
- stale
- retired

Every skill records its platform scope and freshness/invalidation gate.

## Initial skills

- `skills/shared/capability-harvest/SKILL.md`
- `skills/shared/app-bootstrap/SKILL.md`
- `skills/qortium/qdn-resource-discovery/SKILL.md`
- `skills/qortium/qdn-media-readiness/SKILL.md`
- `skills/qortal/cross-app-video-publishing/SKILL.md`

The Qortal video skill is intentionally incomplete. Shadow Archives must finish
its metadata/discovery/edit/runtime contract and only then promote it.

## Claude decision

Claude is **not** added as a current required role because the owner does not yet
have a Claude subscription. Adding a full Claude-specific configuration now
would create unused configuration that can drift.

A thin root `CLAUDE.md` is included now because it is low-maintenance and
captures the desired architecture: Claude will later consume the same AGENTS,
WORKFLOW and canonical skills. No `.claude/skills` copy and no `roles/CLAUDE.md`
are created yet. When Claude is actually enabled, add only the discovery adapter
required by the then-current Claude Code version.

## Base layout decision

The workflow now explicitly supports a neutral functional app shell first:
platform bootstrap, auth, routing, QDN primitives, cache/error/loading,
responsive/accessibility and validation. Final product branding/layout is a
later project-specific layer after important runtime flows work, unless visual
design is itself the task.

This preserves the owner's preference for visually distinct applications while
still capturing the productivity benefit visible in the 7r15 app fleet.

## Active agents after this change

No operational agent is replaced by this package update:

- ChatGPT: architecture/controller/review
- Codex: local orchestration/audit/escalation
- DeepSeek: primary cost-efficient implementation

Claude readiness exists but is inactive.

## Shadow Archives next use

When the paused local task resumes, do not restart its cross-app video research
from zero. Load `skills/qortal/cross-app-video-publishing/SKILL.md`, refresh the
three referenced revisions, perform only the missing schema/discovery delta,
then publish one controlled test resource and validate Q-Tube + Subwire + Shadow
Archives. Promote the skill only after that runtime evidence passes.
