# Environment and reference registry

Updated: 2026-09-13. Paths and reference SHAs below were checked against their
upstreams in phase 2. Never infer a network from a port alone.

| ID | Local endpoint | Observed state | Required next verification |
| --- | --- | --- | --- |
| qortium-node | http://127.0.0.1:24891 | SSH forward verified; Qortium testnet full node, `qortium-1.8.0-05cbc08`, synchronized | Record remote transport/node provenance when changed |
| qortal-node-a | `http://127.0.0.1:24991` | SSH tunnel verified to VPS loopback `12391`; Qortal mainnet full node `qortal-6.1.9-108bf19`, synchronized | Record remote transport/node provenance when changed |
| qortal-node-b | `http://127.0.0.1:24992` | SSH tunnel verified to VPS loopback `12391`; Qortal mainnet full node `qortal-6.1.9-108bf19` | Record remote transport/node provenance when changed |

`24991` and `24992` remain candidates only, not assigned endpoints. Inspect listeners
again before configuration. Each verified endpoint entry must record transport,
network, verification timestamp, remote bind/port, node/host version, allowed
read operations and evidence. Keep sensitive host/account data in owner-local
configuration, not GitHub. Node access does not prove Hub/Home bridge behavior.

## Reference inventory

The legacy Qortium root remains
`/home/iffi/VsCodec-Projects/Qortium/github-clones`. New shared references are
under `/home/iffi/VsCodec-Projects/github-clones`. Existing checkouts were not
moved.

| Checkout beneath actual root | Role / refresh decision |
| --- | --- |
| qortium-core | Primary Core reference; clean and fast-forwarded to `d71bc8f6` |
| qortium-home | Existing Home reference; dirty, 256 commits behind `origin/main`; preserved untouched |
| ../../github-clones/Qortium/qortium-home-current | New clean detached current reference at `155356c` |
| qortium-core-android-stream-fix | Linked worktree with owner changes; preserve |
| qortium-home-background-audio | Linked worktree with owner changes; preserve |
| qortium-home-v2.0.0 | Intentional detached reference worktree; preserve pin |
| qortium-home-auth-reference | Intentional detached reference worktree; preserve pin |
| discussion-boards-reference | Clean comparison checkout; not a governance source |
| qortium-boards | Donor reference; not application identity authority |
| Q-Music-v_2.0 | Historical/visual reference; not NodeFM architecture |

Qortal references created under `/home/iffi/VsCodec-Projects/github-clones/Qortal/`:
`qortal` master `108bf191`, `Qortal-Hub` develop `12a573b2`, `qapp-core` master
`0f9d6ac5`, and `qapp-templates` main `143cc7b`. All are clean and equal their
verified upstream branch HEADs. These match the prior Shadow Archives source
evidence, but future tasks still perform the freshness gate.


## Remote reference snapshot used by the skills redesign

This package update performed read-only GitHub source inspection on 2026-09-13.
It did **not** clone, fetch, reset or modify the owner's local reference checkouts.
These revisions are research baselines for the initial skills only; task-time
freshness rules still apply.

| Public repository / branch | Observed revision | Why inspected |
| --- | --- | --- |
| `Qortal/Qortal-Hub` `develop` | `12a573b27246e8a626b24794830c6bc432d1b05d` | Hub agent/skills architecture and current host authority |
| `Qortal/q-tube` `main` | `68c3ea706c4ab110ffa44a7f55f8e09bdf7e85ff` | Q-Tube video identifier/discovery/publication contract |
| `Qortal/Subwire` `master` | `a933a6c44d60db19cd219408e36c747aebcce994` | Q-Tube-compatible cross-app video conventions |
| `Qortal/create-qortal-app` `main` | `ea9d720bb31fa42b777659aceccd69ad20393abb` | current official Qortal scaffold/CLI reference |
| `QortiumDev/qortium-home` `main` | `155356cdd5f2f91353b387f88f8c591057fd6831` | Qortium bridge/QDN host authority |
| `QortiumDev/qortium-radio` `master` | `870daccb9cd408f175b732e24f56d98e1d63eeeb` | live-tested QDN list/readiness patterns |
| `QortiumDev/qortium-paint` `main` | `f792ae60f3b8ad7692ec7845ea710a0b98b84320` | public CLAUDE.md and reusable bridge/publish conventions |

Do not treat this table as a frozen dependency lock. A task that relies on one
of these contracts must re-run the relevant freshness/compatibility check.

## Mandatory freshness gate

Before each platform-dependent phase:
1. Resolve the exact required Core, Home/Hub, framework and donor references.
2. Record path, remote, branch, HEAD, dirty files and linked worktrees.
3. Check the upstream branch live and fetch the relevant remote refs; record UTC
   time and upstream SHA. A cached origin ref is not a freshness check. If network
   is unavailable, state the reference freshness blocker for dependent claims.
4. For a clean tracking checkout, use a fast-forward-only update when needed.
   Preserve intentional pins. For dirty/diverged references, use a new clean
   reference worktree at the verified upstream SHA, leaving owner work untouched.
   Never reset, clean, auto-stash, force-update, or relocate worktrees.
5. Record the actual inspected SHA, relevant source paths and difference from
   the deployed runtime version. Verify dependent behavior against that runtime.

Phase 2 fetched reference remotes, fast-forwarded clean Qortium Core, Boards and
Discussion Boards references, and created the clean Home worktree and Qortal
clones. It did not modify platform source, dirty owner trees or existing pinned
worktrees. Reference updates do not authorize platform modifications, server
changes or publication.

## Phase 2, after owner approval

The observed Xfce autostart entry now runs
`/home/iffi/.local/bin/dev-node-tunnels.sh`. It isolates its own session, uses a
single lock, permits only explicitly configured SSH aliases, binds only through
the SSH configuration, restarts a failed tunnel after ten seconds, and logs to
`~/.local/state/dev-node-tunnels/`. Its prior Qortium-only script and desktop
entry are backed up under `~/.local/share/dev-node-tunnels/backups/2026-09-13-phase-2/`.
No package was installed. Qortium reconnection was verified after intentionally
terminating its SSH child; its API returned HTTP 200 after restart.

Qortal nodes A and B are configured as `qortal-node-a` and `qortal-node-b`,
forwarding local `24991` and `24992` to their VPS loopback `12391` APIs. SSH
public-key authentication was installed after explicit owner authorization.
Node A's Qortal process had been stopped with a stale pid file; the existing
`/home/iffiolen/qortal/start.sh` was launched after resource and stale-process
checks. The node reached `syncPercent: 100`. Supplied Qortal API keys are not
SSH credentials and are intentionally not stored here.

All three identified read-only APIs now work concurrently. Qortium and Qortal A
and B tunnel reconnection checks passed; no tunnel binds publicly. The owner
then performed a real reboot: the new boot began at `2026-09-13 14:33:33` local
time and Xfce started the supervisor at `2026-09-13 14:34:25`. All three
loopback listeners returned afterward and each read-only `/admin/status` check
returned HTTP 200 with `syncPercent: 100`. This completes the autostart
acceptance layer.
