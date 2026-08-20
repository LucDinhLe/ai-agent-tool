# AI Agent Tool birth entrypoint

An explicit mention of this file means the user wants to initialize or maintain the project agent.

Read `.ai-agent/BIRTH.md` completely, read `.ai-agent/STATE.md`, infer the requested mode from any text after the mention, and execute that mode. With no mode, use `init` for an uninitialized state and `status` for an initialized state.

Keep writes inside the workspace. Preserve existing project instructions and user content. Never request or store credentials.
