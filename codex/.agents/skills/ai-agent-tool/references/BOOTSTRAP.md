# One-folder bootstrap for Codex

The user installed only the `.agents/` folder. This is intentional. The adapter creates the runtime files after the user explicitly invokes `@agents` or `$agents`.

## Source and destination

- Adapter source: the skill directory containing this file.
- Runtime payload: `assets/runtime/.ai-agent/` under that skill directory.
- Codex entry template: `assets/entry/AGENTS.md` under that skill directory.
- Destination: the current project root.

Never read a similarly named payload from outside the current project. Never write outside the current project.

## Installation workflow

1. Resolve the current project root. Prefer the Git root; otherwise use the current working directory.
2. Inspect `AGENTS.md`, `.ai-agent/`, Git status, and any existing agent identity or memory files before writing.
3. Verify that the payload contains `BIRTH.md`, `STATE.md`, `SOUL.md`, `WORKSPACE.md`, `MEMORY_POLICY.md`, `VERSION`, `.gitignore`, and the private templates. If any required source is missing, stop and report an incomplete download.
4. Create `.ai-agent/` from the payload.
   - When the destination is absent, copy the complete payload.
   - When it already exists, add only missing AI Agent Tool files. Compare before changing any existing file and ask before replacing meaningful content.
   - Do not create `.ai-agent/private/` yet. The birth protocol creates it only when the selected memory mode allows it.
5. Install the Codex entry.
   - When root `AGENTS.md` is absent, create it from the entry template.
   - When it exists and has no AI Agent Tool marker, append the complete marked block after its existing content.
   - When the marker already exists, preserve the existing block during ordinary initialization. Update only that marked block during an explicit upgrade or doctor fix.
   - Never replace unrelated instructions.
6. Verify that Codex can still discover this skill at `.agents/skills/ai-agent-tool/SKILL.md` and that `.ai-agent/.gitignore` ignores `/private/`.
7. Continue immediately with `.ai-agent/BIRTH.md`. Do not make the user invoke the skill a second time.

## Managed marker

The entry template uses these exact boundaries:

```text
<!-- AI-AGENT-TOOL:START -->
<!-- AI-AGENT-TOOL:END -->
```

Only content inside those boundaries belongs to AI Agent Tool. Content outside them belongs to the project owner.
