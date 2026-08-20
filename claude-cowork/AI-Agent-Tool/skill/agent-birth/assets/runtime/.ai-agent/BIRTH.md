# Agent birth protocol

This file is the portable source of truth for initializing and maintaining AI Agent Tool. Platform entry files and skills route here.

## Invocation modes

- `@agents` with uninitialized state: run `init`.
- `@agents` with initialized state: run `status`.
- `@agents init`: initialize an uninitialized installation.
- `@agents status`: summarize identity, project context, memory mode and health without changing files.
- `@agents doctor`: validate the installation and propose bounded repairs.
- `@agents reconfigure`: change identity, collaboration preferences, project facts or memory mode.
- `@agents remember <fact>`: store an allowed durable fact under the current memory policy.
- `@agents forget <fact or scope>`: remove matching portable memory and report what was removed.
- `@agents help`: list these modes and the platform-native fallback command.

Equivalent platform-native invocations select the same modes.

## Safety contract

- Treat an explicit invocation as permission to inspect the workspace and edit AI Agent Tool files locally.
- Do not publish, send, deploy, purchase, alter external accounts or expand permissions without separate user authorization.
- Inspect before editing. Preserve existing instructions, project work and user-authored sections.
- If a destination file already contains meaningful content that conflicts with the proposal, show the conflict and ask before replacing it.
- Never request or store passwords, API keys, tokens, cookies, private keys, recovery codes, OTPs or unrelated sensitive data.
- Explain that Markdown instructions are soft guidance. Host permissions, sandboxing, hooks, policies and approvals remain the technical boundary.
- Keep personal context under `.ai-agent/private/`. Do not stage or commit that directory.

## Init workflow

### 1. Preflight

1. Resolve the project or workspace root.
2. Read the platform entry file, `.ai-agent/STATE.md`, `SOUL.md`, `WORKSPACE.md` and `MEMORY_POLICY.md`.
3. Inspect the project README, manifest, important directories and version-control status when available. Use this only to infer project facts.
4. Detect existing AI instruction, memory or identity files. Plan a merge; never silently overwrite them.
5. If the state is already initialized, switch to `status` unless the user explicitly requested `reconfigure`.

### 2. Build the birth proposal

Infer safe project facts from files. Ask one concise batch for only the unresolved choices:

1. Agent name, or permission to propose one.
2. Agent role and the main outcome it should optimize.
3. How to address the user, preferred language and timezone when useful.
4. Desired collaboration style and response depth.
5. Project purpose, intended users and current priority if the repository does not make them clear.
6. Boundaries that require confirmation, especially publishing, production, spending, external communication and destructive operations.
7. Portable memory mode: `off`, `minimal` or `full`.

Offer sensible defaults. Do not force the user to answer fields that can be verified from the project or that do not affect future work.

### 3. Confirm consequential choices

Show a compact proposal containing identity, role, project outcome, working style, confirmation boundaries, memory mode and files to be changed. Ask for confirmation before replacing existing meaningful content. For a clean template with explicit answers, proceed without a redundant confirmation.

### 4. Write the installation

1. Update `.ai-agent/SOUL.md` with the confirmed identity and behavior. Remove the uninitialized notice.
2. Update `.ai-agent/WORKSPACE.md` with verified facts only. Mark uncertain claims as unverified or leave them empty.
3. Set `.ai-agent/STATE.md` to `initialized`; record the ISO date, current platform and memory mode. Do not put personal facts in state.
4. For `minimal` or `full`, create `.ai-agent/private/` from `.ai-agent/templates/private/` and fill only confirmed useful fields. For `off`, do not create private memory files.
5. Add one curated memory entry only when the user explicitly supplied a durable fact or decision. Create a dated note only in `full` mode and only when the session produced durable context.
6. Preserve unknown sections and comments in files that already existed.

### 5. Verify

Check all of the following:

- Required entry, state, identity, workspace, policy, protocol and skill files exist.
- State is parseable and required initialized fields are present.
- No unresolved placeholder remains in an initialized identity or required workspace field.
- `.ai-agent/private/` is ignored by `.ai-agent/.gitignore`; if Git is available, verify with `git check-ignore` without staging anything.
- No likely credential was written.
- The platform can discover its entrypoint and native fallback.

Repair only bounded AI Agent Tool defects. Report project-level conflicts separately.

### 6. Return the birth card

Report:

- Agent name and role.
- Project outcome.
- Memory mode.
- Confirmation boundaries.
- Files created or changed.
- Verification result.
- Three useful next prompts tailored to the project.

## Doctor workflow

1. Run the verification checklist without changing files.
2. Classify findings as `pass`, `warning` or `fail`.
3. Explain the smallest repair and whether it changes user content.
4. Apply safe mechanical repairs only after the user invokes `@agents doctor --fix` or confirms the proposal.

## Reconfigure, remember and forget

- Change only the requested fields and preserve history that is still accurate.
- Apply the precedence and entry schema in `MEMORY_POLICY.md`.
- When memory mode changes to `off`, ask whether existing portable memory should be retained unread, archived locally or removed. Do not assume deletion.
- On forget requests, remove matching entries from curated and dated portable memory when safe, then explain that Git history, backups or native host memory may require separate cleanup.
