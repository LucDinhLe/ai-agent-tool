# Install AI Agent Tool for Codex

The download contains exactly one install folder: `.agents/`.

1. Copy the whole `.agents/` folder into the project root. Do not open it and copy its internal files one by one.
2. If the project already has `.agents/`, choose the operating system option that merges folders. Do not replace the whole existing folder.
3. Start a new Codex session at the project root.

## Activate

- ChatGPT/Codex desktop app: type `@agents` and select **AI Agent Birth**.
- Codex CLI or IDE extension: type `$agents`, or run `/skills` and select `agents`.

The skill creates or safely merges `AGENTS.md` and `.ai-agent/` only after activation. It then inspects the project, asks the unresolved birth choices, creates the identity, and verifies the installation.

Useful maintenance calls:

- `@agents status`
- `@agents doctor`
- `@agents reconfigure`
- `@agents remember <fact>`
- `@agents forget <fact>`

AI Agent Tool changes project context and workflow. It does not retrain the model, grant tools, bypass approvals, or replace the Codex sandbox.
