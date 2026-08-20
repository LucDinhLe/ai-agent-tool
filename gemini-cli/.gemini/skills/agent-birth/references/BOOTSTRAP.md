# One-folder bootstrap for Gemini CLI

The user installed only the `.gemini/` folder. This is intentional. Gemini CLI discovers the custom subagent, command, and workspace skill from that folder; the skill creates runtime files only after activation.

## Source and destination

- Adapter source: the skill directory containing this file.
- Runtime payload: `assets/runtime/.ai-agent/` under that skill directory.
- Gemini entry template: `assets/entry/GEMINI.md` under that skill directory.
- Destination: the current workspace root.

Never read a similarly named payload from outside the current workspace. Never write outside the current workspace.

## Installation workflow

1. Resolve the workspace root and inspect `GEMINI.md`, `.ai-agent/`, Git status, and existing identity or memory files.
2. Verify that the payload contains `BIRTH.md`, `STATE.md`, `SOUL.md`, `WORKSPACE.md`, `MEMORY_POLICY.md`, `VERSION`, `.gitignore`, and the private templates. Stop if the download is incomplete.
3. Create `.ai-agent/` from the payload. Copy the complete payload when absent; otherwise add only missing files and ask before replacing meaningful content. Do not create `.ai-agent/private/` before memory mode is chosen.
4. Install the Gemini entry.
   - When root `GEMINI.md` is absent, create it from the entry template.
   - When it exists without AI Agent Tool markers, append the complete marked block after existing content.
   - When markers already exist, preserve the block during ordinary initialization. Update only the marked block during an explicit upgrade or doctor fix.
   - Never replace unrelated project context.
5. Verify `.gemini/agents/ai-agent-tool.md`, `.gemini/commands/agent-birth.toml`, `.gemini/skills/agent-birth/SKILL.md`, and the `/private/` ignore rule.
6. Continue immediately with `.ai-agent/BIRTH.md`; do not make the user invoke the skill twice.

After changing `GEMINI.md`, request `/memory reload` when the current Gemini CLI session cannot see the new context.
