---
name: qortal-cross-app-video-publishing
description: Use when a Qortal app must publish public video content so Q-Tube-compatible discovery can find it, especially when the same content must also be referenced by another app such as Subwire.
---

# Qortal cross-app video publishing

- Platform: `qortal`
- Maturity: `candidate`
- Last checked: `2026-09-13`
- Owner: shared capability library

## Purpose

This is the first concrete interoperability skill to complete during Shadow
Archives. The target outcome is one canonical publication flow whose video is
visible to Shadow Archives and discoverable by current Q-Tube-compatible
consumers, without app-specific duplicate media uploads when avoidable.

## Current source evidence

| Source | Revision | Evidence |
| --- | --- | --- |
| `Qortal/Qortal-Hub` `develop` | `12a573b27246e8a626b24794830c6bc432d1b05d` | current Qortal host/`qortalRequest` authority; repo itself uses `AGENTS.md` plus on-demand `.agents/skills/`. |
| `Qortal/q-tube` `main` | `68c3ea706c4ab110ffa44a7f55f8e09bdf7e85ff` | `QTUBE_VIDEO_BASE = "qtube_vid_"`; public video metadata uses `DOCUMENT`, metadata identifiers use the video identifier plus `_metadata`, metadata is tagged with `QTUBE_VIDEO_BASE`, and metadata points to the corresponding `VIDEO` resource. Home/search surfaces discover `DOCUMENT` resources by this identifier family. |
| `Qortal/Subwire` `master` | `a933a6c44d60db19cd219408e36c747aebcce994` | `src/constants/qdn.ts` intentionally reuses `qtube_vid_` / `qtube_playlist_`; its article/episode code defines Q-Tube-compatible video metadata/reference structures rather than inventing a completely separate public-video namespace. |

## What is already safe to reuse

- Q-Tube's production public-video identifier family starts with `qtube_vid_`.
- Q-Tube discovery treats the metadata document as the discoverable object.
- The public binary video is a `VIDEO` resource; the metadata document refers
  to that video coordinate.
- Subwire deliberately shares Q-Tube's public-video identifier convention for
  interoperability.

## What is NOT yet verified for Shadow Archives

Do not freeze these until the Shadow Archives delta-audit and runtime smoke:

- the complete current metadata schema and which fields are mandatory vs
  optional for Q-Tube rendering;
- exact title/description/category/tag behavior needed for every Q-Tube search
  surface;
- whether one metadata resource can satisfy both Q-Tube and Subwire discovery
  without a second app-specific pointer/index;
- edit/delete/tombstone semantics across all three apps;
- large-file publish path required by the current Hub/runtime;
- comments/likes/tips interoperability, which are separate capabilities.

## Shadow Archives completion workflow

1. Pin current Hub, Q-Tube and Subwire revisions.
2. Trace Q-Tube's actual publish object construction and every discovery/read
   path that consumes it; document the minimal canonical schema.
3. Trace Subwire's public-video ingestion/reference path and identify the shared
   subset plus any app-specific index/reference it requires.
4. Design Shadow Archives so the canonical media bytes are published once where
   technically possible; derived indexes/pointers must be rebuildable.
5. Publish one controlled test video through Shadow Archives.
6. Verify the exact live resource through Core/QDN.
7. Verify it appears/opens in Q-Tube.
8. Verify the intended Subwire discovery/reference path.
9. Verify Shadow Archives reload/edit behavior.
10. Update this skill with the proven schema, publication sequence, identifiers,
    search queries, edit semantics and test evidence; then promote maturity.

## Exit criterion for `verified-runtime`

A Shadow Archives-owned test publication is successfully discovered and opened
through all explicitly targeted current apps, with source revisions and exact
QDN coordinates recorded. Until then this skill is an investigation accelerator,
not permission to claim interoperability.
