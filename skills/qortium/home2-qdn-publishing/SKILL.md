---
name: qortium-home2-qdn-publishing
description: Use when a Qortium app must publish to QDN through Qortium Home 2 (2.x/2.1) and the app must learn the source-token publishing contract instead of the refused Home 1.x inline/path publish shapes.
---

# Qortium Home 2 QDN publishing (source-token contract)

- Platform: `qortium`
- Maturity: `verified-runtime`
- Last checked: `2026-09-18`
- Owner: shared capability library

## Use when

- A Qortium app publishes QDN resources through the Home bridge and the runtime
  is Home 2 (`SHOW_ACTIONS` on `qdnRequest` advertises `STAGE_QDN_PUBLISH_SOURCE`).
- An app migrated from the Home 1.x contract (inline bytes, path fields,
  app-provided fee) fails publishing with a refusal before any approval prompt.
- An app must batch several resources under the minimum number of Home
  approvals, or must handle a signed-but-unconfirmed publish truthfully.

## Do not use when

- The platform is Qortal: `qortalRequest` has its own publishing, fee-pinning
  and encryption contract. Confirm that platform separately.
- The task is resource discovery, readiness, or playback rather than
  publication.
- The runtime is Home 1.x: the token actions do not exist there. Do not
  downgrade a Home 2 app to the legacy shape; fail closed and tell the user.

## Authoritative evidence

| Source | Revision | Paths / contract proved |
| --- | --- | --- |
| `QortiumDev/qortium-home` | tag `v2.1.0-beta.11` = `5129317fca9af8f6c19f7f72d34f6948dabf0f34` | `docs/QDN_PUBLIC_PUBLISHING.md`, `docs/BRIDGE_ACTIONS.md` (sections for `STAGE_QDN_PUBLISH_SOURCE` and `PUBLISH_MULTIPLE_QDN_RESOURCES`), `docs/HOME_2_1_BETA_TESTING.md` |
| `QortiumDev/qortium-home` | same revision | `electron/home-v2-app-actions.ts` (advertised action set), `electron/home-v2-app-bridge.ts` (approval, binding, signing, broadcast, result), `electron/home-v2-publish-blob-source.ts` (`HOME_V2_PUBLISH_BLOB_MAX_BYTES = 25 * 1024 * 1024`), `electron/home-v2-publish-source-selection.ts`, `electron/qdn-views.ts` |
| `QortiumDev/qortium-radio` | `870daccb` | prior Qortium-native app that already published through Home-issued tokens |

Runtime evidence for this revision (recorded by the NodeFM resumption pass,
2026-09-17, real Home 2.1.0-beta.11 desktop on a real configured Qortium testnet
node, `qortium-1.8.0-05cbc08`, route `custom-authenticated`, `adminTrusted: true`):

- `SHOW_ACTIONS` on `qdnRequest` returned 162 actions including
  `STAGE_QDN_PUBLISH_SOURCE`, `SELECT_QDN_PUBLISH_SOURCE`,
  `PREVIEW_QDN_PUBLISH_SOURCE`, `PUBLISH_QDN_RESOURCE`,
  `PUBLISH_MULTIPLE_QDN_RESOURCES`, `UNLOCK_SELECTED_ACCOUNT`.
- `GET_HOST_INFO` reported `hostVersion: 2.1.0-beta.11`, `platformVersion: 2.1`,
  `network: qortium`, `protocol: qdnRequest`.
- One real `STAGE_QDN_PUBLISH_SOURCE` call with
  `{ bytesBase64, fileName, mimeType }` returned a Home-issued token
  (36-character opaque string, `kind: 'blob'`, exact `size`, echoed `mimeType`)
  in 14 ms with **0 approval prompts**, matching the documented behaviour that
  staging grants nothing.
- The same runtime refused, before any bridge request, every legacy
  input an app might still hold (`data64`, `base64`, `data`, `filename`, `path`,
  `fee`, `source`, `uri`).
- The same runtime refused, before any bridge request, every legacy
  input an app might still hold (`data64`, `base64`, `data`, `filename`, `path`,
  `fee`, `source`, `uri`), and an independent wire tap of one full app session
  (757 bridge entries, 4 publish calls, 5 stage calls) recorded zero refused
  fields on any `PUBLISH_*` request: publishes carried only
  `action`/`service`/`name`/`sourceToken`/`identifier`/`title`/`description`
  while `fileName`/`mimeType`/`bytesBase64` appeared only on
  `STAGE_QDN_PUBLISH_SOURCE`.

Runtime publish + read-back evidence for this revision, recorded by the NodeFM
Home 2.1 write matrix (2026-09-17, Home 2.1.0-beta.11 desktop, account
`iffi_vaba_mees`, real Qortium testnet node `qortium-1.8.0-05cbc08` at
`http://127.0.0.1:24891`, route `custom` authenticated trusted-node):

- `PUBLISH_QDN_RESOURCE` (single) and `PUBLISH_MULTIPLE_QDN_RESOURCES`
  (2-resource batch) both reached `accepted: true` with real Home approval
  prompts, 1 approval per request, scope `single-request` ("Allow once").
- Observed costs per real publish, all through the same runtime: one approved
  single publish of a small JSON landed in ~14 s; a two-resource AUDIO+IMAGE
  batch (49 KB + 342 KB) took ~90 s; one JSON publish failed after Home's own
  3-minute proof-of-work budget (`Proof-of-work did not finish within three
  minutes.`) and succeeded unchanged on retry.
- Read-back: AUDIO render returned HTTP 200 `audio/mpeg`, 49 015 bytes, SHA-256
  identical to the staged source; IMAGE render returned HTTP 200 `image/png`,
  342 068 bytes, SHA-256 identical to the digest Home displayed in its own
  approval dialog; the JSON resources read back with `title`/`artist`
  metadata byte-identical, including non-ASCII text.
- Approval dialogs are the app's only user-visible cost: batching 2 resources
  under one `PUBLISH_MULTIPLE_QDN_RESOURCES` request still produced exactly one
  dialog per request, and staging (`STAGE_QDN_PUBLISH_SOURCE`) stayed
  prompt-free.

Unicode source filenames (Home issue #330, fixed by PR #337, merge
`11f5096740c97cc076ec867b6d8b833301616f5e`, contained in `v2.1.0-beta.11`):

- Home now accepts and stages a source filename with Estonian/Finnish
  (`ä ö õ ü`), Cyrillic, spaces and an em dash; the staged descriptor echoed
  the filename byte-for-byte and staging stayed prompt-free.
- `SELECT_QDN_PUBLISH_SOURCE` also returned the exact non-ASCII basename.
- The residual failure observed in that session was **not** Home: the
  authenticated node's Core rejected the upload with
  `HTTP 500 {"error":5,"message":"Filename is invalid"}` because the node JVM
  ran with `sun.jnu.encoding=ANSI_X3.4-1968` (`LANG` unset), so
  `Paths.get(fileName)` threw for any non-ASCII name. The same bytes with an
  ASCII filename published and read back byte-exact on the same runtime. Treat
  a non-ASCII filename failure as a **serving-node locale** defect and check the
  node's `sun.jnu.encoding`/`LANG` before blaming the Home publish contract.

## Reusable contract / procedure

1. **Feature-detect, then fail closed.** Call `SHOW_ACTIONS` and require
   `STAGE_QDN_PUBLISH_SOURCE` (app-held bytes) and/or
   `SELECT_QDN_PUBLISH_SOURCE` (user-chosen file or folder). If the action is
   absent, raise a truthful "this runtime does not support Home 2 publishing"
   error. Never fall back to the Home 1.x inline contract: Home 2 refuses it.
2. **Acquire exactly one source per item.**
   - User-chosen file/folder: `SELECT_QDN_PUBLISH_SOURCE` (optionally
     `{ kind: 'directory' }`, desktop Qortium only). Home opens the picker and
     returns `{ canceled, sourceToken, fileName, kind, mimeType?, size }`; no
     native path is ever returned.
   - Bytes the app already holds: `STAGE_QDN_PUBLISH_SOURCE` with
     `{ bytesBase64, fileName, mimeType? }`, at most 25 MiB of decoded bytes.
   Either way the result is an opaque, Home-issued `sourceToken`.
3. **Publish token-only.** `PUBLISH_QDN_RESOURCE` carries the resource
   coordinate (`service` required, `name` required, `identifier` optional) plus
   `sourceToken`; Qortium additionally accepts the mutable metadata
   `title`, `description`, `category`, `tags`. Send nothing else.
4. **Never send refused fields.** Inline or path-shaped source encodings are
   refused by Home 2: `data64`, `data`, `dataBase64`, `base64`, `bytesBase64`
   (on a publish request), `filename`/`fileName`, `filePath`/`path`, `mimeType`,
   `source`, `uri`, plus any app-provided `fee`. Home derives the fee from the
   selected chain; naming one is refused on both chains. Reject these at the
   app's own wire boundary too, so a refused encoding cannot be reintroduced by
   a later refactor.
5. **Batch with `PUBLISH_MULTIPLE_QDN_RESOURCES` when one approval should cover
   several resources.** Each item carries the full single-publish contract and
   its own **distinct** `sourceToken`; at most **ten** items per request, and
   the aggregate decoded bytes are bounded (25 MiB for staged bytes). A single
   token reused across items is refused — 1.x released tokens only after the
   loop, so one approval could otherwise back several transactions. Chunk
   larger logical writes; there is no larger batch.
6. **Treat the result as per-item, not atomic.** The result is
   `{ accepted, published: [...], failures: [...] }`; execution is serial and
   item-by-item. An item that Home signed but could not confirm as broadcast
   lands in `failures` with `outcome: 'unknown'` (plus its
   `transactionSignature`) — reconcile it by signature and never re-publish it
   blindly. One unreconciled publish blocks that app's next batch for the
   account, so an unresolved item must be surfaced to the user, not swallowed.
7. **Keep token scope in mind.** A token is bound to the requesting app, tab,
   selected account, invoked network, node route and route revision, and expires
   (30 minutes since issue *and* since last use). A picker/stage call does not
   grant permission: the publish still runs Home's normal per-request approval,
   and the account must be unlocked for that signature. Re-acquire the source if
   the account, tab, route revision or route changed — a restored/reloaded tab
   invalidates the binding even when the token is still inside its TTL.
   Home releases a token once its publish settles (`accepted` or
   `outcome: 'unknown'`), so a token is single-use per item: a retry needs a
   fresh stage/select.
   When the selected account is locked, the runtime's unlock action opens Home's
   own password dialog and Home allows roughly **60 seconds** for it; if the
   owner does not finish in that window Home answers `Account access was
   denied.` and the app must treat it as a cancelled write (nothing published),
   not as a contract error.
8. **Verify what landed.** Home attests the bytes it signs; the app should still
   read the resource back (`GET_QDN_RESOURCE_STATUS` for readiness,
   `FETCH_QDN_RESOURCE`/metadata for content or coordinate) before showing the
   write as confirmed. A `sourceToken` is not evidence of publication.
9. **Legacy interop, informational only.** Home 2 also accepts the narrow
   `{ base64, filename }` request shape used by already-published Home 1.x apps
   and stages it through the same store. New code must use the explicit
   staging/selection path; the adapter exists so old deployed bundles do not
   break mid-transition, not as an alternative contract.
10. **Staging and publication are two separate phases.** `SHOW_ACTIONS` →
    stage/select source → inspect the returned descriptor/token → then publish
    → then verify. Staging is prompt-free and grants nothing; publish is what
    prompts, unlocks, signs and can fail. Do not model them as one request, do
    not treat a successful token as a successful publication, and do not
    release the app's local source state until the publish phase settles.
11. **APP release archives must match the owner's actual release workflow.**
    Do not assume the owner publishes a directory. In Home 2.1 a folder source
    is uploaded with `isZip=true` and unpacks so `/render/<APP>/...` serves the
    entry HTML and assets, while an inline/blob ZIP publishes over the
    authenticated trusted-node route whose publisher hardcodes
    `unpackZip=false`, shipping an opaque archive whose asset paths 404.
    Confirm how the owner actually builds and releases the APP (directory
    picker, release ZIP, or another mechanism) and reproduce that path before
    designing release tooling or telling the owner a build is deployed.
12. **Release-gate verification matches the served bundle to the built
    artifact.** Hash the JS/CSS the app frame actually serves and compare it
    with the locally built release artifact (`dist/assets/...`). `accepted:
    true`, a visible QDN resource, or a green app load does not prove which
    bundle was served; a mismatched hash means the release is not verified.

## Freshness and compatibility gate

Before reuse:

1. resolve the Home revision actually running (`GET_HOST_INFO.hostVersion`) and
   compare it with this skill's recorded revisions;
2. inspect `electron/home-v2-app-actions.ts` (advertised actions) and
   `electron/home-v2-publish-blob-source.ts` (bounds) for changes;
3. run the smallest possible contract smoke on a real Home instance: one
   `SHOW_ACTIONS`, one `STAGE_QDN_PUBLISH_SOURCE`, and — only with authorization
   — one publish plus read-back;
4. mark the result `compatible`, `needs-delta-audit`, or `stale`.

A green unit suite in the app never proves this host contract.

## Validation

- Static/automated: the app's own boundary tests must assert token-only publish
  payloads and refusal of legacy fields.
- Host runtime (required): run the real publish path in a real Home 2 runtime and
  record the observed approval-prompt count and contents, the returned
  `published`/`failures`/`outcome` values, and a QDN read-back of the written
  resources.
- Batch: prove chunking above ten items and that each item used a distinct
  token.
- Failure handling: prove that `outcome: 'unknown'` is surfaced and not retried.
- Release gate: publish through the owner's actual APP release workflow, then
  hash the bundle served from `/render/<APP>/...` and compare it with the local
  release artifact. Inspect the served index for the exact asset filenames.

## Known failure modes

- Publishing from a Home 1.x-shaped payload (inline bytes, `filename`,
  `mimeType`, app-provided `fee`): Home 2 refuses before any prompt, so the
  app's "publish" silently fails with no approval ever shown.
- Assuming `SELECT_QDN_PUBLISH_SOURCE`/`STAGE_QDN_PUBLISH_SOURCE` needs or grants
  approval: staging is prompt-free, and the later publish still prompts.
- Reusing one token for several batch items, or assuming a batch is atomic.
- Retrying an item whose outcome is unknown, which can double-publish.
- Rendering the app from a local dev server inside embedded Home: Home 2 only
  renders approved node `/render/...` URLs or its own managed archive cache, so
  an unpublished local dev build cannot be exercised inside Home.
- Treating a locked account as a broken publish path; the failure is an unlock
  requirement, not a contract change. Home's unlock dialog is timeboxed
  (~60 s), so an app that opens it and waits silently will see
  `Account access was denied.` even when the owner intended to unlock.
- Home enforces its own proof-of-work deadline (~3 minutes) per publish. A
  resource that exceeds it fails with `Proof-of-work did not finish within
  three minutes.` and must be retried explicitly; the failure is not evidence
  that the token or the contract is wrong.
- Reading a just-published media resource can return a transient HTTP 503 from
  the trusted node's render route even though `GET_QDN_RESOURCE_STATUS` already
  reports `DOWNLOADED`/`READY`. Poll the render URL a few times before
  declaring the bytes unreadable.
- Very small media artifacts can be refused by Home's attestation size guard
  (`QDN attestation artifact exceeded the approved size.`) while the same
  resource at a few hundred KB publishes normally; observed once for a 1 773 B
  PNG on Qortium. Re-test the class before assuming the app's payload is wrong.
- Treating staging and publishing as one phase: reporting a publish as done once
  a `sourceToken` exists, or surfacing a stage failure as a publish failure.
- Publishing an APP as an inline/blob ZIP when the owner's release workflow and
  the renderer expect an unpacked directory source: the resource exists and the
  publish is `accepted`, but every `/render/...` asset path 404s because the
  archive shipped opaque.
- Declaring a release deployed from a successful publish without comparing the
  served bundle hash with the local built artifact.

## Non-goals

- The Qortal (`qortalRequest`) publishing, fee, or encryption contract.
- A specific application's resource coordinates, identifiers, authority model,
  or business rules.
- Host UI design, approval-prompt wording, or a portable source-token
  implementation.

## Harvest / maturity update

Promoted to `verified-runtime` on 2026-09-17 by the NodeFM Home 2.1 write matrix,
which recorded on a real Home 2 runtime:

- `PUBLISH_QDN_RESOURCE` and `PUBLISH_MULTIPLE_QDN_RESOURCES` reaching
  `accepted: true` with real, counted approval prompts (1 per request, "Allow
  once");
- read-back of every written coordinate and of the AUDIO/IMAGE bytes from
  Core/QDN with matching SHA-256;
- a documented `outcome: 'unknown'`-class hazard (Home's 3-minute proof-of-work
  deadline, and a same-identifier retry after a partial write) instead of an
  induced stuck batch.

Downgrade to `needs-delta-audit` if `electron/home-v2-app-actions.ts`,
`electron/home-v2-publish-source-tokens.ts` (TTL/binding/bounds),
`electron/home-v2-desktop-publish-source.ts`, or the attestation deadline change.

The 2026-09-18 NodeFM final-audit pass added the phase and release-gate rules:
staging grants nothing and is not publication, the owner's real APP release path
must be reproduced rather than assumed, and release closure requires the served
bundle hash to equal the local release artifact.

If Home's action set, token store bounds, or batch semantics change, downgrade to
`needs-delta-audit` and re-run the gate above.
