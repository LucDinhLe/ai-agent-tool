# Install AI Agent Tool for Codex

This folder is a complete Codex adapter. Copy all of its contents, including `.agents/` and `.ai-agent/`, into the root of the target project.

If the project already has `AGENTS.md`, merge the AI Agent Tool sections instead of overwriting existing project instructions.

## Activate

1. Open a new Codex session at the project root.
2. In the ChatGPT/Codex desktop app, type `@agents` and select the **AI Agent Birth** skill.
3. In Codex CLI or the IDE extension, type `$agents` or run `/skills` and select `agents`.
4. Answer the short birth proposal. The agent will inspect the project, create its identity and verify the installation.

Useful maintenance calls:

- `@agents status`
- `@agents doctor`
- `@agents reconfigure`
- `@agents remember <fact>`
- `@agents forget <fact>`

AI Agent Tool changes project context and workflow. It does not retrain the model, grant tools, bypass approvals or replace the Codex sandbox.
