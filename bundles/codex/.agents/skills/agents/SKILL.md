---
name: agents
description: Initialize, birth, inspect, repair, or reconfigure the portable AI Agent Tool for the current project. Use when the user invokes @agents or $agents, asks to create a persistent project agent identity, runs an agent doctor/status check, changes memory mode, or wants the project agent to remember or forget durable context. Do not use for ordinary project tasks unrelated to agent setup or maintenance.
---

# Initialize or maintain the agent

1. Read `.ai-agent/BIRTH.md` completely.
2. Read `.ai-agent/STATE.md` and determine the requested mode from the user's invocation.
3. Follow the matching workflow exactly. Use `init` when the state is uninitialized and no mode was supplied; use `status` when it is already initialized and no mode was supplied.
4. Keep all writes inside the current workspace. An explicit invocation authorizes local AI Agent Tool setup only, not external actions.
5. Preserve existing project instructions and user-authored content. Ask before replacing or discarding material information.
6. Never request, copy, print or store credentials. Keep private context under `.ai-agent/private/`.
7. Finish with the birth card or doctor report required by the protocol.

If `.ai-agent/BIRTH.md` is missing, stop and report that the bundle is incomplete. Do not invent a replacement protocol.
