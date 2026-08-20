---
name: agents
description: Bootstrap or maintain AI Agent Tool in the active OpenClaw workspace. Use for birth, status, doctor, reconfigure, remember, or forget.
---

# Bootstrap or maintain the OpenClaw workspace agent

1. Treat `{baseDir}` as the trusted adapter source inside the active workspace.
2. If `.ai-agent-tool/BIRTH.md`, `.ai-agent-tool/STATE.md`, the marked AI Agent Tool block in root `AGENTS.md`, `SOUL.md`, `IDENTITY.md`, or `PROJECT.md` is absent, read `{baseDir}/references/BOOTSTRAP.md` completely and run its additive installation or repair workflow first.
3. Read `.ai-agent-tool/BIRTH.md` and `.ai-agent-tool/STATE.md` completely.
4. Determine the requested mode. With no mode, use `init` when state is uninitialized and `status` when it is initialized.
5. Follow the matching protocol exactly and keep every write inside the active workspace.
6. Preserve existing native files and user content. Never replace meaningful content silently.
7. Never request, copy, print, or store credentials.
8. Finish with the required birth card or doctor report.

Use `/skill agents` as the universal invocation. `$agents` is an explicit shortcut in Control UI and WebChat. Treat `@agents` only as a best-effort portable alias when that literal text reaches the model. `/agents` is an OpenClaw built-in and is not the birth command.
