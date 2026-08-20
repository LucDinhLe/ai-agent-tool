---
name: agent-birth
description: Initialize, birth, inspect, repair, or reconfigure AI Agent Tool in the current GitHub Copilot project. Use when the user invokes /agent-birth or the @agents portable alias, asks for a persistent project agent identity, runs an agent doctor/status check, changes portable memory mode, or asks the project agent to remember or forget durable context. Do not use for ordinary project tasks.
---

# Initialize or maintain the agent

1. Read `.ai-agent/BIRTH.md` and `.ai-agent/STATE.md` completely.
2. Determine the requested mode. Default to `init` when uninitialized and `status` when initialized.
3. Follow the protocol exactly. Keep writes inside the current repository.
4. Preserve existing instructions and user content. Ask before discarding material information.
5. Never request, copy, print or store credentials. Keep portable private context under `.ai-agent/private/`.
6. Finish with the required birth card or doctor report.

If the protocol is missing, report an incomplete bundle and stop.
