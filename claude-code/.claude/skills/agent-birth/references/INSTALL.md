# Install AI Agent Tool for Claude Code

The download contains exactly one install folder: `.claude/`.

1. Copy the whole `.claude/` folder into the project root. Do not open it and copy its internal files one by one.
2. If the project already has `.claude/`, choose the operating system option that merges folders. Do not replace the whole existing folder.
3. Start a new Claude Code session at the project root.

## Activate

- Type `@agents` and select `agents (agent)` from typeahead.
- Exact typed fallback: `@agent-agents`.
- Stable skill fallback: `/agent-birth`.

The skill creates `.ai-agent/` only after activation. It does not overwrite root `CLAUDE.md`; the adapter uses a unique project rule under `.claude/rules/`.

Useful calls include `/agent-birth status`, `/agent-birth doctor`, `/agent-birth reconfigure`, and `/agent-birth remember <fact>`.

Claude Code reserves `/agents` for managing subagents. AI Agent Tool does not replace permissions, hooks, or sandboxing.
