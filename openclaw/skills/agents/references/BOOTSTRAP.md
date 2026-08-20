# One-folder bootstrap for OpenClaw

The user installed one visible folder named `skills/` in the active OpenClaw workspace. This is intentional. The `agents` skill creates or merges native workspace files only after explicit activation.

## Source and destination

- Adapter source: `{baseDir}`.
- Runtime payload: `{baseDir}/assets/runtime/.ai-agent-tool/`.
- Native templates: `{baseDir}/assets/native/`.
- Destination: the active OpenClaw workspace root.

Do not install into an arbitrary project unless it is configured as the active OpenClaw workspace. Never write outside that workspace or modify `~/.openclaw` runtime state.

## Installation workflow

1. Confirm the active workspace and writable workspace access. Inspect existing `AGENTS.md`, `SOUL.md`, `IDENTITY.md`, `USER.md`, `PROJECT.md`, `MEMORY.md`, `memory/`, and `.ai-agent-tool/` before writing. Root `USER.md` and `MEMORY.md` may be auto-loaded by OpenClaw, so never assume they are private.
2. Verify the runtime payload, its `.gitignore`, private templates, and native shared templates are complete. Stop and report an incomplete download when a required source is missing.
3. Create `.ai-agent-tool/` from the runtime payload. When it exists, add only missing files and ask before replacing meaningful content.
4. Install the native shared files.
   - Merge the marked AI Agent Tool block from the `AGENTS.md` template into root `AGENTS.md`; never replace unrelated instructions.
   - Create `SOUL.md`, `IDENTITY.md`, and `PROJECT.md` from templates only when absent. Preserve meaningful existing files and let the birth protocol propose bounded updates.
   - Preserve any existing root `USER.md`, `MEMORY.md`, and `memory/`; never use them as a new private store.
   - Keep new personal context only under `.ai-agent-tool/private/`, after verifying `.ai-agent-tool/.gitignore` contains `/private/`.
   - Do not create `TOOLS.md`; non-secret tool notes belong in the `## Tools` section of `AGENTS.md`.
   - Preserve an existing optional `HEARTBEAT.md`, but do not create it automatically. Do not create an automatic `BOOTSTRAP.md`.
5. Continue immediately with `.ai-agent-tool/BIRTH.md`; do not make the user invoke the skill twice.

After a successful birth, tell the user to start a new session or run `/reset soft` so OpenClaw reloads the new workspace files.
