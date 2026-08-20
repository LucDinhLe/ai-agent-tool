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

1. Confirm this is the active OpenClaw workspace. Read `AGENTS.md`, `.ai-agent-tool/STATE.md`, `SOUL.md`, `IDENTITY.md`, `PROJECT.md`, and the memory policy. Detect any root `USER.md`, `MEMORY.md`, or `memory/` content and treat it as potentially session-injected, not private.
2. Inspect the workspace and version-control status. Detect existing native files and plan a merge.
3. Before writing personal values, verify `.ai-agent-tool/.gitignore` exists and contains `/private/`. This nested rule protects future Git repositories too. If Git is available, confirm it with `git check-ignore` without staging anything.
4. Infer safe project facts. Ask one concise batch only for unresolved choices: agent name and role, optional private address/language/timezone, collaboration style, main workspace outcome, confirmation boundaries and memory mode.
5. Show a compact proposal. Ask before replacing meaningful existing identity or memory content. A clean template plus explicit answers needs no redundant confirmation.
6. Update `IDENTITY.md`, `SOUL.md`, `PROJECT.md`, and `.ai-agent-tool/STATE.md`. For `minimal` or `full`, create `.ai-agent-tool/private/` from `.ai-agent-tool/templates/private/` only after the ignore rule is active, and fill only confirmed useful fields. For `off`, do not create private files. Never create or update root `USER.md`, `MEMORY.md`, or `memory/` as a private store.
7. Verify required files, initialized state, ignore behavior, and absence of likely credentials. Confirm that `.ai-agent-tool/.gitignore` protects the full private subtree. Warn if pre-existing root bootstrap files contain sensitive data and offer a confirmed migration or redaction plan.
8. Return a birth card with name, role, workspace outcome, memory mode, confirmation boundaries, changed files, verification result, the reload instruction, and three useful next prompts.

## Doctor

Check native entry files, state, privacy ignore rules, memory-policy consistency, unresolved placeholders, and skill discovery. Classify findings as `pass`, `warning`, or `fail`. Apply repairs only after `doctor --fix` or confirmation when user content could change.

## Reconfigure and memory

Change only requested fields. When memory mode changes to `off`, ask whether existing memory should be retained unread, archived locally or removed. Never assume deletion. Report the limits of forget operations.
