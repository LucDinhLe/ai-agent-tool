# One-folder bootstrap for Claude Code

The user installed only the `.claude/` folder. This is intentional. Claude Code discovers the project skill, custom agent, and rule from that folder; the skill creates runtime files only after explicit activation.

## Source and destination

- Adapter source: the skill directory containing this file.
- Runtime payload: `assets/runtime/.ai-agent/` under that skill directory.
- Destination: the current project root.

Never read a similarly named payload from outside the current project. Never write outside the current project.

## Installation workflow

1. Resolve the project root and inspect `.ai-agent/`, `CLAUDE.md`, `.claude/rules/`, Git status, and existing identity or memory files.
2. Verify that the payload contains `BIRTH.md`, `STATE.md`, `SOUL.md`, `WORKSPACE.md`, `MEMORY_POLICY.md`, `VERSION`, `.gitignore`, and the private templates. Stop if the download is incomplete.
3. Create `.ai-agent/` from the payload.
   - When the destination is absent, copy the complete payload.
   - When it exists, add only missing AI Agent Tool files. Compare before changing any existing file and ask before replacing meaningful content.
   - Do not create `.ai-agent/private/` yet. The birth protocol creates it only when the selected memory mode allows it.
4. Do not create or overwrite root `CLAUDE.md`. Persistent routing already lives in `.claude/rules/ai-agent-tool.md`, which avoids colliding with project instructions.
5. Verify `.claude/agents/agents.md`, `.claude/rules/ai-agent-tool.md`, `.claude/skills/agent-birth/SKILL.md`, and the `/private/` ignore rule.
6. Continue immediately with `.ai-agent/BIRTH.md`; do not make the user invoke the skill a second time.

If a custom agent cannot ask the user for an unresolved identity choice or a consequential merge decision, return that concise question to the main Claude Code conversation. Never guess the answer in a subagent.
