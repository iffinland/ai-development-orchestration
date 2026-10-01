---
name: qortium-account-write-gate
description: Use when a Qortium app must keep read-only/listening surfaces usable without an unlocked account while every signed or QDN write passes through one shared gate that unlocks through Home's own UI and resumes the original write.
---

# Qortium account write gate

- Platform: `qortium`
- Maturity: `verified-runtime`
- Last checked: `2026-09-18`
- Owner: shared capability library

## Use when

- A Qortium app has both public/read-only surfaces (opening the app, media
  playback, browsing public resources) and signed/QDN writes (likes, publishing,
  playlists, submissions, moderation, schedules, config, tips, direct messages).
- Reads are being blocked, or writes are being attempted, by an app that
  currently asks for the wallet password itself, or that fails with a raw
  signing error when the selected account is locked.
- Several features each grew their own account check and they disagree about
  what "ready to write" means.

## Do not use when

- The platform is Qortal: `qortalRequest` authentication, unlock and permission
  semantics are a separate contract. Confirm that platform separately.
- The task is read-only: nothing in this skill belongs on a read path.
- The app needs the wallet *password* for its own logic (it never does). The
  password stays inside Home; this skill only observes account state.

## Authoritative evidence

| Source | Revision | Paths / contract proved |
| --- | --- | --- |
| `QortiumDev/qortium-home` | tag `v2.1.0-beta.11` = `5129317fca9af8f6c19f7f72d34f6948dabf0f34` | `electron/qdn.ts` (`GET_SELECTED_ACCOUNT` shape and the `No account is selected for this tab.` error), `electron/home-v2-app-actions.ts` + `electron/home-v2-app-bridge.ts` (`UNLOCK_SELECTED_ACCOUNT` availability, Home-rendered password dialog, ~60 s prompt timeout at `electron/home-v2-app-bridge.ts:5949`, `Account access was denied.` on expiry/deny) |
| `QortiumDev/qortium-home` | same revision | advertised action list on `qdnRequest` contains **no** app-triggered account select/create/onboarding action; `UNLOCK_SELECTED_ACCOUNT` is the only account-mutating action an app can invoke |
| NodeFM worktree (`qortium/nodefm-station`, `main` @ `4cb5729` + migration changes) | uncommitted Home 2.1 migration | `src/qortium/accountWriteGate.ts` as the reference implementation: one gate, three readiness states, single in-flight unlock, `runAccountWrite()` wrapper, explicit cancel error; `src/hooks/useStableAccountIdentity.ts` for holding the resolved `{ address, name }` across a transient auth `loading` |
| NodeFM worktree | same | `src/pages/ListenerPlaylistEditorPage.tsx` and `src/features/listener-submissions/components/SubmitMusicForm.tsx` as the auth-refresh-safe page pattern: page-local draft/progress keyed to a resolved identity and a run token, never to the transient `loading` state |

Runtime evidence (real Home 2.1.0-beta.11 desktop, real Qortium testnet node
`qortium-1.8.0-05cbc08`, account `iffi_vaba_mees`, 2026-09-17 and 2026-09-18):

- Read-only use with the account **locked**: app shell loaded, Live Radio played
  (player time advanced 5:14 → 5:26 in 9 s, real MP3 decode), public browsing and
  QDN reads worked, and no Home unlock prompt was raised by any read.
- `GET_SELECTED_ACCOUNT` returned `{ address, name, isUnlocked: false }` while
  locked; the gate therefore reported `locked` without touching Home's UI.
- A locked write (`PUBLISH_QDN_RESOURCE` via a Like) produced the sequence
  `GET_SELECTED_ACCOUNT` → `SHOW_ACTIONS` → `UNLOCK_SELECTED_ACCOUNT`, Home's own
  "Unlock account" dialog with a password field appeared, and Home's prompt
  window measured 60 135 ms before answering `Account access was denied.`
  Because the owner did not finish in that window the write was abandoned:
  **zero** QDN writes, no duplicate publication, no retry loop, and truthful UI.
- The same write, re-run with the account unlocked, resolved the gate with a
  bare `GET_SELECTED_ACCOUNT` and published immediately with no Home UI.
- A locked write re-tested with the owner unlocking inside Home's dialog resumed
  **the original operation automatically**: after `UNLOCK_SELECTED_ACCOUNT`
  returned, Home raised the normal publish approval for the same pending write
  with no second user click.
- Lock/unlock is **not** an identity change. Home emits a selected-account change
  on the wallet lock-state transition, and a naive auth provider answers it with
  a transient `loading` state even though `GET_SELECTED_ACCOUNT` still resolves
  the same `{ address, name }` (only `isUnlocked` differs). Keying page identity
  on that transient dropped the authored draft and the in-flight progress modal
  in two NodeFM features (`ListenerPlaylistEditor`, `SubmitMusicForm`) while the
  write itself completed — the write ran on, the page reset around it.
- With the resolved identity held across the transient, the locked→unlock cycle
  kept the draft, the track rows, the `Publishing` modal and the disabled
  publish button; after Home's approval the same run rendered its normal success
  state. A real account change still reset the page and its late completion was
  ignored.

## Reusable contract / procedure

1. **Split read from write, in code.** Reads and playback never call the gate.
   The gate is invoked by the write function itself, not by app startup, not by
   route guards and not by data loading.
2. **One gate, one entry point.** Provide exactly one `requireAccountWrite()` /
   `runAccountWrite(action, fn)` used by every signed/QDN write. Feature modules
   pass an action label for diagnostics and receive an account ticket; they never
   call the unlock action or inspect `isUnlocked` themselves.
3. **Read the selected account state without prompting.**
   `GET_SELECTED_ACCOUNT` returns the account the write would be signed with.
   Treat a missing `isUnlocked` field as locked. Home throws
   `No account is selected for this tab.` when the app tab has no selected
   account — map that to the `no-account` state instead of a crash.
4. **Three readiness states, three responses.**
   - *ready* (`isUnlocked: true`) → resolve immediately, no Home UI.
   - *locked* → invoke the runtime's supported unlock action
     (`UNLOCK_SELECTED_ACCOUNT`), which opens Home's own password UI; resolve
     only after Home reports the account unlocked, so the caller resumes the
     original write without a second user action.
   - *no account* → fail with the platform limitation, after checking which
     account-related actions the runtime actually advertises.
5. **Feature-detect; never invent account bridge actions.** Read the advertised
   action list (`SHOW_ACTIONS`) and require the unlock action before using it.
   If the runtime advertises no account-selection/creation/onboarding action,
   report that Home cannot be asked to create or select an account from the app
   and instruct the user to do it in Home. Do not guess action names, and do not
   fall back to signing with a different account.
6. **Fail closed on the unlock path.** If the runtime does not advertise the
   unlock action, the gate must throw before any write is attempted rather than
   publishing and hoping.
7. **Cancellation is a failure, not a retry.** Home answers a denied or expired
   prompt by returning the account still locked (or by failing the unlock call).
   The gate re-reads the account once to be sure, then raises a distinct
   "cancelled" error. The caller must abort with **zero** writes, no duplicate
   publication, no automatic retry, and must restore truthful UI state.
8. **Share one unlock prompt.** Concurrent writes that all find a locked account
   must coalesce onto a single unlock attempt; the write runs exactly once after
   the account is confirmed unlocked.
9. **The password never leaves Home.** The app must never request, read, log,
   store, transmit or infer the wallet password; it only observes account state
   and the unlock result.
10. **Budget for the prompt window.** Home's unlock prompt is timeboxed
    (~60 s in 2.1). Surface the window to the user, bring Home's window to the
    foreground, and treat expiry as the cancel path.
11. **A lock-state `loading` is not an identity change.** The selected-account
    event fired by a wallet lock/unlock makes the app's auth provider resolve
    asynchronously. Hold the last resolved `{ address, name }` while auth
    reports `loading`, and treat only a non-loading resolution (same or
    different account, `unauthenticated`, `error`) as an identity outcome.
    Otherwise every unlock resets the page that requested the write.
12. **Preserve page-local state across the unlock; invalidate it on a real
    change.** The write flow owns its draft, progress UI and busy flag across
    Home's unlock. Give each run a token: a real account or route change bumps
    it, clears the local state, and makes the late completion of an abandoned
    run a no-op. Never let a resolved-but-superseded async run write into the
    next page's state.

## Freshness and compatibility gate

Before reuse:

1. resolve the running Home revision (`GET_HOST_INFO.hostVersion` /
   `platformVersion`) and compare it with the revisions recorded above;
2. confirm from the advertised action list that the unlock action names used here
   still exist, and re-check whether an app-triggered account
   selection/creation/onboarding action has appeared (if it has, wire it as the
   `no-account` path instead of only reporting the limitation);
3. re-measure the unlock prompt timeout and the unlock response shape in the
   new revision;
4. run the smallest runtime check: read-only use with the account locked (no
   prompt), one locked write (prompt appears, cancel writes nothing), one
   unlocked write (immediate);
5. mark the result `compatible`, `needs-delta-audit`, or `stale`.

An action-list snapshot alone is not proof: an app can only observe the unlock
contract by exercising it against a real locked account.

## Validation

- Static/automated: one gate module with unit tests for ready / locked /
  no-account / unlock-unsupported, coalesced concurrent unlock, and
  cancel-produces-no-write.
- Host runtime, read path: with the account locked, prove the shell loads, media
  plays and public reads succeed, and that no bridge call in those paths is an
  unlock or write action.
- Host runtime, write path: with the account locked, prove Home's password UI
  appears from the app's own write, that unlocking resumes the original write
  once, and that denying/expiring it produces zero writes and no retry.
- Wire evidence: record the request sequence
  (`GET_SELECTED_ACCOUNT` → unlock action → original write) and the absence of
  duplicate publish requests.
- Refresh behavior: prove a lock-state-only refresh (`A → loading → A`) keeps
  the page's local draft and in-flight progress, while a real account change
  (`A → B`) still resets the page and ignores the previous run's completion.

## Known failure modes

- Wiring the gate into app startup or into read paths: the app starts demanding
  an unlock before it can show public content, which is the exact regression this
  gate exists to prevent.
- Duplicating account handling inside each feature, so one feature publishes
  while another silently fails with a signing error.
- Treating `Account access was denied.` as a transport error and retrying, which
  can publish twice when the account was in fact unlocked.
- Assuming an acknowledgement from the unlock call means success, instead of
  re-reading the account state.
- Assuming the app can create or select an account: Home 2.1 advertises no such
  action, so a missing/invalid selected account is a user task in Home, not an
  app workflow.
- Blocking a whole page behind an unlock prompt, so reading stops working while
  the prompt is open.
- Treating the auth provider's transient `loading` on a lock-state change as an
  account change: the page resets (draft lost, progress modal unmounted) while
  the write it started is still running, and the success confirmation is never
  shown even though the write landed.
- Letting a resumed write outlive its page without a run token, so its
  completion writes progress into whatever page state exists next.
- Freezing page state forever on `loading`: a genuine account change or an auth
  error must still invalidate a stale identity and its async runs.

## Non-goals

- The Qortal authentication/unlock contract.
- Wallet/key management, password handling, or a portable credential prompt.
- Any application's specific resource coordinates, business rules or UI layout.
- Deciding which writes an app should offer; this skill only governs how an
  already-chosen write is authorized.

## Harvest / maturity update

`verified-runtime` rests on a real Home 2.1 runtime in which the locked read path
stayed prompt-free, a locked write opened Home's own unlock dialog, an unlocked
write ran immediately, an expired prompt produced zero writes, and an unlock
completed inside the prompt window resumed the original write automatically.
The 2026-09-18 NodeFM final-audit pass added the page-state half of the
contract: lock-state `loading` keeps the resolved identity and the page's local
draft/progress, while real account/route changes still invalidate stale runs.

Downgrade to `needs-delta-audit` if Home changes the account-state action shape,
the set of app-invokable account actions, the unlock prompt timeout, or the
unlock response semantics; re-run the freshness gate above before reuse.
