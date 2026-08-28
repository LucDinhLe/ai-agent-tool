# Platform support và nguồn chính thức

Kiểm tra gần nhất: **2026-08-20**.

AI Agent Tool đóng gói theo agent host/runtime, không theo tên model. Một host có thể đổi model mà vẫn dùng cùng convention; ngược lại, cùng một model trong host khác có thể đọc file khác.

## Mức hỗ trợ

- **Supported**: entry file và đường gọi native được tài liệu chính thức mô tả.
- **Supported with setup**: cần một bước UI được tài liệu chính thức hỗ trợ.
- **Runtime bundle**: dành cho active workspace của runtime, không phải project folder bất kỳ.
- **Portable alias**: `@agents` do AI Agent Tool định nghĩa; host có thể dành ký hiệu `@` cho chức năng khác.

## OpenAI Codex

Install folder: `.agents/` trong `AI-Agent-Tool-Codex.zip`.

- Codex tự đọc `AGENTS.md` theo phạm vi project và ưu tiên file gần working directory hơn.
- Repository skills nằm ở `.agents/skills/<name>/SKILL.md`. Đây là toàn bộ folder người dùng cần copy.
- ChatGPT/Codex desktop dùng `@` để chọn skill; Codex CLI và IDE dùng `$` hoặc `/skills`.
- Sandbox, approvals và instructions là các lớp khác nhau.

Invocation: `@agents` trong desktop; `$agents` trong CLI/IDE. Sau lần gọi đầu, skill tạo hoặc merge `AGENTS.md` và `.ai-agent/`.

Nguồn:

- [Customization overview](https://learn.chatgpt.com/docs/customization/overview)
- [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [Sandboxing](https://learn.chatgpt.com/docs/permissions/sandboxing)

## Claude Code

Install folder: `.claude/` trong `AI-Agent-Tool-Claude-Code.zip`.

- Claude Code tự đọc `CLAUDE.md`, `.claude/rules/`, `.claude/agents/` và `.claude/skills/` theo convention tương ứng.
- Bundle dùng file riêng `.claude/rules/ai-agent-tool.md` để không ghi đè `CLAUDE.md` đang có.
- Project skills nằm ở `.claude/skills/<name>/SKILL.md` và gọi bằng `/skill-name`.
- `/agents` là built-in subagent manager, nên AI Agent Tool dùng `/agent-birth`.
- Gõ `@agents` rồi chọn `agents (agent)` trong typeahead. Anthropic tài liệu hóa cú pháp nhập tay chính xác là `@agent-agents`.

Invocation: chọn custom agent từ `@agents`; exact fallback `@agent-agents`; skill fallback `/agent-birth`.

Nguồn:

- [Features overview](https://code.claude.com/docs/en/features-overview)
- [Manage Claude's memory](https://code.claude.com/docs/en/memory)
- [Extend Claude with skills](https://code.claude.com/docs/en/slash-commands)
- [Subagents](https://code.claude.com/docs/en/sub-agents)
- [Permissions](https://code.claude.com/docs/en/permissions)

## Claude Cowork

Install folder: `khai-sinh/` trong `AI-Agent-Tool-Claude-Cowork.zip`.

Claude Cowork là nền tảng duy nhất trong sáu không dùng kiến trúc skill + `.ai-agent/` runtime chung. Đây là quyết định có chủ đích, không phải phần thiếu:

- Cowork Project có Instructions, Context và project memory trong UI, nhưng tài liệu hiện không cam kết tự nạp `CLAUDE.md`, local skill hay một `agents.md` chỉ vì folder được connect.
- Cowork không đọc local `~/.claude/skills`; upload skill qua Customize là luồng riêng cho tài khoản, không phải cho một project folder cụ thể. Vì bundle này gắn với một project cụ thể của một người dùng, `khai-sinh/` bỏ hẳn lớp skill và dùng file Markdown thuần ở root, agent tự đọc theo thứ tự cố định trong `CLAUDE.md`.
- Bundle yêu cầu paste `khai-sinh/COWORK-PROJECT-INSTRUCTIONS.txt` vào Project Instructions một lần. Đây là điều kiện để `CLAUDE.md` chắc chắn được đọc đầu mỗi phiên, kể cả phiên chạy theo lịch.
- Danh tính, người dùng, bài toán và ký ức chắt lọc nằm trực tiếp ở `IDENTITY.md`, `USER.md`, `PROJECT.md`, `MEMORY.md` tại root, không có lớp `.ai-agent/private/`. Trạng thái làm việc trong phiên dùng project memory của chính Cowork thay vì một file `STATE.md` portable.

Invocation: không có alias `@agents`. Sau khi paste Project Instructions, mở phiên mới và gõ đại ý "bắt đầu đi"; agent thấy `BOOTSTRAP.md` còn trong thư mục sẽ tự dẫn qua nghi thức khai sinh.

Nguồn:

- [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
- [Projects in Claude Cowork](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork)
- [Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)

## Gemini CLI

Install folder: `.gemini/` trong `AI-Agent-Tool-Gemini-CLI.zip`.

- `GEMINI.md` là project context file và hỗ trợ `@file` imports.
- Workspace skills nằm ở `.gemini/skills/`. Bundle dùng vị trí này để toàn bộ cài đặt nằm trong một folder.
- Custom subagents nằm ở `.gemini/agents/*.md`.
- `@subagent-name` ở đầu prompt là cú pháp chính thức để hướng tác vụ tới subagent.
- Project commands nằm ở `.gemini/commands/`; file `agent-birth.toml` tạo `/agent-birth`.

Invocation: `@agents`; fallback `/agent-birth`.

Nguồn:

- [GEMINI.md project context](https://geminicli.com/docs/cli/gemini-md/)
- [Agent Skills](https://geminicli.com/docs/cli/skills/)
- [Subagents](https://geminicli.com/docs/core/subagents/)
- [Custom commands](https://geminicli.com/docs/cli/custom-commands/)
- [Trusted folders](https://geminicli.com/docs/cli/trusted-folders/)
- [Sandboxing](https://geminicli.com/docs/cli/sandbox/)

## GitHub Copilot

Install folder: `.github/` trong `AI-Agent-Tool-GitHub-Copilot.zip`.

- Repository instructions có thể nằm ở file riêng `.github/instructions/*.instructions.md` với `applyTo`. Bundle dùng tên riêng để tránh ghi đè `.github/copilot-instructions.md`.
- Project skills có thể nằm ở `.github/skills`, `.agents/skills` hoặc `.claude/skills`.
- Custom agents cho CLI nằm ở `.github/agents/*.agent.md` và được chọn qua `/agent` hoặc `--agent`.
- GitHub không tài liệu hóa `@agents` như command native. Bundle giữ nó làm portable alias và dùng `/agent-birth` làm đường chính thức. Copilot CLI đã giữ `/agents` cho cấu hình subagents.

Invocation: `/agent-birth`; custom-agent fallback `/agent` → `ai-agent-tool`; portable alias `@agents` chỉ best-effort.

Nguồn:

- [Custom instructions support matrix](https://docs.github.com/en/copilot/reference/custom-instructions-support)
- [About agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)
- [Add skills to Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills)
- [Create custom agents for Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli)
- [Copilot CLI command reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference)
- [Cloud-agent risks and mitigations](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations)
- [Cloud and local sandboxes](https://docs.github.com/en/copilot/concepts/about-cloud-and-local-sandboxes)

## OpenClaw

Install folder: `skills/` trong `AI-Agent-Tool-OpenClaw.zip`.

- OpenClaw ưu tiên workspace skill tại `<workspace>/skills/`. Người dùng chỉ copy folder này; skill tạo hoặc merge các file native sau khi được gọi.
- AI Agent Tool tạo hoặc merge các file shared native `AGENTS.md`, `SOUL.md`, `IDENTITY.md` và `PROJECT.md`. Root `USER.md` và `MEMORY.md` có thể bị OpenClaw tự nạp, nên tool giữ dữ liệu riêng dưới `.ai-agent-tool/private/` và không tạo hai root file này làm kho private.
- `HEARTBEAT.md` đã bị loại khỏi template workspace mới. Tool notes nên nằm trong `## Tools` của `AGENTS.md`; v2.1 không tạo `TOOLS.md` hoặc `BOOTSTRAP.md` mặc định.
- `@agents` là portable alias, không phải command native. Trên Discord, Slack hoặc Telegram, ký hiệu `@` còn có thể bị channel dùng cho mention.
- Workspace là working directory mặc định, không phải hard sandbox; sandbox gateway được cấu hình bên ngoài workspace.

Invocation: `/skill agents` trên mọi bề mặt; `$agents` trong Control UI/WebChat; alias `@agents` chỉ best-effort. `/agents` là built-in khác.

Nguồn:

- [Agent runtime](https://docs.openclaw.ai/concepts/agent)
- [Agent workspace](https://docs.openclaw.ai/concepts/agent-workspace)
- [Skills](https://docs.openclaw.ai/tools/skills)
- [Slash commands](https://docs.openclaw.ai/tools/slash-commands)
- [Retired HEARTBEAT.md](https://docs.openclaw.ai/reference/templates/HEARTBEAT)
- [Sandboxing](https://docs.openclaw.ai/gateway/sandboxing)
- [Security](https://docs.openclaw.ai/gateway/security)

## Nền tảng chưa đóng gói

Google Antigravity 2.0 có rules, skills và custom agents trong `.agents/`, nhưng behavior giữa IDE và CLI vẫn khác nhau và Strict Mode có ảnh hưởng riêng tới file bị ignore. v2 ưu tiên Gemini CLI ổn định; Antigravity có thể được thêm khi adapter và privacy behavior được test độc lập.
