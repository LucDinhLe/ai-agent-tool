# Install AI Agent Tool for GitHub Copilot

Copy all contents of this folder, including `.github/` and `.ai-agent/`, into the repository root. If `.github/copilot-instructions.md` already exists, merge the AI Agent Tool sections instead of overwriting project instructions.

## Activate

1. Reload Copilot or start a new Copilot CLI/IDE session at the repository root.
2. Run the native project skill `/agent-birth`.
3. You may type `@agents` where the host passes that literal text through to Copilot. It is a portable alias, not a GitHub-native command.
4. Fallback: run `/agent`, choose `ai-agent-tool`, then request initialization.

Useful calls include `/agent-birth doctor`, `/agent-birth reconfigure` and `/agent-birth remember <fact>`.

Copilot CLI reserves `/agents` for subagent configuration, so this bundle deliberately avoids that name.

AI Agent Tool does not replace Copilot's permissions, GitHub Actions firewall, human PR review or optional local sandbox.
