# Platform support và nguồn chính thức

Kiểm tra gần nhất: **2026-08-19**.

AI Agent Tool đóng gói theo agent host/runtime, không theo tên model. Một host có thể đổi model mà vẫn dùng cùng convention; ngược lại, cùng một model trong host khác có thể đọc file khác.

## Mức hỗ trợ

- **Supported**: entry file và đường gọi native được tài liệu chính thức mô tả.
- **Supported with setup**: cần một bước UI được tài liệu chính thức hỗ trợ.
- **Runtime bundle**: dành cho active workspace của runtime, không phải project folder bất kỳ.
- **Portable alias**: `@agents` do AI Agent Tool định nghĩa; host có thể dành ký hiệu `@` cho chức năng khác.

## OpenAI Codex

Bundle: `codex/`.

- Codex tự đọc `AGENTS.md` theo phạm vi project và ưu tiên file gần working directory hơn.
- Repository skills nằm ở `.agents/skills/<name>/SKILL.md`.
- ChatGPT/Codex desktop dùng `@` để chọn skill; Codex CLI và IDE dùng `$` hoặc `/skills`.
- Sandbox, approvals và instructions là các lớp khác nhau.

Invocation: `@agents` trong desktop; `$agents` trong CLI/IDE.

Nguồn:

- [Customization overview](https://learn.chatgpt.com/docs/customization/overview)
- [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [Sandboxing](https://learn.chatgpt.com/docs/permissions/sandboxing)

## Claude Code

Bundle: `claude-code/`.

- Claude Code tự đọc `CLAUDE.md`; file có thể import bằng `@path`.
- Anthropic khuyên giữ `CLAUDE.md` ngắn và dùng `CLAUDE.local.md` cho preference cá nhân cục bộ.
- Project skills nằm ở `.claude/skills/<name>/SKILL.md` và gọi bằng `/skill-name`.
- `/agents` là built-in subagent manager, nên AI Agent Tool dùng `/agent-birth`.
- `@agents.md` là adapter ghép từ file mention chính thức và nội dung imperative; nó không phải command native tên `@agents`.

Invocation: mention `@agents.md`; fallback `/agent-birth`.

Nguồn:

- [Features overview](https://code.claude.com/docs/en/features-overview)
- [Manage Claude's memory](https://code.claude.com/docs/en/memory)
- [Extend Claude with skills](https://code.claude.com/docs/en/slash-commands)
- [Subagents](https://code.claude.com/docs/en/sub-agents)
- [Permissions](https://code.claude.com/docs/en/permissions)

## Claude Cowork

Bundle: `claude-cowork/`.

- Cowork Project có Instructions, Context và project memory trong UI.
- Cowork không đọc local `~/.claude/skills`; skill cần được bật trong tài khoản và upload qua Customize.
- Tài liệu hiện không cam kết Cowork tự nạp `CLAUDE.md`, `.claude/skills` hoặc một local `agents.md` chỉ vì folder được connect.
- Vì vậy bundle yêu cầu paste `COWORK-PROJECT-INSTRUCTIONS.txt` một lần. Đây là điều kiện để quảng cáo `@agents` một cách trung thực.

Invocation: `@agents` sau Project Instructions; fallback `/agent-birth` sau khi upload skill ZIP.

Nguồn:

- [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
- [Projects in Claude Cowork](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork)
- [Use Skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [Use plugins in Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)
- [Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)

## Gemini CLI

Bundle: `gemini-cli/`.

- `GEMINI.md` là project context file và hỗ trợ `@file` imports.
- Workspace skills nằm ở `.gemini/skills/` hoặc alias liên công cụ `.agents/skills/`.
- Custom subagents nằm ở `.gemini/agents/*.md`.
- `@subagent-name` ở đầu prompt là cú pháp chính thức để hướng tác vụ tới subagent.
- Project commands nằm ở `.gemini/commands/`; đường dẫn `ai-agent/init.toml` tạo `/ai-agent:init`.

Invocation: `@agents`; fallback `/ai-agent:init`.

Nguồn:

- [GEMINI.md project context](https://geminicli.com/docs/cli/gemini-md/)
- [Agent Skills](https://geminicli.com/docs/cli/skills/)
- [Subagents](https://geminicli.com/docs/core/subagents/)
- [Custom commands](https://geminicli.com/docs/cli/custom-commands/)
- [Trusted folders](https://geminicli.com/docs/cli/trusted-folders/)
- [Sandboxing](https://geminicli.com/docs/cli/sandbox/)

## GitHub Copilot

Bundle: `github-copilot/`.

- Repository-wide instructions nằm ở `.github/copilot-instructions.md`.
- Project skills có thể nằm ở `.github/skills`, `.agents/skills` hoặc `.claude/skills`.
- Custom agents cho CLI nằm ở `.github/agents/*.agent.md` và được chọn qua `/agent` hoặc `--agent`.
- GitHub không tài liệu hóa `@agents` như command native. Bundle giữ nó làm portable alias và dùng `/agent-birth` làm đường chính thức. Copilot CLI đã giữ `/agents` cho cấu hình subagents.

Invocation: `/agent-birth`; portable alias `@agents`; custom-agent fallback `/agent` → `ai-agent-tool`.

Nguồn:

- [Custom instructions support matrix](https://docs.github.com/en/copilot/reference/custom-instructions-support)
- [About agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)
- [Add skills to Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills)
- [Create custom agents for Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli)
- [Copilot CLI command reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference)
- [Cloud-agent risks and mitigations](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations)
- [Cloud and local sandboxes](https://docs.github.com/en/copilot/concepts/about-cloud-and-local-sandboxes)

## OpenClaw

Bundle: `openclaw/`.

- OpenClaw dùng workspace native với `AGENTS.md`, `SOUL.md`, `IDENTITY.md`, `USER.md`, `BOOTSTRAP.md`, `MEMORY.md`, `TOOLS.md` và dated memory.
- `BOOTSTRAP.md` là nghi thức một lần và được xóa sau khi birth thành công.
- OpenClaw tự bootstrap ở lượt thật đầu tiên; skill có thể gọi qua `/skill agents` hoặc `$agents` tùy interface.
- `@agents` là portable alias, không phải command native. Trên Discord, Slack hoặc Telegram, ký hiệu `@` còn có thể bị channel dùng cho mention.
- Workspace là working directory mặc định, không phải hard sandbox; sandbox gateway được cấu hình bên ngoài workspace.

Invocation: auto bootstrap; alias `@agents`; fallback `/skill agents` hoặc `$agents`.

Nguồn:

- [Agent runtime](https://docs.openclaw.ai/concepts/agent)
- [Agent bootstrapping](https://docs.openclaw.ai/start/bootstrapping)
- [Agent workspace](https://docs.openclaw.ai/agent-workspace)
- [Skills](https://docs.openclaw.ai/skills)
- [Slash commands](https://docs.openclaw.ai/slash-commands)
- [Sandboxing](https://docs.openclaw.ai/gateway/sandboxing)
- [Security](https://docs.openclaw.ai/gateway/security)

## Nền tảng chưa đóng gói

Google Antigravity 2.0 có rules, skills và custom agents trong `.agents/`, nhưng behavior giữa IDE và CLI vẫn khác nhau và Strict Mode có ảnh hưởng riêng tới file bị ignore. v2 ưu tiên Gemini CLI ổn định; Antigravity có thể được thêm khi adapter và privacy behavior được test độc lập.
