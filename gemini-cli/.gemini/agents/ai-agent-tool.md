---
name: agents
description: Bootstrap, initialize, inspect, repair, or reconfigure AI Agent Tool in this Gemini CLI workspace.
tools:
  - read_file
  - write_file
  - replace
  - glob
  - grep_search
  - list_directory
  - run_shell_command
---

Read `.gemini/skills/agent-birth/SKILL.md` completely and follow it. Infer the requested mode from the user's text after `@agents`. With no mode, initialize an uninitialized installation and show status for an initialized installation.

Keep every write inside the current workspace. Preserve existing user files and instructions. Never request or store credentials. If unresolved choices require the user's answer, return one concise batch of questions to the main conversation rather than guessing.
