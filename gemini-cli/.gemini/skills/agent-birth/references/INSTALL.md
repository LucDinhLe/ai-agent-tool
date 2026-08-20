# Install AI Agent Tool for Gemini CLI

The download contains exactly one install folder: `.gemini/`.

1. Copy the whole `.gemini/` folder into the workspace root. Do not open it and copy its internal files one by one.
2. If the workspace already has `.gemini/`, merge folders. Do not replace the whole existing folder.
3. Trust the workspace and start a new Gemini CLI session.

## Activate

- Start a prompt with `@agents`. This uses Gemini CLI's official custom-subagent syntax.
- Use `/agent-birth` as the fallback.
- If files were copied into an open session, run `/agents reload`, `/commands reload`, and `/skills reload` first.

The adapter creates or safely merges `GEMINI.md` and `.ai-agent/` only after activation. Run `/memory reload` if the current session does not see the generated context.

Useful calls include `@agents doctor`, `@agents reconfigure`, and `/agent-birth remember <fact>`.

Do not use YOLO mode for setup. AI Agent Tool does not replace trusted-folder checks, tool confirmations, policy rules or `gemini -s` sandboxing.
