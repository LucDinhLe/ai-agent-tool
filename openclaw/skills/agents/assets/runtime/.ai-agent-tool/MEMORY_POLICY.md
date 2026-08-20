# Memory policy

## Modes

- `off`: do not read or write private portable memory.
- `minimal`: keep only explicit preferences and durable verified decisions in `.ai-agent-tool/private/MEMORY.md`.
- `full`: use curated private memory plus selective `.ai-agent-tool/private/memory/YYYY-MM-DD.md` notes.

Default to `minimal`. Record the selected mode in `.ai-agent-tool/STATE.md`.

## Allowed content

Record explicit preferences, verified decisions, active state not maintained elsewhere, and lessons from confirmed corrections. Never record credentials, unnecessary personal details, guesses as facts or full transcripts.

Use one item per fact:

```text
- [active] Fact or decision. Source: user|file|test. Verified: YYYY-MM-DD. Review: YYYY-MM-DD|when-condition.
```

Use `[inference]`, `[unverified]`, `[superseded]` or `[expired]` when appropriate. Current explicit user statements and verified project files override older memory.

On a forget request, remove matching entries from curated and dated memory when safe. Explain that Git history, backups, native runtime memory or external copies may require separate cleanup.

Keep private runtime memory out of public Git history. The shipped `.ai-agent-tool/.gitignore` must contain `/private/` before writing personal values.

OpenClaw may inject root `USER.md` and `MEMORY.md` into session context. AI Agent Tool therefore never uses those root files as a private store. Preserve pre-existing root files, warn when they contain sensitive content, and propose redaction or migration only with confirmation.
