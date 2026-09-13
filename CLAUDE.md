# Claude Code adapter

@AGENTS.md
@WORKFLOW.md
@skills/README.md

Claude is not currently an active required agent in this workflow. This file is
kept intentionally thin so future Claude Code adoption does not fork the shared
rules or capability library.

When Claude is enabled:

1. use the same canonical platform workspaces, project contexts and `skills/`
   library as ChatGPT, Codex and DeepSeek;
2. add only the minimum Claude discovery adapter required by the then-current
   Claude Code version (for example a `.claude/skills` link to the canonical
   library if supported);
3. do not copy skills into a second Claude-owned knowledge tree;
4. add a Claude role overlay only when Claude receives a real workflow role and
   that role differs materially from an existing one.
