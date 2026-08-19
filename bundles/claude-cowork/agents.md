# AI Agent Tool birth entrypoint for Claude Cowork

When the project instructions route an explicit `@agents` invocation here, read `.ai-agent/BIRTH.md` completely and read `.ai-agent/STATE.md`.

Infer the requested mode from text after `@agents`. With no mode, use `init` for an uninitialized state and `status` for an initialized state.

Keep writes inside the connected project folder. Preserve existing user content. Never request or store credentials. Follow Cowork's folder permissions and confirmation prompts.
