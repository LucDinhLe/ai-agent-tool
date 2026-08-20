---
name: agent-birth
description: Bootstrap or maintain AI Agent Tool in a connected Cowork project. Use for birth, status, doctor, reconfigure, remember, or forget.
---

# Bootstrap or maintain the project agent

1. Identify the connected project folder selected by the user. Treat the directory containing this `SKILL.md` as the trusted adapter source, whether it came from the copied `AI-Agent-Tool/` folder or an enabled Cowork skill.
2. If `.ai-agent/BIRTH.md`, `.ai-agent/STATE.md`, or `AI-Agent-Tool/agents.md` is absent in the connected project folder, read `references/BOOTSTRAP.md` completely and run its additive installation or repair workflow first.
3. Read `.ai-agent/BIRTH.md` and `.ai-agent/STATE.md` completely.
4. Determine the requested mode. With no mode, use `init` when state is uninitialized and `status` when it is initialized.
5. Follow the matching protocol while keeping every write inside the connected project folder.
6. Preserve existing user content. Never replace meaningful content silently.
7. Never request, copy, print or store credentials. Keep portable private context under `.ai-agent/private/`.
8. Finish with the required birth card or doctor report.

An explicit invocation authorizes local setup in the connected folder only. It does not expand Cowork folder access or authorize external actions.
