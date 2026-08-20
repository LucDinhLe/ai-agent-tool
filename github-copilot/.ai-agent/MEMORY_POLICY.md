# Memory policy

## Purpose

Portable memory preserves useful continuity across sessions and agent hosts. It is not a transcript, credential store or substitute for project documentation or native host memory.

## Modes

- `off`: do not create or read portable private memory.
- `minimal`: keep only explicit preferences and durable verified decisions in `private/MEMORY.md`.
- `full`: use curated memory plus selective dated notes when recent continuity is useful.

The selected mode is recorded in `.ai-agent/STATE.md`. Default to `minimal` when the user does not choose.

## Storage

- `private/MEMORY.md` contains a short curated index of durable facts and decisions.
- `private/memory/YYYY-MM-DD.md` contains selective dated notes in `full` mode.
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

Current explicit user statements and verified project sources override older portable memory. Mark the old entry as superseded and describe the replacement. Never silently preserve both as active.

When the user asks to forget something, remove it from curated and dated portable memory when safe and report what was removed. Git history, backups, native host memory and external copies may require separate cleanup.

## Maintenance

- Prefer updating an existing entry over adding a duplicate.
- Keep curated memory short enough to scan.
- Review stale items when their review date or condition is reached.
- Do not commit the `private/` directory. `.ai-agent/.gitignore` provides the default guard.
