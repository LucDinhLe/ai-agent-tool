---
name: agent-birth
description: Initialize, birth, inspect, repair, or reconfigure AI Agent Tool in the current Claude Code project. Use when the user invokes /agent-birth, mentions @agents.md, asks to create a persistent project agent identity, runs an agent doctor/status check, changes portable memory mode, or asks the agent to remember or forget durable context. Do not use for ordinary project tasks.
---

# Initialize or maintain the agent

1. Read `.ai-agent/BIRTH.md` completely.
2. Read `.ai-agent/STATE.md` and determine the requested mode.
3. Follow the matching workflow exactly. Default to `init` when uninitialized and `status` when initialized.
4. Keep all writes inside the workspace. This invocation does not authorize external actions.
5. Preserve existing instructions and user-authored content. Ask before discarding material information.
6. Never request, copy, print or store credentials. Keep private context under `.ai-agent/private/`.
7. Finish with the protocol's birth card or doctor report.

If `.ai-agent/BIRTH.md` is missing, report an incomplete bundle and stop.
