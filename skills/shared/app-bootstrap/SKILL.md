---
name: functional-app-bootstrap
description: Use when starting a new Qortal or Qortium application, or when a prototype needs a maintainable functional shell before product-specific visual design.
---

# Functional app bootstrap before branding

- Platform: `shared`
- Maturity: `verified-reference`
- Last checked: `2026-09-13`
- Owner: shared capability library

## Use when

- Starting a Qortal or Qortium application, or replacing a prototype with a
  maintainable functional shell before final product-specific branding.

## Do not use when

- The requested outcome is explicitly visual-first and visual design itself is
  the acceptance surface.
- A project-specific publication or domain workflow is being mistaken for a
  reusable application shell.

## Authoritative evidence

The evidence below records a dated comparison and current official scaffold
reference; re-check both before treating either as current authority.

## Reusable contract / procedure

Build a neutral, production-capable functional shell first; apply the app's
final visual identity only after the important platform and runtime flows work.
This is not a rule that all owner apps must look alike.

The shell may standardize, where applicable:

- TypeScript/build/test baseline;
- platform bootstrap and host/bridge feature detection;
- selected account/auth loading/error states;
- routing/base-path handling;
- QDN client primitives and response normalization;
- cache/error-boundary/loading primitives;
- responsive/accessibility defaults;
- host theme/display-settings integration;
- common build verification and artifact checks.

It must not freeze:

- brand colors, typography or visual language;
- homepage/content layout;
- navigation appearance when product needs differ;
- product-specific domain state or publication protocol.

A 2026-09-13 comparison of the public QortiumDev application fleet found real
code-level reuse, not merely visual similarity: multiple 7r15-maintained apps
share identical `AppIdentity.tsx`, `RatingControl.tsx`,
`ColorTokensContext.tsx`, and theme-token blobs and use a highly consistent
React/TypeScript/Vite/MUI/Jotai/single-file stack. Their QDN/API modules differ
by application, which is why this skill standardizes the shell and platform
primitives rather than one universal business wrapper.

Qortal's current Hub also separates unconditional agent guidance (`AGENTS.md` /
`CLAUDE.md`) from on-demand skills, reinforcing the same principle: load stable
shared capability where it helps, keep domain-specific implementation local.
Qortal also currently publishes `Qortal/create-qortal-app` (main revision
`ea9d720bb31fa42b777659aceccd69ad20393abb`) as an official template-fetching
CLI. For a new Qortal app, inspect its current templates before inventing a
scaffold from scratch.

1. Run the platform's session router and current reference freshness gate.
2. Search for a current official scaffold/framework and proven applications.
3. Reuse a verified shell capability instead of copying an entire donor app.
4. Make the first UI intentionally neutral but fully usable.
5. Implement and validate the platform/data/runtime path.
6. Only after the required runtime smoke passes, begin project-specific visual
   design unless visual design itself is the task's primary outcome.

## Freshness and compatibility gate

Do not pin a permanent framework choice here. Before each new app, verify the
current Qortal/Qortium official scaffold/framework and host contracts. Updating
the bootstrap should be a bounded delta check, not a redesign from memory.

## Validation

The functional shell is not complete until the app's actual host runtime path
works. Browser/Vite preview and a production build are necessary but not proof
of embedded Hub/Home behavior.

## Known failure modes

- Copying a donor application's business logic or visual identity together with
  the shell creates false reuse and blocks product-specific design.
- Treating a local preview as proof of embedded Hub/Home behavior leaves the
  critical runtime boundary unvalidated.

## Non-goals

- A mandatory visual system, product layout, or universal QDN business layer.

## Harvest / maturity update

Upgrade only after a target application proves the selected shell in its own
embedded host runtime; mark stale when the official scaffold or host contract
changes materially.
