# Install AI Agent Tool for Claude Code

Copy all contents of this folder, including `.claude/` and `.ai-agent/`, into the project root. If `CLAUDE.md` already exists, merge the AI Agent Tool sections instead of overwriting existing instructions.

## Activate

1. Start a new Claude Code session at the project root.
2. Type `@agents` and select the root `agents.md` file from autocomplete. `@agents.md` is the unambiguous form.
3. If file mention is unavailable, run the native project skill `/agent-birth`.
4. Answer the short birth proposal. Claude will inspect the project, write the confirmed identity and verify the installation.

Useful calls include `@agents.md status`, `@agents.md doctor`, `/agent-birth reconfigure`, and `/agent-birth remember <fact>`.

Claude Code reserves `/agents` for managing subagents. AI Agent Tool does not replace permissions, hooks or sandboxing.
