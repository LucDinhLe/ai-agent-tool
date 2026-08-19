# Install AI Agent Tool for Claude Cowork

Claude Cowork does not currently document an automatically loaded project file equivalent to Claude Code's `CLAUDE.md`. One Project Instructions step is therefore required for a reliable `@agents` alias.

## Activate with a connected folder

1. Copy all contents of this bundle into a dedicated local working folder.
2. Create a Cowork Project from that existing folder, or connect the folder as project context.
3. Copy the contents of `COWORK-PROJECT-INSTRUCTIONS.txt` into the project's **Instructions** field.
4. Start a new task and type `@agents`.

## Optional account skill

The source under `cowork-skill/agent-birth/` can be zipped and uploaded at **Customize → Skills**. A prebuilt skill ZIP is attached to the GitHub release. After enabling it, invoke `/agent-birth` when the `@agents` alias is unavailable.

Cowork uses only folders you explicitly grant. Prefer a dedicated working folder and do not include secrets. AI Agent Tool does not expand Cowork permissions or replace its sandbox and confirmation prompts.
