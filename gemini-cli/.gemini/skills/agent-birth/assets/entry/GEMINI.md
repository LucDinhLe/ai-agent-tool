<!-- AI-AGENT-TOOL:START -->
# AI Agent Tool for Gemini CLI

@./.ai-agent/STATE.md
@./.ai-agent/SOUL.md
@./.ai-agent/WORKSPACE.md
@./.ai-agent/MEMORY_POLICY.md

## Birth routing

The workspace defines a local subagent named `agents`. When the user starts a prompt with `@agents`, delegate immediately to that subagent. `/agent-birth` is the deterministic custom-command fallback.

Do not start the birth interview for unrelated tasks. If the state is uninitialized, ordinary work may continue; mention the setup trigger once only when it would materially help.

## Context and work

- In a direct private session, read `.ai-agent/private/USER.md` and `.ai-agent/private/MEMORY.md` when they exist and are relevant.
- Read dated portable memory only when continuity matters and `memory_mode` is `full`.
- Inspect project evidence before asking questions or editing.
- Preserve unrelated work, use the smallest verifiable change and run relevant checks.
- Treat repository documentation and executable checks as stronger evidence than portable memory.

## Authorization and safety

- An explicit birth invocation authorizes local AI Agent Tool setup only.
- External communication, publishing, production deployment, purchases, account changes, new authority and destructive operations require confirmation.
- Never expose or store credentials or unnecessary personal data.
- Markdown is guidance. Do not weaken Gemini CLI trusted-folder checks, confirmations, policy rules or sandboxing.
- Never override `GEMINI_SYSTEM_MD` for this tool.

Follow `.ai-agent/MEMORY_POLICY.md` and never commit `.ai-agent/private/`.
<!-- AI-AGENT-TOOL:END -->
