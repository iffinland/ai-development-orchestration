# Git and durable handoff

Each task names an application repository, a verified base SHA and a unique
`agent/<project>/<task>` branch. Keep owner dirty checkouts intact; use a separate
worktree under `/home/iffi/VsCodec-Projects` when isolation is needed. Never force
push, rewrite shared history, update parent gitlinks or bundle unrelated changes.

A task records exact commit/push permission for both the application branch and
handoff repository/branch. Designing this workflow does not grant blanket push
permission. Reuse already-given authorization; do not ask again. Without it,
prepare local artifacts and state `handoff_sync = pending_authorization`.
Main/default-branch merge/push, tags, releases, deployment, QDN writes, signing,
transactions and issue mutation require their own explicit scope authorization.

Durable exchange, once a GitHub remote and branch permissions are configured:
1. Store `tasks/<project>/<task>/TASK.md`, `STATUS.json`, `IMPLEMENTATION.md` and
   `AUDIT.md` in this orchestration repository on the task branch. Create only
   artifacts that actually exist; start from `templates/`. TASK/STATUS record
   the exact skills loaded and their freshness result.
2. Push authorized application changes first; verify the remote branch SHA.
3. The current writer updates STATUS with that exact application SHA, evidence
   and next actor. Commit and push handoff artifacts; verify their remote SHA.
4. The receiving agent fetches and reads the exact handoff commit and exact
   application SHA. Verify task ID, expected prior revision/state and evidence
   before claiming work. A changed application SHA invalidates prior review.
5. Codex Local is the single handoff-state writer/coordinator. DeepSeek submits
   implementation evidence; Codex records the transition. Do not concurrently
   update STATUS. A stale/conflicting update requires re-read and reconciliation,
   never force push. Resume idempotently from task ID + application SHA + state.
6. Before the terminal handoff, record capability harvest: exact skills created
   or updated, their maturity, or an explicit project-specific/no-harvest result.
   A skill update is orchestration knowledge, not authorization to change or
   publish the application.

States: `planned -> implementing -> review_pending -> owner_validation_pending
-> complete`. Review may return `changes_required -> implementing`. Any active
state may become `blocked`, with reason, missing evidence and resume condition.
`review_pending` means reviewable, not product-ready. `complete` requires all
TASK acceptance checks, required live/host evidence and owner acceptance.
If owner acceptance is not applicable (e.g. a documentation-only task), record
that reason in TASK. Do not use READY/COMPLETE to hide an unexecuted workflow.

GitHub stores evidence; it does not start agents. No background polling,
notification service, API agent runner or scheduled job is installed by phase 1.
Dispatch requires a separately verified local DeepSeek client and an authorized
run. If unavailable, record a blocker; do not silently substitute a costly model.

Detailed platform reports remain canonical at their platform report root.
Handoff artifacts contain a concise summary, exact source revision and a durable
remote report link when available. For local-only Qortium reports, publish an
explicitly approved, sanitized evidence snapshot in the handoff; record its local
source and SHA-256. A local path alone is not a GitHub-readable handoff.
Never include credentials, wallet data, secrets or private infrastructure details.
