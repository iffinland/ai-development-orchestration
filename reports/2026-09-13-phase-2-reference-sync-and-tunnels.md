# Phase 2 — reference synchronization and tunnels

Status: PARTIALLY COMPLETE.

## Completed

- Fetched every audited Qortium reference remote without resetting, cleaning or
  stashing owner work.
- Fast-forwarded clean `qortium-core` to `d71bc8f6`, `qortium-boards` to
  `dc888cc8`, and `discussion-boards-reference` to `0a52d5de`.
- Preserved the dirty Qortium Home checkout at `927d932b`; it is now 256 commits
  behind `origin/main`. Created a clean detached reference worktree at
  `/home/iffi/VsCodec-Projects/github-clones/Qortium/qortium-home-current`,
  commit `155356c`.
- Created clean Qortal Core, Hub and framework clones under
  `/home/iffi/VsCodec-Projects/github-clones/Qortal`. Verified upstream HEADs:
  Core `108bf191`, Hub `12a573b2`, qapp-core `0f9d6ac5`, qapp-templates
  `143cc7b`.
- Replaced the Qortium-only Xfce startup target with a generic node-tunnel
  supervisor. It accepts only explicit SSH aliases, has a lock, writes logs and
  restarts failed SSH children after ten seconds.
- Preserved exact rollback copies of the former script and desktop entry under
  `/home/iffi/.local/share/dev-node-tunnels/backups/2026-09-13-phase-2/`.
- Verified Qortium loopback API at `http://127.0.0.1:24891`: HTTP 200,
  synchronized testnet full node, version `qortium-1.8.0-05cbc08`.
- Terminated the active Qortium SSH child deliberately. The supervisor created a
  new child and the node API returned HTTP 200. Verified supervisor stop leaves
  no tunnel process behind and a clean restart creates one process group.

## Not complete

- The local SSH configuration has only `qortium-vps`; `qortal-node-a` and
  `qortal-node-b` are not defined. The supervisor logs both as skipped and opens
  no guessed ports. Their hosts, accounts and remote loopback API ports are
  required before those two tunnels can exist.
- A real Xfce logout/login or reboot was not performed. The desktop entry passes
  format validation and a manually launched supervisor survived the calling
  session, but that does not prove login autostart.
- No three-node concurrent API check is possible until the two Qortal targets
  are configured.

## Changed local files

- `/home/iffi/.local/bin/dev-node-tunnels.sh` (new, executable)
- `/home/iffi/.config/autostart/Qortium SSH Tunnel.desktop` (updated target and
  corrected obsolete desktop-entry keys)
- `/home/iffi/VsCodec-Projects/AI-Orchestration/ENVIRONMENT.md`
- this report

No package installation, VPS configuration, platform-source modification,
commit, push, release, QDN publication or destructive cleanup occurred.

## Validation

- `bash -n /home/iffi/.local/bin/dev-node-tunnels.sh`: pass.
- `desktop-file-validate`: pass.
- Qortium Core, Boards, Discussion Boards and all new Qortal clones: clean and
  equal their checked upstream branch heads.
- Existing dirty Home checkout and linked worktrees: preserved.
- Qortium reconnect, API health and clean supervisor lifecycle: pass.

## Resume inputs

Provide or configure two explicit SSH aliases, each with a verified host,
account, host key and local-forward target. Then restart the existing supervisor,
verify the two independent Qortal APIs, validate three concurrent listeners, and
perform a real logout/login test.

Report saved:
/home/iffi/VsCodec-Projects/AI-Orchestration/reports/2026-09-13-phase-2-reference-sync-and-tunnels.md
