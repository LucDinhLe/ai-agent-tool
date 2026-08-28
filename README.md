# AI Agent Tool

**Tải đúng nền tảng → giải nén → dán đúng một folder vào dự án → kích hoạt → agent tự khai sinh.**

AI Agent Tool là lớp khởi tạo mã nguồn mở cho các AI agent phổ biến. Nó không thay model và không “tăng IQ” bằng phép màu. Nó giúp model dùng năng lực sẵn có ổn định hơn nhờ danh tính rõ, bối cảnh dự án có cấu trúc, workflow lặp lại được, memory có kiểm soát và bước tự kiểm tra.

> English: AI Agent Tool is a one-folder project bootstrap for persistent, auditable agent identity, context, workflow, and optional memory.

## Bộ file này giúp người dùng làm gì?

- Khởi tạo một project agent bằng một lời gọi thay vì tự tạo và điền nhiều file cấu hình.
- Giữ vai trò, cách hợp tác và mục tiêu dự án ổn định giữa các phiên làm việc.
- Giúp AI tìm đúng tài liệu, lệnh setup, lệnh kiểm thử và tiêu chí hoàn thành của dự án.
- Giảm việc phải nhắc lại preference, quyết định và bối cảnh đã xác minh.
- Tách memory riêng tư khỏi file chia sẻ, có chế độ `off`, `minimal` và `full`.
- Kiểm tra cài đặt bằng doctor workflow và báo rõ phần thiếu, xung đột hoặc cần người dùng xác nhận.

AI vẫn hoạt động khi không có bộ file này. Người dùng sẽ phải tự cung cấp lại bối cảnh thường xuyên hơn, còn agent dễ đoán sai phạm vi, quên quyết định và làm việc thiếu nhất quán giữa các phiên.

## Tải đúng một gói

Không dùng **Code → Download ZIP** để cài. Nút đó tải mã nguồn dành cho nhà phát triển.

| Công cụ đang dùng | Tải trực tiếp | Sau khi giải nén, chỉ có | Kích hoạt |
|---|---|---|---|
| OpenAI Codex | [AI-Agent-Tool-Codex.zip](https://github.com/LucDinhLe/ai-agent-tool/releases/latest/download/AI-Agent-Tool-Codex.zip) | `.agents/` | `@agents` trong desktop, `$agents` trong CLI/IDE |
| Claude Code | [AI-Agent-Tool-Claude-Code.zip](https://github.com/LucDinhLe/ai-agent-tool/releases/latest/download/AI-Agent-Tool-Claude-Code.zip) | `.claude/` | gõ `@agents` rồi chọn `agents (agent)`, hoặc `/agent-birth` |
| Claude Cowork | [AI-Agent-Tool-Claude-Cowork.zip](https://github.com/LucDinhLe/ai-agent-tool/releases/latest/download/AI-Agent-Tool-Claude-Cowork.zip) | `khai-sinh/` | dán Project Instructions một lần, mở phiên mới và gõ "bắt đầu đi" |
| Gemini CLI | [AI-Agent-Tool-Gemini-CLI.zip](https://github.com/LucDinhLe/ai-agent-tool/releases/latest/download/AI-Agent-Tool-Gemini-CLI.zip) | `.gemini/` | `@agents`, dự phòng `/agent-birth` |
| GitHub Copilot | [AI-Agent-Tool-GitHub-Copilot.zip](https://github.com/LucDinhLe/ai-agent-tool/releases/latest/download/AI-Agent-Tool-GitHub-Copilot.zip) | `.github/` | `/agent-birth` |
| OpenClaw | [AI-Agent-Tool-OpenClaw.zip](https://github.com/LucDinhLe/ai-agent-tool/releases/latest/download/AI-Agent-Tool-OpenClaw.zip) | `skills/` | `/skill agents`; `$agents` trong Control UI/WebChat |

Mỗi link trên là một gói cài độc lập. Trong tài liệu này, **root dự án** nghĩa là **folder chính của dự án** mà AI đang mở.

## Cài trong bốn bước

1. Tải đúng ZIP theo công cụ AI đang dùng.
2. Giải nén. Bên trong chỉ có đúng một folder cài đặt ghi trong bảng trên.
3. Copy nguyên folder đó vào root dự án. Nếu folder nền tảng như `.agents/`, `.claude/`, `.gemini/` hoặc `.github/` đã có, chỉ **merge folder**, không xóa hay thay thế cả folder cũ.
4. Mở phiên AI mới và dùng lệnh kích hoạt trong bảng.

Không cần mở folder cài đặt và copy từng file bên trong. Không cần tự tạo `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.ai-agent/` hay các file memory.

Nếu hệ điều hành báo trùng đúng một file hoặc skill cùng tên, hãy giữ bản cũ, tạo bản sao lưu và review trước khi thay. Các file của gói đã được đặt tên riêng để giảm xung đột. Trên macOS, `.agents/` và `.claude/` có thể bị Finder ẩn; nhấn `Command + Shift + .` để hiện folder ẩn.

Sau khi được gọi, adapter sẽ:

1. Đọc project và phát hiện cấu hình AI đang có.
2. Kiểm tra xung đột trước khi ghi.
3. Tạo hoặc hợp nhất entry file cần thiết của nền tảng.
4. Tạo `.ai-agent/` hoặc các file workspace native của OpenClaw.
5. Hỏi một nhóm câu ngắn cho những lựa chọn không thể suy ra.
6. Trả birth card và doctor check để người dùng review.

## Lưu ý riêng cho từng nền tảng

### Codex

Codex chính thức khám phá repository skill trong `.agents/skills/`. Vì vậy người dùng chỉ cần dán `.agents/`. Skill sẽ tạo hoặc hợp nhất `AGENTS.md` và `.ai-agent/` sau khi được gọi.

Trong ChatGPT/Codex desktop, gõ `@agents` và chọn **AI Agent Birth**. Trong Codex CLI hoặc IDE, dùng `$agents`.

### Claude Code

Claude Code chính thức khám phá project agents, rules và skills trong `.claude/`. Gõ `@agents` rồi chọn `agents (agent)`. Cú pháp nhập tay chính xác là `@agent-agents`; fallback ổn định là `/agent-birth`.

Bundle dùng `.claude/rules/ai-agent-tool.md`, nên không ghi đè `CLAUDE.md` đang có của dự án. `/agents` vẫn là lệnh quản lý subagent tích hợp của Claude Code, không phải lệnh khai sinh.

### Claude Cowork

Cowork chưa công bố cơ chế tự nạp `CLAUDE.md` hoặc một local skill chỉ nhờ copy folder vào Project. Vì vậy Claude Cowork không dùng kiến trúc skill/`@agents` chung với năm nền tảng còn lại; nó dùng một bộ file Markdown thuần, agent tự đọc theo thứ tự cố định, không cần upload skill:

1. Copy `khai-sinh/` vào folder chính của dự án, rồi kết nối chính folder dự án đó với Cowork Project.
2. Thêm nội dung `khai-sinh/COWORK-PROJECT-INSTRUCTIONS.txt` xuống dưới Project Instructions đang có; không xóa hoặc thay thế chỉ dẫn cũ. Đoạn này bảo đảm mọi phiên, kể cả phiên chạy theo lịch, đều đọc `khai-sinh/CLAUDE.md` trước.
3. Mở phiên mới, gõ đại ý "bắt đầu đi". Agent thấy `BOOTSTRAP.md` còn trong thư mục sẽ tự dẫn qua nghi thức khai sinh, hỏi lần lượt về bài toán, người dùng, ranh giới rồi mới tới danh tính, và ghi thẳng vào `PROJECT.md`, `USER.md`, `IDENTITY.md`.

Xem `khai-sinh/HUONG-DAN.md` trong gói để biết chi tiết từng bước.

### Gemini CLI

Gemini CLI hỗ trợ custom subagent trong `.gemini/agents/`, nên `@agents` là đường gọi native. Nếu copy bundle khi phiên đang mở, chạy `/agents reload`, `/commands reload` và `/skills reload`; sau khi tạo `GEMINI.md`, có thể cần `/memory reload`.

### GitHub Copilot

GitHub không tài liệu hóa `@agents` như lệnh gọi repository agent. Đường được hỗ trợ là `/agent-birth`, hoặc `/agent` rồi chọn `ai-agent-tool`. Bundle giữ `@agents` như alias best-effort khi giao diện chuyển nguyên văn chuỗi đó tới model.

Bundle dùng file riêng `.github/instructions/ai-agent-tool.instructions.md`, nên không ghi đè `.github/copilot-instructions.md` của dự án.

### OpenClaw

OpenClaw là agent runtime, không phải model. Copy `skills/` vào active OpenClaw workspace. Dùng `/skill agents` trên mọi bề mặt; `$agents` là shortcut trong Control UI và WebChat. `/agents` là lệnh built-in khác. Sau khi birth thành công, mở phiên mới hoặc chạy `/reset soft` để các file workspace mới được nạp đầy đủ.

## Vì sao cần AI Agent Tool?

Một model mạnh vẫn bắt đầu dự án với nhiều khoảng trống: mục tiêu thật là gì, lệnh kiểm thử nào đúng, được phép tự làm đến đâu, người dùng thích cách hợp tác nào, quyết định cũ còn hiệu lực hay không.

AI Agent Tool bổ sung năm phần thường thiếu:

- Entry và adapter đúng convention của host.
- Nghi thức birth thay cho việc tự sửa nhiều template.
- Danh tính và cách hợp tác ổn định.
- Project source of truth gồm mục tiêu, phạm vi, lệnh và tiêu chí hoàn thành.
- Portable memory có nguồn, ngày, trạng thái và chế độ `off`, `minimal`, `full`.

Nếu không có bộ này, AI vẫn làm việc được. Người dùng thường phải nhắc lại context, agent dễ đoán sai lệnh hoặc phạm vi, quyết định qua phiên bị quên, hành vi thiếu nhất quán và dữ liệu riêng tư khó kiểm soát hơn.

Nếu context hoặc memory bị ghi sai, agent cũng có thể sai một cách nhất quán hơn. Vì vậy birth flow luôn inspect trước, giữ nguồn và trạng thái, không ghi đè âm thầm, và có doctor check.

## Bộ này đáp ứng phần nào của một AI agent?

| Lớp của agent | AI Agent Tool đáp ứng |
|---|---|
| Model và suy luận | Không thay đổi; dùng model do host chọn |
| Runtime và tool loop | Dùng runtime hiện có như Codex, Claude, Gemini, Copilot hoặc OpenClaw |
| Persistent instructions | Có, qua convention chính thức của từng host |
| Reusable workflow hoặc skill | Có, bằng birth skill và adapter |
| Identity và project context | Có |
| Portable memory | Có, tùy chọn và tách private |
| MCP, connector và credential | Không tự cài |
| Sandbox, permissions và approval | Không thay thế |
| Evaluation | Có structural doctor check; không thay behavioral eval của host |

Đọc [Vì sao và kiến trúc](docs/WHY-AND-ARCHITECTURE.md) để xem phân tích đầy đủ.

## Các lệnh bảo trì

- `agents status`: xem danh tính, project context, memory mode và sức khỏe cấu hình.
- `agents doctor`: kiểm tra mà không sửa.
- `agents doctor --fix`: áp dụng sửa chữa cơ học an toàn.
- `agents reconfigure`: đổi danh tính, cách hợp tác, project facts hoặc memory mode.
- `agents remember <fact>`: lưu một dữ kiện bền vững hợp lệ.
- `agents forget <fact>`: xóa portable memory phù hợp và báo giới hạn xóa.

Thêm ký hiệu gọi đúng của nền tảng, chẳng hạn `@agents doctor`, `$agents doctor` hoặc `/agent-birth doctor`.

Riêng Claude Cowork không có skill nên không có các lệnh trên. Đổi ưu tiên, ranh giới hay danh tính thì sửa thẳng `khai-sinh/USER.md`, `khai-sinh/PROJECT.md` hoặc `khai-sinh/IDENTITY.md`, hoặc bảo agent sửa rồi đọc lại để xác nhận.

## Quyền riêng tư và an toàn

- Runtime private memory nằm trong `.ai-agent/private/` và bị ignore mặc định.
- OpenClaw giữ dữ liệu riêng dưới `.ai-agent-tool/private/`, đã được `.ai-agent-tool/.gitignore` bảo vệ. Tool không tạo root `USER.md` hoặc `MEMORY.md` làm kho riêng vì OpenClaw có thể tự nạp chúng vào session.
- Claude Cowork không có `.ai-agent/private/`: `khai-sinh/USER.md`, `PROJECT.md`, `IDENTITY.md`, `MEMORY.md` nằm ngay ở root folder cài đặt và bắt đầu trống. Đừng commit folder `khai-sinh/` đã điền vào một repository công khai; giữ nó trong project riêng đã kết nối với Cowork.
- Không lưu password, token, API key, cookie, private key, OTP hoặc recovery code trong Markdown.
- Birth invocation chỉ cấp phạm vi khởi tạo cục bộ. Nó không cấp quyền publish, deploy, gửi tin, mua hàng, đổi tài khoản hoặc mở rộng sandbox.
- Prompt và Markdown là chỉ dẫn mềm. Quyền thật vẫn nằm ở sandbox, permissions, hooks, firewall, tool policy và bước phê duyệt của host.

Đọc [SECURITY.md](SECURITY.md) trước khi dùng trong project có dữ liệu nhạy cảm.

## Nguồn chính thức

Thiết kế v2.1 được đối chiếu ngày **2026-08-20** với tài liệu chính thức:

- [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills) và [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Anthropic: Claude Code skills](https://code.claude.com/docs/en/slash-commands), [subagents](https://code.claude.com/docs/en/sub-agents) và [Cowork Projects](https://claude.com/docs/cowork/guide/projects)
- [Google: Gemini CLI subagents](https://geminicli.com/docs/core/subagents/), [skills](https://geminicli.com/docs/cli/skills/) và [commands](https://geminicli.com/docs/cli/custom-commands/)
- [GitHub: Copilot Agent Skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills), [custom agents](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-custom-agents-for-cli) và [instructions](https://docs.github.com/en/copilot/reference/custom-instructions-support)
- [OpenClaw: Skills](https://docs.openclaw.ai/tools/skills), [slash commands](https://docs.openclaw.ai/tools/slash-commands) và [agent workspace](https://docs.openclaw.ai/concepts/agent-workspace)

Xem [bảng hỗ trợ nền tảng](docs/PLATFORM-SUPPORT.md) để biết lệnh nào là native, lệnh nào là alias tương thích.

## Phiên bản và giấy phép

Phiên bản hiện tại: `2.2.0`.

MIT License. Xem [LICENSE](LICENSE).
