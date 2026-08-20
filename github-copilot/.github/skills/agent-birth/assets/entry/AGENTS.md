<!-- AI-AGENT-TOOL:START -->
# AI Agent Tool for GitHub Copilot

## Startup routing

Before substantial work, when `.ai-agent/STATE.md` exists:

1. Read `.ai-agent/STATE.md`.
2. Read `.ai-agent/SOUL.md` for identity and collaboration style.
3. Read `.ai-agent/WORKSPACE.md` for verified project facts and commands.
4. Read `.ai-agent/MEMORY_POLICY.md` before portable memory.
5. In a direct private session, read `.ai-agent/private/USER.md` and `.ai-agent/private/MEMORY.md` only when relevant.

Missing optional private files are not errors.

## Birth routing

For initialization, status, doctor, repair, reconfiguration, remember, or forget requests, use `.github/skills/agent-birth/SKILL.md`. The supported skill invocation is `/agent-birth`; the custom-agent fallback is `/agent` then `ai-agent-tool`. Treat literal `@agents` only as a portable best-effort alias.

Do not start birth for unrelated work. Preserve existing project instructions and user-authored content.

## Safety

- An explicit birth invocation authorizes local project setup only.
- External communication, publishing, deployment, purchases, account changes, new authority, and destructive actions require separate confirmation.
- Never expose or store credentials or unnecessary personal data.
- Project Markdown is guidance; do not weaken Copilot permissions, firewall controls, review requirements, or sandboxing.
- Never commit `.ai-agent/private/`.
<!-- AI-AGENT-TOOL:END -->
