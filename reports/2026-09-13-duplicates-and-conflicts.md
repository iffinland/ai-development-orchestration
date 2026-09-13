# Duplicate and conflict inventory — 2026-09-13

Audit scanned 750 Markdown files under both platform roots and the registered
Qortal application, excluding dependencies/builds/.git. Hash equality identifies
byte duplicates; semantic conclusions below concern active governance only.
Historical product reports were inventoried, not all re-audited for correctness.

## Active conflicts and disposition

| Finding | Evidence / disposition |
| --- | --- |
| Qortal blanket SSH prohibition | Found in AGENTS, README, workflow-v2, standard section 12, bridge guide, live-validation guide, CODEX and DEEPSEEK overlays, report-policy rationale and validator warning wording. All active instances corrected. Historical reports retained. |
| Codex role lacked local coordination | Both primary-work-model documents and entrypoints now route to universal roles; platform duties remain overlays. No running dispatcher is claimed. |
| Qortium owner decisions below source | source-of-truth-and-lifecycle conflated product intent with implemented behavior. Split factual source order from owner intent/authorization. |
| Report locations differ | Qortal uses its governance repo docs; Qortium uses sibling docs largely outside useful Git. Keep canonical roots; GitHub handoff needs approved sanitized durable evidence for local-only reports. |
| GitHub handoff vs no push without authorization | Agent branch design is now explicit; task-scoped commit/push authorization remains required and reusable. No remote was created or pushed in phase 1. |
| Different completion vocabularies | Shared STATUS state is separate from platform report verdict; missing host/owner evidence cannot map to complete. |
| Proposed shared github-clones absent | Actual references live under Qortium/github-clones. Keep them; a Qortal namespace may be added during phase 2. |
| Home reference freshness | Home main is dirty and 241 commits behind cached origin/main. This is not a live remote freshness result. Use an isolated fresh reference after fetch, not a destructive pull/reset. |
| Shadow Archives missing app AGENTS | Thin Qortal-specific router added at its actual path; no relocation. |
| Qortium WORKSPACE.md dated 2026-08-30 | Useful inventory but current Core HEAD and additional worktrees differ. Universal registry records current inventory; update old inventory after phase-2 synchronization. |
| Legacy root gitlinks | Qortium root has no remote and stale gitlinks; not a synchronization layer. No gitlink/index edits performed. |
| Project contexts contain dated snapshots | Keep as provenance; current source/runtime must be checked per task, not inferred from old phase descriptions. |

## Intentional multiple checkouts — not deletion candidates

- qortium-home-v2.0.0 and qortium-home-auth-reference are detached linked worktrees.
- qortium-home-background-audio and qortium-core-android-stream-fix are linked
  task worktrees with owner changes.
- Home worktree metadata also lists a missing `/tmp/ivm-audit-home-20260908` path
  as prunable. No prune was performed; inspect recovery needs first.
- discussion-boards-reference is a deliberate comparison clone. Its `agents/`
  includes old governance; three guides are byte-identical to canonical guides
  (runtime diagnostics, issue audit/refactor, Git hygiene). They are reference
  evidence, not current routing.
- community-discussion-boards is an unversioned prototype; Discssion-Boards is
  a different active repository. Similar names do not imply duplicate products.
- Q-Music-v_2.0 is an intentional historical visual reference.

## Consolidation plan before any destructive cleanup

1. Keep the new universal layer small. Platform source contracts stay separate;
   Qortal and Qortium are not interchangeable despite similar document names.
2. After owner review, publish the shared contract and scoped platform routers
   on authorized branches. Verify remote parity and an actual two-agent handoff.
3. Inventory legacy reference guides by hash, ownership and historical role.
   Prefer marking their reference status in the registry to editing donor clones.
4. For any proposed removal/move, present exact paths, migrated unique content,
   Git/worktree dependencies, recoverable backup and rollback plan first.
5. Only an explicitly approved cleanup task may remove files, prune metadata,
   relocate clones or replace duplicated platform workflow prose with pointers.
   Phase 1 deletes and relocates nothing.

## Byte-identical Markdown groups

Hash equality is only a candidate inventory. It does not authorize deletion.

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/README.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/README.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/preview/TESTER-GUIDE.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/preview/TESTER-GUIDE.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/preview/OPERATOR-RUNBOOK.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/preview/OPERATOR-RUNBOOK.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/preview/README.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/preview/README.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/src/test/resources/chat/interop/README.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/src/test/resources/chat/interop/README.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/README.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/README.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/development/database.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/development/database.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/development/testing.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/development/testing.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/development/developer-proxy.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/development/developer-proxy.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/development/public-api-allowlist.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/development/public-api-allowlist.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/development/notifications.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/development/notifications.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/development/ultra-review-remediation-plan.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/development/ultra-review-remediation-plan.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/dependencies/dependency-provenance.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/dependencies/dependency-provenance.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/dependencies/code-scanning-triage.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/dependencies/code-scanning-triage.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/dependencies/dependency-security-review.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/dependencies/dependency-security-review.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/chain-design/at-map-storage.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/chain-design/at-map-storage.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/chain-design/on-chain-chain-parameters.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/chain-design/on-chain-chain-parameters.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/chain-design/chain-parameter-audit.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/chain-design/chain-parameter-audit.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/releases/v1.0.0-preview.11.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/releases/v1.0.0-preview.11.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/releases/v1.0.0-preview.9.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/releases/v1.0.0-preview.9.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/releases/v1.0.0-preview.8.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/releases/v1.0.0-preview.8.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/releases/v1.0.0-preview.12.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/releases/v1.0.0-preview.12.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/releases/v1.2.1.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/releases/v1.2.1.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/releases/v1.0.0-preview.14.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/releases/v1.0.0-preview.14.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/releases/v1.0.0-preview.13.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/releases/v1.0.0-preview.13.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/releases/v1.0.0-preview.15.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/releases/v1.0.0-preview.15.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/networking/peer-maintenance.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/networking/peer-maintenance.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/networking/i2p-fallback-operator-guide.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/networking/i2p-fallback-operator-guide.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/cross-chain/electrum-server-refresh.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/cross-chain/electrum-server-refresh.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/cross-chain/crosschain-reverse-trades.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/cross-chain/crosschain-reverse-trades.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/cross-chain/crosschain-foreign-foreign-trades.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/cross-chain/crosschain-foreign-foreign-trades.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/cross-chain/bitcoiny-chain-specs.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/cross-chain/bitcoiny-chain-specs.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/cross-chain/zcash-family-chain-support.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/cross-chain/zcash-family-chain-support.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/cross-chain/electrum-tls-trust.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/cross-chain/electrum-tls-trust.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/chat/chat-portability-roadmap.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/chat/chat-portability-roadmap.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/chat/private-group-chat-encryption.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/chat/private-group-chat-encryption.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/qdn/q-apps.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/qdn/q-apps.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/qdn/multi-file-resources.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/qdn/multi-file-resources.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/qdn/encrypted-data-envelope.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/qdn/encrypted-data-envelope.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/design/networkdata-capacity.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/design/networkdata-capacity.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/design/i2p-fallback-transport.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/design/i2p-fallback-transport.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/design/dev-group-approval-split.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/design/dev-group-approval-split.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/design/node-minting-reward-bundles.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/design/node-minting-reward-bundles.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/trust/aura-trust-tier-minting.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/trust/aura-trust-tier-minting.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/trust/trust-network-client-integration.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/trust/trust-network-client-integration.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/trust/trust-network-launch-readiness.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/trust/trust-network-launch-readiness.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/trust/account-trust-network.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/trust/account-trust-network.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/upstream/qortal-6.1.8-comparison.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/upstream/qortal-6.1.8-comparison.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/upstream/qortal-v6-network-notes.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/upstream/qortal-v6-network-notes.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/upstream/qortal-6.1.6-comparison.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/upstream/qortal-6.1.6-comparison.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/upstream/qortal-6.1.9-comparison.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/upstream/qortal-6.1.9-comparison.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/upstream/qortal-6.1.5-comparison.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/upstream/qortal-6.1.5-comparison.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/upstream/qortal-6.1.7-comparison.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/upstream/qortal-6.1.7-comparison.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/lite-node/lite-node-proof-anchoring.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/lite-node/lite-node-proof-anchoring.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/lite-node/lite-node-state-root-design.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/lite-node/lite-node-state-root-design.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/docs/lite-node/lite-node-plan.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/docs/lite-node/lite-node-plan.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/WindowsInstaller/README.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/WindowsInstaller/README.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/testnet/README.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/testnet/README.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core/tools/auto-update-scripts/README.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-core-android-stream-fix/tools/auto-update-scripts/README.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/discussion-boards-reference/IMPLEMENTATION-SUMMARY.md`
- `/home/iffi/VsCodec-Projects/Qortium/docs/discussion-boards/implementations/2026-05-14-empty-content-fix-implementation.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/discussion-boards-reference/ANALYSIS-REPORT.md`
- `/home/iffi/VsCodec-Projects/Qortium/docs/discussion-boards/investigations/2026-05-14-empty-content-analysis.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/discussion-boards-reference/README.md`
- `/home/iffi/VsCodec-Projects/Qortium/projects/Discssion-Boards/README.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/discussion-boards-reference/THIRD_PARTY_NOTICES.md`
- `/home/iffi/VsCodec-Projects/Qortium/projects/Discssion-Boards/THIRD_PARTY_NOTICES.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/discussion-boards-reference/src/features/forum/README.md`
- `/home/iffi/VsCodec-Projects/Qortium/projects/Discssion-Boards/src/features/forum/README.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/discussion-boards-reference/docs/RELEASE.md`
- `/home/iffi/VsCodec-Projects/Qortium/projects/Discssion-Boards/docs/RELEASE.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/discussion-boards-reference/docs/QORTIUM-HOME-DISPLAY.md`
- `/home/iffi/VsCodec-Projects/Qortium/projects/Discssion-Boards/docs/QORTIUM-HOME-DISPLAY.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/discussion-boards-reference/docs/ARCHITECTURE-V2.md`
- `/home/iffi/VsCodec-Projects/Qortium/projects/Discssion-Boards/docs/ARCHITECTURE-V2.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/discussion-boards-reference/docs/QORTIUM-BRIDGE-PUBLICATION.md`
- `/home/iffi/VsCodec-Projects/Qortium/projects/Discssion-Boards/docs/QORTIUM-BRIDGE-PUBLICATION.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/discussion-boards-reference/docs/STARTUP-DIAGNOSTICS.md`
- `/home/iffi/VsCodec-Projects/Qortium/projects/Discssion-Boards/docs/STARTUP-DIAGNOSTICS.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/discussion-boards-reference/docs/DEPENDENCY-BASELINE.md`
- `/home/iffi/VsCodec-Projects/Qortium/projects/Discssion-Boards/docs/DEPENDENCY-BASELINE.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/discussion-boards-reference/docs/releases/ARCHITECTURE-V2-RC1.md`
- `/home/iffi/VsCodec-Projects/Qortium/projects/Discssion-Boards/docs/releases/ARCHITECTURE-V2-RC1.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/discussion-boards-reference/docs/migration/LEGACY-CANONICAL-PUBLISHER-REVIEW.md`
- `/home/iffi/VsCodec-Projects/Qortium/projects/Discssion-Boards/docs/migration/LEGACY-CANONICAL-PUBLISHER-REVIEW.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/discussion-boards-reference/docs/migration/HIGH-RISK-DECISION-SHEET.md`
- `/home/iffi/VsCodec-Projects/Qortium/projects/Discssion-Boards/docs/migration/HIGH-RISK-DECISION-SHEET.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/discussion-boards-reference/agents/runtime-diagnostics-and-performance.md`
- `/home/iffi/VsCodec-Projects/Qortium/qortium-dev-workspace/agents/runtime-diagnostics-and-performance.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/discussion-boards-reference/agents/issue-driven-audit-and-refactor.md`
- `/home/iffi/VsCodec-Projects/Qortium/qortium-dev-workspace/agents/issue-driven-audit-and-refactor.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/discussion-boards-reference/agents/git-generated-files-and-hygiene.md`
- `/home/iffi/VsCodec-Projects/Qortium/qortium-dev-workspace/agents/git-generated-files-and-hygiene.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/discussion-boards-reference/scripts/BACKUP-RESTORE.md`
- `/home/iffi/VsCodec-Projects/Qortium/projects/Discssion-Boards/scripts/BACKUP-RESTORE.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/README.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/README.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/src/v2/assets/marks/README.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/src/v2/assets/marks/README.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/src/v2/assets/marks/README.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/src/v2/assets/marks/README.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/QDN_PUBLIC_PUBLISHING.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/QDN_PUBLIC_PUBLISHING.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/HOME_DATA_MANAGERS.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/HOME_DATA_MANAGERS.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/HOME_V2_DISPLAY_SETTINGS_MIGRATION.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/HOME_V2_DISPLAY_SETTINGS_MIGRATION.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/HOME_V2_DISPLAY_SETTINGS_MIGRATION.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/HOME_V2_DISPLAY_SETTINGS_MIGRATION.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/REMOTE_MAC_BUILDS.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/REMOTE_MAC_BUILDS.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/REMOTE_MAC_BUILDS.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/REMOTE_MAC_BUILDS.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/QDN_WIDGETS.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/QDN_WIDGETS.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/HOME_V2_LIVE_NODE_APPIMAGE.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/HOME_V2_LIVE_NODE_APPIMAGE.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/HOME_V2_LIVE_NODE_APPIMAGE.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/HOME_V2_LIVE_NODE_APPIMAGE.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/APP_VERSIONING.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/APP_VERSIONING.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/HOME_SETTINGS_BRIDGE.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/HOME_SETTINGS_BRIDGE.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/CORE_MANAGEMENT.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/CORE_MANAGEMENT.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/HOME_V2_APP_NOTIFICATIONS.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/HOME_V2_APP_NOTIFICATIONS.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/COIN_SUPPORT_MATRIX.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/COIN_SUPPORT_MATRIX.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/PROVENANCE_LEDGER.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/PROVENANCE_LEDGER.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/PROVENANCE_LEDGER.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/PROVENANCE_LEDGER.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/HOME_CHAT_INTEROP_VECTORS.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/HOME_CHAT_INTEROP_VECTORS.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/HOME_CHAT_INTEROP_VECTORS.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/HOME_CHAT_INTEROP_VECTORS.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/HOME_CHAT_PORTABILITY_ROADMAP.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/HOME_CHAT_PORTABILITY_ROADMAP.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/HOME_CHAT_PORTABILITY_ROADMAP.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/APP_NOTIFICATIONS.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/APP_NOTIFICATIONS.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/HOME_APP_ASSIGNMENTS.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/HOME_APP_ASSIGNMENTS.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/OPEN_CURRENT_TAB.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/OPEN_CURRENT_TAB.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/QDN_RESOURCE_VIEWER.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/QDN_RESOURCE_VIEWER.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/CHAT_2_0_PLAN.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/CHAT_2_0_PLAN.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/CHAT_2_0_PLAN.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/CHAT_2_0_PLAN.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/HOME_CHAT_PRIVATE_ATTACHMENTS.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/HOME_CHAT_PRIVATE_ATTACHMENTS.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/HOME_CHAT_PRIVATE_ATTACHMENTS.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/HOME_CHAT_PRIVATE_ATTACHMENTS.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/HOME_V2_OPERATIONAL_COMPLETION.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/HOME_V2_OPERATIONAL_COMPLETION.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/HOME_V2_OPERATIONAL_COMPLETION.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/HOME_V2_FIXTURE_APPIMAGE.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/HOME_V2_FIXTURE_APPIMAGE.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/HOME_V2_FIXTURE_APPIMAGE.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/HOME_V2_FIXTURE_APPIMAGE.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/PROJECT_PLAN.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/PROJECT_PLAN.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/adr/0003-isolated-v2-fixture-appimage.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/adr/0003-isolated-v2-fixture-appimage.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/adr/0003-isolated-v2-fixture-appimage.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/adr/0003-isolated-v2-fixture-appimage.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/adr/0008-home-v2-public-identity-lookup.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/adr/0008-home-v2-public-identity-lookup.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/adr/0008-home-v2-public-identity-lookup.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/adr/0008-home-v2-public-identity-lookup.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/adr/0011-home-v2-production-account-shell.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/adr/0011-home-v2-production-account-shell.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/adr/0011-home-v2-production-account-shell.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/adr/0011-home-v2-production-account-shell.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/adr/0007-home-v2-node-readiness-and-android.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/adr/0007-home-v2-node-readiness-and-android.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/adr/0007-home-v2-node-readiness-and-android.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/adr/0007-home-v2-node-readiness-and-android.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/adr/0009-home-v2-read-only-account-catalogue.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/adr/0009-home-v2-read-only-account-catalogue.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/adr/0009-home-v2-read-only-account-catalogue.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/adr/0009-home-v2-read-only-account-catalogue.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/adr/0001-home-v2-foundation-boundaries.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/adr/0001-home-v2-foundation-boundaries.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/adr/0001-home-v2-foundation-boundaries.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/adr/0001-home-v2-foundation-boundaries.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/adr/0005-home-v2-live-node-preview.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/adr/0005-home-v2-live-node-preview.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/adr/0005-home-v2-live-node-preview.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/adr/0005-home-v2-live-node-preview.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/adr/0004-browser-shell-startup-and-theme.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/adr/0004-browser-shell-startup-and-theme.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/adr/0004-browser-shell-startup-and-theme.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/adr/0004-browser-shell-startup-and-theme.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/adr/0002-fixture-bridge-permission-model.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/adr/0002-fixture-bridge-permission-model.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/adr/0002-fixture-bridge-permission-model.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/adr/0002-fixture-bridge-permission-model.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/adr/0010-home-v2-persistent-shell-and-read-only-app-runtime.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/adr/0010-home-v2-persistent-shell-and-read-only-app-runtime.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/adr/0010-home-v2-persistent-shell-and-read-only-app-runtime.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/adr/0010-home-v2-persistent-shell-and-read-only-app-runtime.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/docs/adr/0006-qortium-public-node-endpoints.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/docs/adr/0006-qortium-public-node-endpoints.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/adr/0006-qortium-public-node-endpoints.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/adr/0006-qortium-public-node-endpoints.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-v2.0.0/scripts/fixtures/README.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home/scripts/fixtures/README.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/scripts/fixtures/README.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/scripts/fixtures/README.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/SECURITY.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/SECURITY.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/QDN_WIDGETS.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/QDN_WIDGETS.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/APP_VERSIONING.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/APP_VERSIONING.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/HOME_SETTINGS_BRIDGE.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/HOME_SETTINGS_BRIDGE.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/CORE_MANAGEMENT.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/CORE_MANAGEMENT.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/HOME_V2_APP_NOTIFICATIONS.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/HOME_V2_APP_NOTIFICATIONS.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/APP_NOTIFICATIONS.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/APP_NOTIFICATIONS.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/HOME_V2_IMAGE_CACHE.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/HOME_V2_IMAGE_CACHE.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/HOME_APP_ASSIGNMENTS.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/HOME_APP_ASSIGNMENTS.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/OPEN_CURRENT_TAB.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/OPEN_CURRENT_TAB.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/QDN_RESOURCE_VIEWER.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/QDN_RESOURCE_VIEWER.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/HOME_V2_CONTEXT_MENUS.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/HOME_V2_CONTEXT_MENUS.md`

- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-background-audio/docs/PROJECT_PLAN.md`
- `/home/iffi/VsCodec-Projects/Qortium/github-clones/qortium-home-auth-reference/docs/PROJECT_PLAN.md`
