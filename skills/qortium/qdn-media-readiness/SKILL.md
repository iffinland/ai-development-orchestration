---
name: qortium-qdn-media-readiness
description: Use when Qortium AUDIO/VIDEO playback must wait for QDN data to become locally ready, trigger network fetching when needed, and avoid opening a media URL before the resource is usable.
---

# Qortium QDN media readiness before playback

- Platform: `qortium`
- Maturity: `verified-reference`
- Last checked: `2026-09-13`
- Owner: shared capability library

## Use when

- A Qortium app must play `AUDIO` or `VIDEO` QDN content and cannot assume a
  resolvable URL means the local node has usable bytes.

## Do not use when

- The platform is Qortal; confirm that platform's bridge and readiness contract
  separately.
- The requirement is resource discovery rather than readiness after coordinates
  are known.

## Authoritative evidence

| Source | Revision | Evidence |
| --- | --- | --- |
| `QortiumDev/qortium-radio` | `870daccb9cd408f175b732e24f56d98e1d63eeeb` | `src/api/qdn.ts` checks resource status, treats `READY` as usable, nudges fetching with `FETCH_QDN_RESOURCE`, polls boundedly, and resolves the stream URL only for playback. The file states `READY` was confirmed against a live node. |
| `QortiumDev/qortium-home` | `155356cdd5f2f91353b387f88f8c591057fd6831` | Home QDN viewer/publishing code is the current host-side reference for QDN readiness/status behavior. |

## Reusable contract / procedure

1. Resolve the exact service/name/identifier.
2. Query the current resource-status action with build/readiness semantics.
3. If already `READY`, continue.
4. If a current terminal failure status is returned, fail explicitly.
5. Otherwise trigger a bounded fetch/read to make Core request missing data.
6. Poll with cancellation and a finite timeout; surface progress when useful.
7. Resolve/open the media URL only after readiness.

## Freshness and compatibility gate

Before reuse, compare current Qortium Home and Core readiness/status behavior
with the recorded references. Exercise one known non-ready resource through the
bounded fetch/poll path and record `compatible`, `needs-delta-audit`, or
`stale`. Do not hardcode the recorded terminal-status list forever.

## Validation

- Validate a known ready resource and a cold/non-ready resource against a real
  Qortium node; confirm playback URL resolution happens only after readiness.
- Keep cancellation and timeout coverage in local tests.

## Known failure modes

- Opening a URL before bytes are ready produces a playback failure that can be
  mistaken for a codec or player defect.
- Unbounded polling can continue after navigation or a terminal failure.

## Non-goals

- A universal QDN status vocabulary or Qortal readiness behavior.
- Resource discovery, publication, or media transcoding.

## Harvest / maturity update

Upgrade after our own Qortium media app passes an embedded Home + real QDN
cold-resource smoke using this procedure.
