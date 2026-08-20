---
name: agents
description: Bootstrap, birth, inspect, repair, or reconfigure AI Agent Tool in the current Codex project. Use when the user invokes @agents in the desktop app or $agents in Codex CLI or IDE, asks to create a persistent project agent, runs agent status or doctor, changes portable memory mode, or asks the project agent to remember or forget durable context. Do not use for ordinary project work.
---

# Bootstrap or maintain the project agent

1. Treat the directory containing this `SKILL.md` as the trusted adapter source. Do not search for another copy outside the current project.
2. If `.ai-agent/BIRTH.md`, `.ai-agent/STATE.md`, or the marked AI Agent Tool block in root `AGENTS.md` is absent, read `references/BOOTSTRAP.md` completely and run its additive installation or repair workflow first.
3. Read `.ai-agent/BIRTH.md` and `.ai-agent/STATE.md` completely.
4. Determine the requested mode from the user's invocation. With no mode, use `init` when state is uninitialized and `status` when it is initialized.
5. Follow the matching protocol exactly. Keep every write inside the current project.
6. Preserve existing project instructions and user-authored content. Never replace meaningful content silently.
7. Never request, copy, print or store credentials. Keep private context under `.ai-agent/private/`.
8. Finish with the birth card or doctor report required by the protocol.

An explicit invocation authorizes local AI Agent Tool setup only. It does not authorize publishing, deployment, external communication, purchases, account changes, destructive operations, or broader permissions.
