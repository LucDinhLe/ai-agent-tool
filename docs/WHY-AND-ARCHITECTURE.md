# Vì sao AI Agent Tool tồn tại?

## Model, runtime và agent là ba lớp khác nhau

Một model tạo phản hồi từ context hiện tại. Một runtime như Codex, Claude Code, Cowork, Gemini CLI, GitHub Copilot hay OpenClaw bổ sung vòng lặp hành động, công cụ, file access, permissions và giao diện. Một project agent chỉ trở nên ổn định khi runtime còn có chỉ dẫn, kiến thức dự án, workflow, ký ức và cơ chế kiểm tra phù hợp.

AI Agent Tool làm việc ở lớp cấu hình project agent. Nó không thay model và không thay runtime.

## Kiến trúc tham chiếu của một agent hiện đại

1. **Model**: suy luận, ngôn ngữ, lập kế hoạch và tạo nội dung.
2. **Harness/runtime**: vòng lặp agent, quản lý context, tool calls, phiên và UI.
3. **Persistent instructions**: quy tắc luôn áp dụng trong project.
4. **Skills và specialist agents**: workflow có thể tái sử dụng, chỉ nạp khi cần.
5. **Project knowledge**: mục tiêu, kiến trúc, lệnh, tiêu chí hoàn thành và quyết định.
6. **Memory**: dữ kiện bền vững và continuity qua phiên.
7. **Tools/connectors**: filesystem, shell, browser, MCP, apps và API.
8. **Guardrails**: sandbox, permissions, hooks, policy, approval và audit log.
9. **Evaluation**: kiểm tra cấu trúc, hành vi và kết quả.

Các nhà phát hành hiện đều tách các lớp này. OpenAI mô tả Codex customization qua `AGENTS.md`, memories, skills, MCP và subagents. Anthropic tách `CLAUDE.md`, rules, skills, subagents, hooks và permissions. Gemini CLI có `GEMINI.md`, Agent Skills, commands, subagents, trusted folders và sandbox. GitHub Copilot có repository instructions, skills và custom agents.

## AI Agent Tool cung cấp gì?

### 1. Adapter đúng convention

Mỗi host chỉ tự khám phá một số vị trí và filename. Một folder chung dùng sai entry file có thể nằm trong project nhưng không bao giờ được nạp. Vì vậy v2.1 phát hành một ZIP riêng cho từng host. Năm host dùng đúng một discovery folder native với birth protocol và schema ký ức logic tương đương. Claude Cowork là ngoại lệ có chủ đích: Cowork không có cơ chế discovery skill theo project folder, nên bundle của nó bỏ hẳn lớp skill/`.ai-agent/` và dùng file Markdown thuần ở root, xem chi tiết tại [bảng hỗ trợ nền tảng](PLATFORM-SUPPORT.md#claude-cowork).

### 1.1. One-folder bootstrap

Mỗi gói chỉ cài lớp mồi mà host có thể tự khám phá:

- Codex: `.agents/`
- Claude Code: `.claude/`
- Claude Cowork: `khai-sinh/` cùng Project Instructions một lần, không dùng skill hay `.ai-agent/`
- Gemini CLI: `.gemini/`
- GitHub Copilot: `.github/`
- OpenClaw: `skills/`

Sau lời gọi khai sinh, chính agent inspect project, tạo hoặc merge entry, chép runtime template, hỏi lựa chọn còn thiếu và chạy doctor. Thiết kế này làm thao tác cài đặt ngắn, giảm nguy cơ ghi đè và giữ quyền quyết định ở thời điểm agent đã nhìn thấy project thật.

### 2. Birth workflow

Template tĩnh buộc người dùng tự tìm và điền nhiều file. Birth workflow chuyển việc đó thành một cuộc khởi tạo có kiểm soát:

- Inspect project trước.
- Suy ra dữ kiện có thể kiểm chứng.
- Hỏi một nhóm câu ngắn cho phần không thể suy ra.
- Xác nhận khi có nguy cơ ghi đè nội dung thật.
- Ghi đúng file và tự kiểm tra.
- Trả birth card để người dùng review.

### 3. Danh tính có cấu trúc

`SOUL.md` hoặc các file native tương đương giữ tên, vai trò, cách giao tiếp và giá trị làm việc ổn định. Project facts không bị nhét vào persona; dữ liệu cá nhân không bị nhét vào file chia sẻ.

### 4. Nguồn sự thật của project

`WORKSPACE.md` hoặc `PROJECT.md` gom mục tiêu, phạm vi, đường dẫn quan trọng, lệnh setup/test/build, tiêu chí hoàn thành và quyết định đã xác minh. Agent có một điểm tra cứu rõ thay vì đoán từ nhiều cuộc chat.

### 5. Ký ức portable có kiểm soát

Memory được chia thành ba mode:

- `off`: không dùng memory file riêng.
- `minimal`: chỉ giữ preference rõ ràng và quyết định bền vững.
- `full`: thêm dated notes chọn lọc khi continuity thực sự cần.

Mỗi entry có trạng thái, nguồn, ngày xác minh và điều kiện review. Dữ kiện mới có bằng chứng mạnh hơn sẽ thay thế entry cũ, thay vì để hai “sự thật” cùng hoạt động.

### 6. Doctor check

Doctor kiểm tra file bắt buộc, state, placeholder, rule riêng tư, đường gọi native và dấu hiệu credential. Đây là structural eval nhỏ, hữu ích sau copy/paste hoặc upgrade. Nó không thay thế behavioral eval của host.

Phần 5 và 6 mô tả năm bundle dùng kiến trúc skill/`.ai-agent/`. Claude Cowork không có memory mode hay lệnh doctor riêng; thay vào đó nó dùng hai lớp trí nhớ đơn giản hơn (project memory của Cowork cho trạng thái phiên, `MEMORY.md` cho quyết định đã chốt) và không có structural eval tự động, xem `khai-sinh/HUONG-DAN.md`.

## Vì sao agent thường làm tốt hơn khi có bộ này?

Hiệu quả đến từ context engineering và workflow reliability:

- **Ít entropy đầu vào hơn**: model biết outcome, scope và acceptance criteria.
- **Ít đoán hơn**: setup/test/build command và source of truth được chỉ rõ.
- **Ít context lặp lại hơn**: preference và quyết định bền vững được nạp có chọn lọc.
- **Hành vi ổn định hơn**: cùng working contract áp dụng giữa các phiên.
- **Giảm lỗi quy trình**: birth và doctor biến setup thành checklist có thể kiểm chứng.
- **Dễ chuyển host hơn**: dữ liệu cốt lõi ở Markdown portable, adapter xử lý convention riêng.

Bộ này không bảo đảm mọi output hay hơn. Khi context sai, memory cũ hoặc instruction xung đột, nó có thể làm sai một cách nhất quán hơn. Vì vậy source, status, review date và doctor check là phần bắt buộc của thiết kế.

## Nếu không có thì sao?

AI vẫn có thể hoàn thành nhiều tác vụ. Người dùng thường phải trả chi phí vận hành:

- Nhắc lại vai trò, mục tiêu và preference ở mỗi phiên.
- Agent đọc nhầm hoặc bỏ sót tài liệu quan trọng.
- Lệnh kiểm thử và tiêu chí hoàn thành thay đổi theo phỏng đoán.
- Quyết định cũ biến mất hoặc bị nhớ sai.
- Khó biết dữ liệu cá nhân đang nằm trong file nào.
- Một bộ instruction dùng được ở host A có thể vô hình với host B.
- Onboarding thành viên hoặc agent mới tốn nhiều cuộc chat.

## Phần cố ý không đóng gói

- **Model pinning**: model thay đổi nhanh và nên do host/người dùng chọn.
- **MCP/connectors mặc định**: mỗi tổ chức có dữ liệu, credential và policy khác nhau.
- **Allow-all permissions**: tiện lúc đầu nhưng mở rộng blast radius.
- **Auto hooks chạy script**: không phù hợp với gói copy/paste công khai.
- **Tự publish hoặc tự push**: hành động bên ngoài cần authorization riêng.
- **Credential memory**: Markdown không phải secret manager.

## Soft guidance và hard controls

Entry files, soul, memory policy và skills đều là soft guidance được model diễn giải. Hard controls nằm ở runtime:

- Filesystem/network sandbox.
- Tool allow/deny policy.
- Human approval.
- Hooks có khả năng block.
- Firewall và environment isolation.
- Audit log và review workflow.

Một gói Markdown không được quảng cáo như một security boundary. AI Agent Tool luôn giữ sự phân biệt này trong entry files và tài liệu cài đặt.

## Nguyên tắc nâng cấp

- Kiểm tra official convention trước khi đổi adapter.
- Giữ birth protocol portable và platform entry ngắn.
- Không ghi đè file project đã có; merge theo từng phần.
- Không tự di chuyển hoặc xóa memory khi đổi mode.
- Chạy validator, skill validator và forward test trước khi phát hành.
