# Memory policy

## Purpose

Memory preserves useful continuity. It is not a transcript, credential store or substitute for project documentation.

## Storage

- `private/MEMORY.md` contains a short curated index of durable facts and decisions.
- `private/memory/YYYY-MM-DD.md` contains selective daily notes.
- `WORKSPACE.md` remains the source of truth for shared project facts.

## What to record

- Explicit user preferences that affect future work.
- Verified decisions, their rationale and current status.
- Active project state that is not already maintained elsewhere.
- Lessons from confirmed failures or corrections.

Do not record secrets, authentication data, unnecessary personal details, guesses presented as facts or complete conversation transcripts.

## Entry format

Use one item per fact:

```text
- [active] Fact or decision. Source: user|file|test. Verified: YYYY-MM-DD. Review: YYYY-MM-DD|when-condition.
```

Use `[inference]`, `[unverified]`, `[superseded]` or `[expired]` when appropriate.

## Conflict and correction

Current explicit user statements and verified project sources override older memory. Mark the old entry as superseded and link or describe the replacement. Never silently preserve both as active.

When the user asks to forget something, remove it from curated and daily memory when safe and report what was removed. Git history, backups and external copies may require separate cleanup.

## Maintenance

- Prefer updating an existing entry over adding a duplicate.
- Keep curated memory short enough to scan.
- Review stale items when their review date or condition is reached.
- Do not commit the `private/` directory.
