---
name: agents
description: Initialize, inspect, repair or reconfigure the portable AI Agent Tool identity and memory system for this workspace.
kind: local
max_turns: 30
---

Read `.ai-agent/BIRTH.md` and `.ai-agent/STATE.md` completely. Infer the requested mode from the user's text after `@agents`. With no mode, use `init` when uninitialized and `status` when initialized.

Follow the protocol exactly. Keep all writes inside the workspace, preserve existing user content and never request or store credentials. Finish with the required birth card or doctor report.

If the protocol is missing, report an incomplete bundle and stop.
