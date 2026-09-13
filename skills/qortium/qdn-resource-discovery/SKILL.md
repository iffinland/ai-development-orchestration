---
name: qortium-qdn-resource-discovery
description: Use when a Qortium app must enumerate QDN resources by publisher or discover resources by identifier/search criteria without rediscovering LIST_QDN_RESOURCES vs SEARCH_QDN_RESOURCES behavior.
---

# Qortium QDN resource discovery

- Platform: `qortium`
- Maturity: `verified-reference`
- Last checked: `2026-09-13`
- Owner: shared capability library

## Authoritative / working evidence

| Source | Revision | Evidence |
| --- | --- | --- |
| `QortiumDev/qortium-radio` | `870daccb9cd408f175b732e24f56d98e1d63eeeb` | `src/api/qdn.ts` documents and implements publisher AUDIO enumeration with `LIST_QDN_RESOURCES`; the app records a live test where search returned 1 of 19 while list returned all 19. |
| `QortiumDev/qortium-home` | `155356cdd5f2f91353b387f88f8c591057fd6831` | current Home bridge/action documentation is the authority for supported QDN actions and response contracts. |

## Reusable contract

Do not treat list and search as interchangeable.

- When the semantic requirement is **all resources a known publisher/name has
  published for a service**, start from the current verified
  `LIST_QDN_RESOURCES` contract.
- When the requirement is **search/discovery by identifier/title/metadata or
  across publishers**, use the current search capability and verify its
  semantics for that query.
- Normalize only response shapes actually returned by the selected action; do
  not assume all bridge actions wrap data identically.

## Compatibility gate

Before reuse, compare current Home and the target app's selected runtime with
these revisions and inspect any changes to list/search bridge actions. A small
contract smoke with a publisher having multiple known resources is preferred to
another full architecture audit.

## Validation

For an app claiming complete publisher enumeration, validate against a real
publisher with more than one resource and compare count/identifiers to the live
node. A green mocked test is insufficient.

## Maturity upgrade

Upgrade to `verified-runtime` after our own target Qortium runtime proves the
complete-list scenario and the result is recorded in a task handoff.
