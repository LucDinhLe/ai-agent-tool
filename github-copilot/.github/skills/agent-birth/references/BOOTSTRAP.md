# One-folder bootstrap for GitHub Copilot

The user installed only the `.github/` folder. This is intentional. Copilot discovers the repository skill, custom agent, and path-scoped adapter from that folder; the skill creates runtime files and the repository-wide `AGENTS.md` entry only after activation.

## Source and destination

- Adapter source: the skill directory containing this file.
- Runtime payload: `assets/runtime/.ai-agent/` under that skill directory.
- Repository entry template: `assets/entry/AGENTS.md` under that skill directory.
- Destination: the current repository root.

Never read a similarly named payload from outside the current repository. Never write outside the repository.

## Installation workflow

1. Resolve the repository root and inspect `.ai-agent/`, `.github/`, `AGENTS.md`, Git status, and existing identity or memory files.
2. Verify that the payload contains `BIRTH.md`, `STATE.md`, `SOUL.md`, `WORKSPACE.md`, `MEMORY_POLICY.md`, `VERSION`, `.gitignore`, and the private templates. Verify the marked `AGENTS.md` entry template too. Stop if the download is incomplete.
3. Create `.ai-agent/` from the payload. Copy the complete payload when absent; otherwise add only missing files and ask before replacing meaningful content. Do not create `.ai-agent/private/` before memory mode is chosen.
4. Install the repository-wide entry.
   - When root `AGENTS.md` is absent, create it from the entry template.
   - When it exists without the AI Agent Tool marker, append the complete marked block after existing content.
   - When a balanced marker block already exists, preserve it during ordinary initialization. Replace only that block during an explicit upgrade or doctor fix.
   - Never replace instructions outside the managed markers.
5. Do not create or overwrite `.github/copilot-instructions.md`. The unique `.github/instructions/ai-agent-tool.instructions.md` is only a path-scoped adapter; persistent startup routing comes from root `AGENTS.md`.
6. Verify root `AGENTS.md`, `.github/agents/ai-agent-tool.agent.md`, `.github/instructions/ai-agent-tool.instructions.md`, `.github/skills/agent-birth/SKILL.md`, and the `/private/` ignore rule.
7. Continue immediately with `.ai-agent/BIRTH.md`; do not make the user invoke the skill twice.

## Managed marker

Only content between these exact boundaries belongs to AI Agent Tool:

```text
<!-- AI-AGENT-TOOL:START -->
<!-- AI-AGENT-TOOL:END -->
```
