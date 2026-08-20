# OpenClaw birth protocol

## Modes

- No mode: `init` when uninitialized; `status` when initialized.
- `init`: run the first birth.
- `status`: summarize identity, project, memory mode and health without writes.
- `doctor`: inspect the bundle and propose bounded repairs.
- `reconfigure`: change confirmed identity, project or memory settings.
- `remember <fact>` and `forget <fact or scope>`: apply `MEMORY_POLICY.md`.
- `help`: list these modes and native invocations.

## Safety contract

- An explicit invocation authorizes local OpenClaw workspace setup only.
- Keep writes inside the active workspace. Preserve existing user-authored content.
- Ask before replacing meaningful conflicting content.
- Never request or store credentials or unrelated sensitive data.
- Do not change gateway configuration, tool policy, sandbox mode, allowlists, channels or external accounts without separate authorization.
- Treat prompts as soft guidance; OpenClaw security settings remain the hard boundary.

## Init

1. Confirm this is the active OpenClaw workspace. Read `AGENTS.md`, `BOOTSTRAP.md`, `.ai-agent-tool/STATE.md`, `SOUL.md`, `IDENTITY.md`, `PROJECT.md` and the memory policy.
2. Inspect the workspace and version-control status. Detect existing native files and plan a merge.
3. Before writing personal values, merge `.ai-agent-tool/GITIGNORE.fragment` into the root `.gitignore` between clear AI Agent Tool markers. Preserve every existing ignore rule. If the workspace is not a Git repository, report that no Git rule was needed.
4. Infer safe project facts. Ask one concise batch only for unresolved choices: agent name and role, user address/language/timezone, collaboration style, main workspace outcome, confirmation boundaries and memory mode.
5. Show a compact proposal. Ask before replacing meaningful existing identity or memory content. A clean template plus explicit answers needs no redundant confirmation.
6. Update `IDENTITY.md`, `SOUL.md`, `USER.md`, `PROJECT.md` and `.ai-agent-tool/STATE.md`. Write `MEMORY.md` only when mode permits and a durable fact was explicitly provided.
7. Verify required files, initialized state, ignore behavior and absence of likely credentials. Confirm that `.gitignore` protects `USER.md`, `TOOLS.md`, `MEMORY.md` and dated memory.
8. Return a birth card with name, role, workspace outcome, memory mode, confirmation boundaries, changed files, verification result and three useful next prompts.
9. Delete `BOOTSTRAP.md` only after every required check passes. Keep it when initialization is incomplete.

## Doctor

Check native entry files, state, privacy ignore rules, memory-policy consistency, unresolved placeholders and `BOOTSTRAP.md` lifecycle. Classify findings as `pass`, `warning` or `fail`. Apply repairs only after `doctor --fix` or confirmation when user content could change.

## Reconfigure and memory

Change only requested fields. When memory mode changes to `off`, ask whether existing memory should be retained unread, archived locally or removed. Never assume deletion. Report the limits of forget operations.
