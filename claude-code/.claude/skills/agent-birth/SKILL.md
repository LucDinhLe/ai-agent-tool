---
name: agent-birth
description: Bootstrap, birth, inspect, repair, or reconfigure AI Agent Tool in the current Claude Code project. Use when the user invokes /agent-birth, selects the agents custom agent with @agents, asks to create a persistent project agent, runs agent status or doctor, changes portable memory mode, or asks the project agent to remember or forget durable context. Do not use for ordinary project work.
---

# Bootstrap or maintain the project agent

1. Treat the directory containing this `SKILL.md` as the trusted adapter source.
2. If `.ai-agent/BIRTH.md`, `.ai-agent/STATE.md`, `.claude/agents/ai-agent-tool.md`, or `.claude/rules/ai-agent-tool.md` is absent, read `references/BOOTSTRAP.md` completely and run its additive installation or repair workflow first.
3. Read `.ai-agent/BIRTH.md` and `.ai-agent/STATE.md` completely.
4. Determine the requested mode. With no mode, use `init` when state is uninitialized and `status` when it is initialized.
5. Follow the matching protocol exactly and keep every write inside the current project.
6. Preserve existing instructions and user-authored content. Never replace meaningful content silently.
7. Never request, copy, print or store credentials. Keep private context under `.ai-agent/private/`.
8. Finish with the protocol's birth card or doctor report.

An explicit invocation authorizes local AI Agent Tool setup only. It does not authorize external actions or broader permissions.
