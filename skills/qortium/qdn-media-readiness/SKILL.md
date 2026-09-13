---
name: qortium-qdn-media-readiness
description: Use when Qortium AUDIO/VIDEO playback must wait for QDN data to become locally ready, trigger network fetching when needed, and avoid opening a media URL before the resource is usable.
---

# Qortium QDN media readiness before playback

- Platform: `qortium`
- Maturity: `verified-reference`
- Last checked: `2026-09-13`
- Owner: shared capability library

## Working evidence

| Source | Revision | Evidence |
| --- | --- | --- |
| `QortiumDev/qortium-radio` | `870daccb9cd408f175b732e24f56d98e1d63eeeb` | `src/api/qdn.ts` checks resource status, treats `READY` as usable, nudges fetching with `FETCH_QDN_RESOURCE`, polls boundedly, and resolves the stream URL only for playback. The file states `READY` was confirmed against a live node. |
| `QortiumDev/qortium-home` | `155356cdd5f2f91353b387f88f8c591057fd6831` | Home QDN viewer/publishing code is the current host-side reference for QDN readiness/status behavior. |

## Reusable procedure

1. Resolve the exact service/name/identifier.
2. Query the current resource-status action with build/readiness semantics.
3. If already `READY`, continue.
4. If a current terminal failure status is returned, fail explicitly.
5. Otherwise trigger a bounded fetch/read to make Core request missing data.
6. Poll with cancellation and a finite timeout; surface progress when useful.
7. Resolve/open the media URL only after readiness.

Do not hardcode the recorded terminal-status list forever; re-check Home/Core
when their status contract changes.

## Why this is a skill

The correct behavior is not merely "get a QDN URL and play it". A URL can
resolve before the node has downloaded/built the media. Re-solving this through
playback failures in every radio/video app is unnecessary.

## Maturity upgrade

Upgrade after our own Qortium media app passes an embedded Home + real QDN
cold-resource smoke using this procedure.
