# Install AI Agent Tool as an OpenClaw workspace

OpenClaw is an agent runtime, not a model. Copy all contents of this bundle into the active OpenClaw workspace, not an arbitrary project directory.

## Activate

1. Start a fresh OpenClaw session in this workspace. `BOOTSTRAP.md` will trigger the native one-time birth flow on the first real interaction.
2. To invoke it explicitly, use `@agents` where the channel passes the alias through.
3. Native fallbacks are `/skill agents` and `$agents` in interfaces that expose skill mentions.
4. After successful birth, OpenClaw deletes `BOOTSTRAP.md`; the `agents` skill remains for `status`, `doctor` and `reconfigure`.

The birth flow merges private-memory rules into the workspace `.gitignore` before storing personal values. Review the result before committing anything.

OpenClaw's workspace is not a hard sandbox and its sandbox may be disabled by default. Configure gateway sandbox, tool policy, approvals and channel allowlists separately. This bundle never enables broad permissions.
