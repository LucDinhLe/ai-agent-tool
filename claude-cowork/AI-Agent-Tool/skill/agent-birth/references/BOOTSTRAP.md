# One-folder bootstrap for Claude Cowork

The project bundle contains one visible folder named `AI-Agent-Tool/`. Cowork does not document automatic discovery of local `.claude/` project skills or an `@agents` command, so the copied-folder flow requires the supplied Project Instructions once.

## Source and destination

- Adapter source: the skill directory containing this file.
- Runtime payload: `assets/runtime/.ai-agent/` under that skill directory.
- Destination: the connected project or working folder the user explicitly granted to Cowork.

Never write outside the connected folder. Never widen folder permissions.

## Installation workflow

1. Confirm the connected folder that will own the project agent and inspect `.ai-agent/`, project instructions visible in context, and any existing identity or memory files.
2. Verify that the payload contains `BIRTH.md`, `STATE.md`, `SOUL.md`, `WORKSPACE.md`, `MEMORY_POLICY.md`, `VERSION`, `.gitignore`, and the private templates. Stop if the package is incomplete.
3. Create `.ai-agent/` from the payload. Copy the complete payload when absent; otherwise add only missing files and ask before replacing meaningful content. Do not create `.ai-agent/private/` before memory mode is chosen.
4. Do not claim that local files changed Cowork account settings. If the supplied Project Instructions are not active, tell the user to paste `AI-Agent-Tool/COWORK-PROJECT-INSTRUCTIONS.txt` into the project's Instructions field once.
5. Continue immediately with `.ai-agent/BIRTH.md`; do not make the user invoke the skill twice.

Cowork permissions and sandboxing remain the technical boundary. Markdown files are project guidance only.
