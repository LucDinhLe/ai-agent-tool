# Install AI Agent Tool for GitHub Copilot

The download contains exactly one install folder: `.github/`.

1. Copy the whole `.github/` folder into the repository root. Do not open it and copy its internal files one by one.
2. If the repository already has `.github/`, merge folders. Do not replace the whole existing folder.
3. Reload Copilot or start a new Copilot CLI or IDE session.

## Activate

- Recommended: run `/agent-birth`.
- Fallback: run `/agent`, choose `ai-agent-tool`, then request initialization.
- `@agents` remains a best-effort portable alias only where the interface passes that literal text to the model. GitHub does not document it as a native repository-agent command.

The adapter creates `.ai-agent/` only after activation. It uses a unique scoped instruction file and does not overwrite `.github/copilot-instructions.md`.

Useful calls include `/agent-birth doctor`, `/agent-birth reconfigure` and `/agent-birth remember <fact>`.

Copilot CLI reserves `/agents` for subagent configuration, so this bundle deliberately avoids that name.

AI Agent Tool does not replace Copilot's permissions, GitHub Actions firewall, human PR review or optional local sandbox.
