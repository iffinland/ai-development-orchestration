# Implementation / handoff — qortal/qwb-qortal-web-builders/qwb-rc-7fd03fc-staging-confirmation-20260916

Executing agent (actual executor of the work): **DeepSeek**
Report/handoff writer (if different from the executing agent): same (`DeepSeek`)
Executing-agent evidence: the Hub session, the staging publish, the five runtime checks, the node
read-backs, every documentation edit and this record were produced by the **DeepSeek** model running
through the local Codex CLI profile (`CODEX_HOME=/home/iffi/.codex-deepseek`,
`model = "deepseek-flash"`, `model_provider = "deepseek"`); per `AI-Orchestration/GIT-AND-HANDOFF.md`
the CLI/orchestration profile is not the executor.

## Exact revisions

| Repository | Branch | Base | Head | Remote |
| --- | --- | --- | --- | --- |
| `git@github.com:iffinland/QWB-Qortal-Web-Builders.git` | `agent/qwb/phase-4-runtime-fix` | `7fd03fc5b2d39d80b20ccaa9c7a07355d85dc94a` | `7fd03fc5b2d39d80b20ccaa9c7a07355d85dc94a` (**unchanged — no source changed**) | unchanged |
| `git@github.com:iffinland/qortal-dev-workspace.git` | `agent/qwb-qortal-web-builders/phase-4-checkpoint-docs-20260916` | `8c16550b729a2c5cc858796c24ee4d35fc6f6a46` | see `STATUS.json` | pushed, `git ls-remote` verified |
| this repository | `agent/orchestration/qwb-rc-7fd03fc-staging-confirmation-20260916` | `1320e1648d4c18a50630b9db746b69f83c8b0e4d` | recorded in the final handoff after push | pushed |

`main` is at `18d760d011e956829714e7489432949829fa1840` in the application repository and at
`b8fd2f6fbfcff88c0ab9bc8fd116d5548679d2d2` (`origin/main`) in the workspace repository: untouched in
both. No merge, no force push, no history rewrite, no tag, no release.

## 1. Result — PASS

Five checks, all PASS, in Qortal Hub 3.0.3 against the real staging resource.

| Check | Result |
| --- | --- |
| existing synthetic QDN entities still render | PASS — all 3 active synthetic entities, the step with its 3 016 B thumbnail |
| untouched shipped seed items render beside them | PASS — 14 shipped items, none of whose identifiers is published |
| those items still expose the owner inline controls | PASS — 14 shipped rows, each `✎ / 🗑 / ↑ / ↓` |
| hard reload preserves both | PASS — identical counts and assertions after the Hub reload |
| no tombstoned item is resurrected | PASS — both tombstones filtered, titles absent from the DOM |

## 2. Staging publish

Published the `dist/` of `7fd03fc` (19 files, 879 170 B, sha256 `43244c21…67984cf7`) through the
Hub's own publish implementation — `window.sendMessage('publishOnQDN', …)` in the Hub renderer, which
backs the Hub's **Apps → My apps → Publish site** flow — so the transaction is signed by the Hub
wallet with no node API key.

| Item | Value |
| --- | --- |
| Resource | `WEBSITE / Q-Website / default` |
| Previous revision | `5qU9BKTp…cgb4i`, 880 160 B (build `741754b`) |
| New revision | `2egexP3JFzX5pkyVKkPrt9Pidcv9QWvcrvYoxCb8KDtmZa1iY76TUjd4CxLG128xUszoJV2rxKCmyza1gDFJ9sLd` |
| New size | 880 368 B (`properties` 1 210 698 B, 3 chunks, `READY`) |
| Transaction | `ARBITRARY`, block 2 725 989, fee 0.01000000 QORT, creator `QNwV9VV82UUZmMkDZZbEMAKPpCx7otnnsi` |

The first attempt was rejected by the node (`Finalize failed: Bad parameter "category"`, payload
carried `category: 'other'`) and retried without a category, matching the previous staging publish.

All 19 published files were fetched back through `/render/` and hashed against the local `dist/` of
`7fd03fc`: 18 byte-identical, `index.html` differing only by the node's `/render/` shell (injected
`<base>`, `_qdn*` variables, `q-apps.js`, an extra `<meta charset>`) and HTML re-serialisation. The
served application chunk is `assets/index-Cc7rTXmF.js`, sha256 `19c6ff71…0fcd6084`.

## 3. The defect also reproduced live

Staging was still serving the pre-fix build (`assets/index-BKwnLHC3.js`, sha256 `9e1ce7a1…863db27f`,
identical to the Phase 4 evidence), so the bounded run captured the defect in the real Hub rather than
only from source: build `741754b` rendered 0 highlights, 0 featured works, 0 prices, 2 services and
1 step, with only 3 owner item control rows and no `Add featured card`. The release candidate renders
2 / 3 / 2 / 6 / 4 and 17 item control rows.

## 4. Documentation

- `qortal-dev-workspace` `docs/qwb-qortal-web-builders/validation/2026-09-16-qwb-rc-7fd03fc-staging-confirmation.md`
  plus its evidence directory (30 checksummed artefacts, `sha256sum -c` clean).
- `…/implementations/2026-09-16-qwb-phase-4-checkpoint.md` — closure addendum marking checkpoint §6
  item 2 closed.
- `…/projects/qwb-qortal-web-builders.md` — status header, D9 row, QDN-identity section and the report
  index updated: release candidate `7fd03fc` confirmed on staging and **production-ready**.

## 5. A correction to the checkpoint's expected evidence

The checkpoint planned to read a `console.info('[qwb owner] bootstrap-defaults: …')` line. That
expectation was wrong: `bootstrap-defaults` is a **QDN source load-result** diagnostic, while the
console logging in `src/owner/shell.ts` only reports **control-mount** diagnostics. The baseline is
therefore evidenced by the rendered content plus the 404 probe of all shipped identifiers. Recorded so
the next agent does not go looking for a console line that does not exist.

## 6. Deliberately not done

No entity write of any kind (the only QDN write was the staging `WEBSITE` bundle); the Phase 4 §14
owner-runtime suite was not repeated; no automated gate was re-run because no source changed
(`git status` clean, HEAD unmoved, so the recorded `tsc --noEmit` / `eslint .` / `prettier --check .`
and 294 tests in 25 files still describe the tree); nothing was merged into `main`;
`WEBSITE / Qortal Web Builders / default` was read-only inspected (metadata identical to the Phase 4
record) and never written; no importer or migration was created.

## 7. Durable report link

`qortal-dev-workspace` on `agent/qwb-qortal-web-builders/phase-4-checkpoint-docs-20260916`:
`docs/qwb-qortal-web-builders/validation/2026-09-16-qwb-rc-7fd03fc-staging-confirmation.md` with its
evidence directory (all artefacts checksummed in `SHA256SUMS.txt`).
