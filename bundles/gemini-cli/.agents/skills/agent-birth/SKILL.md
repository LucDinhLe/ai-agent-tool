---
name: agent-birth
description: Initialize, birth, inspect, repair, or reconfigure AI Agent Tool in the current Gemini CLI workspace. Use for persistent project agent identity, agent doctor/status checks, portable memory-mode changes, or remember/forget requests. The @agents subagent and /ai-agent:init command are the explicit entrypoints. Do not use for ordinary project tasks.
---

# Initialize or maintain the agent

1. Read `.ai-agent/BIRTH.md` and `.ai-agent/STATE.md` completely.
2. Determine the requested mode. Default to `init` when uninitialized and `status` when initialized.
3. Follow the protocol exactly and keep writes inside the workspace.
4. Preserve existing user content. Ask before discarding material information.
5. Never request, copy, print or store credentials. Keep portable private context under `.ai-agent/private/`.
6. Finish with the required birth card or doctor report.

If the protocol is missing, report an incomplete bundle and stop.
