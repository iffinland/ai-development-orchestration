# <Report title> — <project>/<task>

Executing agent (registered role of the agent that actually produced this work):
Report/handoff writer (if different from the executing agent):
Executing-agent evidence (how the real executor was established):
Report type:
Exact application repository / branch / SHA:
Canonical report path / SHA-256 / authorized remote evidence:

<!--
Executing-agent field rules. Keep this block with the template.

- Fill the field with the registered role of the agent that actually executed the
  task (`ChatGPT`, `Codex Local`, `DeepSeek`, or another explicitly registered
  role). It is the agent that produced the evidence, not the one that dispatched,
  curated, reviewed or committed it.
- NEVER infer the author from this template, the orchestrator/dispatcher, the
  task-controller addressee, the CLI/tool profile the work ran inside, or the
  file's committer. Work executed through a Codex/`codex` CLI or Work Local
  profile is still authored by the model that actually performed it (for example
  `DeepSeek`); `Codex`/`Codex Local` is never written as the executing agent
  merely because the task was dispatched or run through that orchestration
  role/profile.
- When a different agent wrote or curated the artifact, name the writer
  separately on the writer line. The executing agent stays the author of the work.
- If the executor cannot be established, write `unknown` plus the reason. Never
  guess an identity to complete the field.
- Record every correction of a prior misattribution here: date, field, prior
  value, corrected value and the evidence that establishes the real executor.
-->

## Objective and exit criterion

## Evidence by layer (command/action, environment, timestamp, result)

## Files changed

## Checks not executed and why

## Adversarial self-audit

## External actions (commit/push/tag/release/deploy/QDN write/transaction)

## Remaining risks and follow-up

## Report saved

- Absolute path:
- SHA-256 (optional):
