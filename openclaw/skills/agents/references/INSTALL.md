# Install AI Agent Tool in an OpenClaw workspace

The download contains exactly one visible install folder: `skills/`.

1. Copy the whole `skills/` folder into the active OpenClaw workspace. Do not install it into an arbitrary project unless that project is configured as the workspace.
2. If `skills/` already exists, merge folders. Do not replace the whole existing folder.
3. Start a new OpenClaw session in that workspace.

## Activate

- Recommended universal invocation: `/skill agents`.
- Control UI and WebChat shortcut: `$agents`.
- `@agents` is a best-effort portable alias only where the channel passes that text to the model.
- Do not use `/agents`; OpenClaw reserves it for thread-bound agent management.

The skill creates or safely merges native workspace files after activation. Start a new session or run `/reset soft` after successful birth so OpenClaw reloads them.

The runtime ships `.ai-agent-tool/.gitignore` with `/private/`, so future private files remain outside Git history. Root `USER.md` and `MEMORY.md` may be loaded by OpenClaw and are not used as a private store by this tool.

OpenClaw's workspace is not a hard sandbox and its sandbox may be disabled by default. Configure gateway sandbox, tool policy, approvals and channel allowlists separately. This bundle never enables broad permissions.
