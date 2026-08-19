# Install AI Agent Tool for Gemini CLI

Copy all contents of this folder, including `.gemini/`, `.agents/` and `.ai-agent/`, into the project root. If `GEMINI.md` already exists, merge the AI Agent Tool sections instead of overwriting existing context.

## Activate

1. Trust the project folder in Gemini CLI.
2. Start a new session at the project root, or run `/memory reload`, `/commands reload` and verify `/skills list`.
3. Start a prompt with `@agents`. This targets the bundled `agents` subagent using Gemini CLI's official `@subagent` syntax.
4. Use `/ai-agent:init` if subagent forcing is unavailable.

Useful calls include `@agents doctor`, `@agents reconfigure` and `/ai-agent:init remember <fact>`.

Do not use YOLO mode for setup. AI Agent Tool does not replace trusted-folder checks, tool confirmations, policy rules or `gemini -s` sandboxing.
