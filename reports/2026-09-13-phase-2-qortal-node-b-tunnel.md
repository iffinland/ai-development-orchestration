# Phase 2 continuation — Qortal node tunnels

Status: COMPLETE.

The owner provided two Qortal node URLs and SSH account credentials. Their
secrets are deliberately absent from this report and all local configuration.
The workstation's existing public SSH key was installed on both supplied SSH
accounts under explicit owner authorization.

## Verified topology

- Node B: SSH host `144.91.123.144` has a local Qortal API listener at
  `127.0.0.1:12391`. The configured `qortal-node-b` alias forwards it to
  `127.0.0.1:24992`. API `/admin/info` returns HTTP 200 from a mainnet full node,
  `qortal-6.1.9-108bf19`.
- Node A: the Qortal installation was present at `/home/iffiolen/qortal` but
  stopped with a stale `run.pid`. Resource checks showed 11 GiB available RAM
  and 161 GiB free disk. Its existing `start.sh` was launched. The API began
  listening at `127.0.0.1:12391`, reached `syncPercent: 100`, and is forwarded
  as `qortal-node-a` to `127.0.0.1:24991`.

## Changes and validation

- Added key-only `qortal-node-a` and `qortal-node-b` SSH configuration with
  loopback-only forwards `24991 -> 127.0.0.1:12391` and
  `24992 -> 127.0.0.1:12391`.
- Restarted the existing Xfce tunnel supervisor; Qortium and node B run together.
- Terminated each Qortal SSH child deliberately; each restarted after ten
  seconds and its local API returned HTTP 200.
- Three concurrent read-only API checks passed: Qortium testnet at `24891`,
  Qortal mainnet A at `24991`, and Qortal mainnet B at `24992`.
- No API key, password, remote node configuration, package, platform source,
  commit, push or QDN write was stored or performed.

## Reboot acceptance

The owner performed a real workstation reboot. The new boot began at
`2026-09-13 14:33:33` local time. Xfce launched the tunnel supervisor at
`2026-09-13 14:34:25` local time; it then launched all three configured SSH
children: `qortium-vps`, `qortal-node-a`, and `qortal-node-b`.

After that restart, loopback listeners were present on `24891`, `24991`, and
`24992`. Each corresponding read-only `/admin/status` request returned HTTP
200 with `syncPercent: 100`. This completes the autostart acceptance check.

Report saved:
/home/iffi/VsCodec-Projects/AI-Orchestration/reports/2026-09-13-phase-2-qortal-node-b-tunnel.md
