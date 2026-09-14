---
name: qortal-bridge-fetch-qdn-resource-normalization
description: Use when a Qortal dApp reads QDN resources through the injected host bridge and FETCH_QDN_RESOURCE may return a JSON-parsed object or array instead of raw text, so reads must be normalized and validated at the transport boundary.
---

# Qortal bridge FETCH_QDN_RESOURCE normalization

- Platform: `qortal`
- Maturity: `verified-runtime`
- Last checked: `2026-09-13`
- Owner: shared capability library

## Use when

- A Qortal dApp reads QDN resources through the host-injected bridge
  (`qortalRequest`/`FETCH_QDN_RESOURCE`) rather than a same-origin REST reader.
- A read path expects text but receives a parsed object/array, or a read path
  fails with an error such as `FETCH_QDN_RESOURCE did not return text`.
- You are designing the app's single bridge/transport boundary and need the
  verified current response-shape contract and normalization rule.

## Do not use when

- The transport is a same-origin REST call to a node API; those return raw text
  and are not affected by this bridge parsing behavior.
- The platform is Qortium. This is a verified Qortal bridge behavior; do not
  apply it to Qortium merely because the action name is similar.
- You want one universal response contract for **all** bridge actions. Only
  `FETCH_QDN_RESOURCE` has this JSON-parsing behavior; other actions return
  different shapes.
- You need the media-availability/URL contract (see the derived-index and
  video/SubWire skills).

## Authoritative evidence

| Source | Revision | Paths / contract proved |
| --- | --- | --- |
| `Qortal/qortal` (Core 6.1.9) `master` | `108bf191d42d710ec617f535af30cfd82fc03c87` | `src/main/resources/q-apps/q-apps.js` `handleResponse()` does `JSON.parse(response)` for every `FETCH_QDN_RESOURCE` result and only falls back to raw `response.text()` when the body is not JSON. |
| `Qortal/Qortal-Hub` `develop` | `12a573b27246e8a626b24794830c6bc432d1b05d` | current host authority that injects the bridge shim into the app render frame. |
| Reference implementation (Shadow Archives) | app commit `472f244` | `src/qortal/qdn.ts` `bridgeFetchResultToText()` and `fetchQdnResourceText` normalize a JSON-parsed bridge result to text; tests cover parsed-object normalization and non-JSON primitives failing closed. Report: `docs/shadow-archives-webportal/runtime/2026-09-13-gallery-host-read-contract-and-media-rendering-report.md`. |

Runtime evidence (why maturity is `verified-runtime`):

- **Runtime-provenance check:** `/apps/q-apps.js` fetched from both live nodes
  was byte-identical to the inspected clone file — md5
  `3ae7deaa55f353dc0ae4e8d13f3c1034`, 37 604 bytes — so the inspected bridge
  source is the code the host actually executes.
- **Observed shapes** inside the real render frame
  `http://127.0.0.1:24992/render/APP/…` against the real injected shim
  (Core `qortal-6.1.9-108bf19`, 2026-09-13):

| Request | Observed result |
| --- | --- |
| `FETCH_QDN_RESOURCE { DOCUMENT, <json id> }` | `typeof === 'object'` (parsed entity), not a string |
| `FETCH_QDN_RESOURCE { DOCUMENT, <json id>, encoding: 'base64' }` | string (base64) |
| `FETCH_QDN_RESOURCE { IMAGE, <media id> }` | string (raw bytes) |
| `GET_QDN_RESOURCE_STATUS` | object |
| `GET_QDN_RESOURCE_URL` | string |
| `SEARCH_QDN_RESOURCES` | array |

- The published build reproduced the defect verbatim on the live node: every
  Gallery card rendered the empty-media glyph and a detail route showed
  `FETCH_QDN_RESOURCE did not return text`. After the boundary normalization and
  a rebuilt bundle, all views loaded in both bridge and same-origin modes.
- Owner real-host acceptance **2026-09-13** (Gallery workflow) confirms the
  corrected build on the real host.

## Scope classification

- **Verified Qortal platform behavior:** the bridge's JSON-parse behavior for
  `FETCH_QDN_RESOURCE`, and the observed shapes for the other actions above
  (current revision only).
- **Reusable transport-boundary pattern:** normalize once, then validate.
- **Dated revision pin:** this is Core `108bf191` behavior; it can change.
- **Not Qortium behavior:** never transfer automatically.

## Reusable contract / procedure

Normalize once, at the transport boundary, before any domain code sees the
result:

1. If the bridge result is a non-null **object** (including arrays), convert it
   to its JSON text form (`JSON.stringify`).
2. If it is already a **string**, pass it through unchanged (this covers raw text
   and `encoding: 'base64'` reads).
3. If it is any other primitive (`null`, number, boolean), **fail closed** with an
   explicit, descriptive error; do not coerce it into a payload that
   validators will misread.
4. **Validate after normalization**: the consumer's own schema/gate must run on
   the normalized text, not on an assumed shape.
5. Keep the normalization in a single helper/module. Do not spread
   "response might be an object" assumptions through repositories, services or
   components.
6. Do not assume the same normalization for other actions: `GET_QDN_RESOURCE_URL`
   returns a string, `GET_QDN_RESOURCE_STATUS` an object, `SEARCH_QDN_RESOURCES`
   an array. Normalize per action at the boundary.
7. **Binary is binary.** Media bytes are rendered by URL (`<img src>`/`<video>`),
   not read through a text helper. Do not JSON-normalize a binary read.
8. **Related verified guard rail (same boundary):** media URLs must be
   **absolute** (`/arbitrary/<service>/<name>[/<identifier>]...`). A relative
   path resolves under the render frame's `<base href>` and the node answers
   `200 text/html` (the app shell), which renders as a broken image.

## Freshness and compatibility gate

Before reuse:

1. Re-check the running Core build against `108bf191` and confirm
   `handleResponse()` in the live `/apps/q-apps.js` still JSON-parses
   `FETCH_QDN_RESOURCE`.
2. Confirm the shapes above still hold for the actions the app uses.
3. Run the smallest contract check: read one JSON `DOCUMENT` and one binary
   resource through the real shim and assert the normalization output.
4. Mark the result `compatible`, `needs-delta-audit`, or `stale`.

Re-run this gate whenever the Core build or Hub bridge changes, or when the app
switches transports (bridge vs same-origin).

## Validation

- Static/unit: a normalization table (parsed object, array, string, base64
  string, non-JSON primitive → fail closed); a shim-contract fake whose JSON
  bodies arrive already parsed.
- Local runtime: exercise the same read path through the bridge contract fake and
  through a same-origin reader, and assert identical downstream results.
- Host/live: probe the real render frame with the real injected shim and record
  `typeof` for each action the app uses.

## Known failure modes

- **Text assumption on a JSON read:** every `DOCUMENT` read throws, which can
  cascade into an unreadable index, detail-route errors, "index update
  incomplete" after a successful publish, and missing-media placeholders.
- **Double parsing:** calling `JSON.parse` on an already-parsed object.
- **Leaked shape assumptions:** casting in domain code instead of normalizing at
  the boundary, so each consumer breaks independently.
- **Wrong action generalization:** assuming `SEARCH_QDN_RESOURCES` or
  `GET_QDN_RESOURCE_STATUS` has the same contract.
- **Relative media URL:** silently renders the app shell HTML as a broken image.

## Non-goals

- A universal contract for every bridge action.
- Qortium bridge behavior.
- Media readiness/playback handling or publication transport (separate skills).

## Harvest / maturity update

- Upgrade evidence: none outstanding — real-render-frame observation plus owner
  runtime acceptance are recorded (2026-09-13).
- Downgrade to `stale` if Core/Hub change `handleResponse()` or the bridge action
  contracts, or if a new transport is adopted.
- Record the new exact revision and observed shapes when re-verifying.
