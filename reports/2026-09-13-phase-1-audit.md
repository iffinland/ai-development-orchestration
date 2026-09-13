# Phase 1 audit and implementation — 2026-09-13

Status: documentation structure implemented and locally verified; owner review
pending. Operational orchestration/GitHub exchange is NOT VERIFIED and is not
reported ready. Primary task class: DOCUMENTATION.

## Scope and evidence

Read-only audit preceded edits: both platform workspaces, active AGENTS/session/
workflow/role/lifecycle/report policies, project routing/context identity,
Qortium WORKSPACE inventory, reference clone and linked-worktree metadata.
Inventoried 750 Markdown documents and 20 Git checkout locations.
Read-only audit means no reference fetch/update, package install or server change.
Historical reports were inventoried, not exhaustively fact-checked.
Sibling non-Qortal/Qortium projects were not included in the workflow.

Baseline: [exact Git inventory](2026-09-13-git-baseline.json) and
[document hashes](2026-09-13-document-inventory.json).

## Findings and authority

- Qortal authority: `/home/iffi/VsCodec-Projects/Qortal/qortal-dev-workspace`.
- Qortium authority: `/home/iffi/VsCodec-Projects/Qortium/qortium-dev-workspace`.
- Both already have Workflow v2, compact controller templates, thin roles and
  canonical project contexts. Reused this structure rather than creating a new
  platform guide system. Shared coordination is now in AI-Orchestration.
- Nine registered contexts: one Qortal and eight Qortium, including one
  unversioned prototype. Registry maps real paths rather than moving projects.
- No shared top-level github-clones directory exists. Nine reference/worktree
  locations exist under Qortium/github-clones. No Qortal platform checkout was
  found under the audited roots.
- Qortium Home is dirty and 241 commits behind its cached origin/main; preserve
  owner changes. Core and extra worktree details are in the exact inventory.
- Qortal SSH prohibition was an environment assumption expressed as a permanent
  platform rule. Corrected active occurrences without changing host validation.
- The Qortium factual authority order conflated source and desired owner behavior;
  corrected it to keep product authorization separate.
- Qortal and Qortium report-storage differences remain intentional. GitHub
  evidence snapshots address visibility without relocating historical reports.

[Full duplicate/conflict list and non-destructive consolidation plan](2026-09-13-duplicates-and-conflicts.md).

## Final file tree

The proposed minimal tree was implemented as follows. No runtime dispatcher,
unused task directories or duplicate technical knowledge base was generated.

```text
AI-Orchestration/
AGENTS.md
ENVIRONMENT.md
GIT-AND-HANDOFF.md
PROJECT-REGISTRY.md
README.md
WORKFLOW.md
reports/2026-09-13-document-inventory.json
reports/2026-09-13-duplicates-and-conflicts.md
reports/2026-09-13-files-changed.txt
reports/2026-09-13-git-baseline.json
reports/2026-09-13-git-final.txt
reports/2026-09-13-phase-1-audit.md
roles/CHATGPT.md
roles/CODEX.md
roles/DEEPSEEK.md
templates/HANDOFF.md
templates/STATUS.json
templates/TASK.md
```

Task directories are created on demand as `tasks/<project>/<task>/` containing
TASK.md, STATUS.json, IMPLEMENTATION.md and AUDIT.md. The reusable HANDOFF.md
shape serves both reports. A real GitHub-backed task has not yet been run.

## Changes and validation

[Exact files created/changed](2026-09-13-files-changed.txt).

Platform AGENTS and session routers load shared coordination even where app
AGENTS point straight to session-start. Both primary-work-model documents route
shared roles there. Shadow Archives gained its missing thin app AGENTS.
No application source or reference checkout was edited.

- Qortal structural validator: PASS, five hygiene warning categories reviewed
  (platform naming, SSH, QAVS, configurable ports, archived UI references).
  The warning wording was corrected; no assertion was disabled.
- Changed-repository whitespace checks: PASS.
- Universal file links: all 30 resolve. STATUS JSON parses; both platform routers
  resolve the shared contract. All original HEADs and unaffected checkout statuses
  match baseline. Complete tracked diffs reviewed.
- Pre-existing Markdown outside the explicit change allowlist: 735
  files verified byte-for-byte unchanged against the audit snapshot.
- Semantic self-review: owner authorization remains explicit; no tunnel/node
  reachability is represented as host proof; dirty references cannot be reset;
  handoffs bind to exact SHAs; no background execution is implied.
- No tests/builds/package commands for application code: documentation-only work.
- No live host, QDN publication, SSH or GitHub handoff validation claimed.

## Exact Git state

[Full final status for every inspected checkout](2026-09-13-git-final.txt).
New repository is on `agent/orchestration/bootstrap`, has no commits and no remote.
Qortal workspace HEAD remains `91b664b9747c`; Qortium workspace HEAD remains
`4115dcb8a4a6`; Shadow Archives HEAD remains `6ec2915a47b8`.
Qortium parent root remains `36bac59d6aa6`, without a remote; its existing stale
gitlinks and dirty/untracked tree were not staged or synchronized.
All remote ahead/behind results use cached refs and are not live parity claims.
Commit: no. Push: no. Delete/move: no. SSH/VPS changes: no. Packages: no.

## Phase 2 plan

1. Verify upstreams and safely fetch/synchronize references. Preserve dirty Home
   and intentional pins; create an isolated current reference if needed. Add
   missing verified Qortal Core/Hub/framework clones beneath the shared root.
2. Inspect current tunnel/client/init setup read-only, confirm the three intended
   remote API listeners and networks, and choose collision-free loopback ports.
3. After explicit configuration/package authorization, reuse an existing suitable
   supervisor or configure one for three independent SSH forwards and autostart.
4. Prove three concurrent real API reads, reconnection and real session/reboot
   autostart. Record exact environment/version/provenance and rollback.
5. Separately approve the GitHub remote and agent-branch push scope; publish the
   contract, verify a real DeepSeek-to-Codex exact-SHA handoff and only then enable
   any requested dispatcher/monitoring. GitHub storage alone does not wake agents.

Report saved: /home/iffi/VsCodec-Projects/AI-Orchestration/reports/2026-09-13-phase-1-audit.md
