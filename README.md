# AI Agent Tool

AI Agent Tool là bộ cấu hình Markdown giúp Codex và Claude Code làm việc nhất quán, nhớ đúng bối cảnh và giữ ranh giới an toàn qua nhiều phiên.

Bộ công cụ tác động lên ngữ cảnh và quy trình làm việc. Nó không huấn luyện lại mô hình, không mở thêm quyền và không tự tạo tác vụ chạy nền.

## Chọn gói cài đặt

- `bundles/codex/` dành cho Codex CLI, ứng dụng Codex và phần mở rộng Codex.
- `bundles/claude-code/` dành cho Claude Code.

Mỗi thư mục là một gói độc lập. Sao chép **nội dung bên trong** gói phù hợp vào thư mục gốc của workspace hoặc repository.

Nếu workspace đã có `AGENTS.md`, `CLAUDE.md` hoặc `.gitignore`, hãy hợp nhất nội dung thay vì ghi đè. Bản sao lưu trước khi hợp nhất luôn là lựa chọn khôn ngoan.

## Thiết lập trong 5 phút

1. Chọn gói Codex hoặc Claude Code.
2. Sao chép nội dung gói vào thư mục gốc của workspace.
3. Điền `.ai-agent/SOUL.md` và `.ai-agent/WORKSPACE.md`.
4. Điền `.ai-agent/private/USER.md`; chỉ thêm thông tin thật sự giúp công việc.
5. Mở một phiên AI mới để tệp đầu vào được nạp lại.

Nếu cài bằng cách clone repository, Git sẽ không tải thư mục `private/` vì đây là vùng dữ liệu cục bộ. Hãy sao chép `.ai-agent/private.example/` thành `.ai-agent/private/` trong bundle đã chọn, rồi điền thông tin của bạn.

`SOUL.md`, `WORKSPACE.md` và `MEMORY_POLICY.md` có thể được chia sẻ cùng dự án. Toàn bộ `.ai-agent/private/` bị Git bỏ qua mặc định.

## Kiểm tra sau khi cài

Hỏi agent lần lượt:

1. “Hãy tóm tắt các chỉ dẫn workspace đang áp dụng.”
2. “Thông tin nào được phép ghi vào ký ức dài hạn?”
3. “Nếu tôi yêu cầu gửi hoặc công bố nội dung ra ngoài, bạn sẽ làm gì?”
4. “Đâu là nguồn sự thật của dự án này?”

Agent đạt khi trả lời đúng nội dung đã cấu hình, phân biệt dữ kiện với suy luận và yêu cầu xác nhận trước hành động bên ngoài hoặc phá hủy dữ liệu.

## Cấu trúc

```text
.ai-agent/
├── SOUL.md             # Giọng điệu, giá trị và phong cách hợp tác
├── WORKSPACE.md        # Mục tiêu, kiến trúc, quy ước và lệnh kiểm tra dự án
├── MEMORY_POLICY.md    # Quy tắc ghi, đọc, sửa và loại bỏ ký ức
└── private/            # Dữ liệu cục bộ, bị Git bỏ qua
    ├── USER.md
    ├── TOOLS.md
    ├── MEMORY.md
    └── memory/
```

## Nguyên tắc thiết kế

- Tệp đầu vào ngắn, đóng vai trò bản đồ.
- Thông tin có một nguồn sự thật, tránh lặp lại ở nhiều tệp.
- Ký ức phải có nguồn, ngày, trạng thái và khả năng sửa.
- Dữ liệu riêng tư tách khỏi tài liệu có thể commit.
- Quyền của công cụ và cơ chế xin phép do nền tảng kiểm soát; Markdown không thay thế sandbox.

## Gỡ cài đặt

Xóa phần AI Agent Tool đã thêm trong `AGENTS.md` hoặc `CLAUDE.md`, sau đó xóa `.ai-agent/`. Kiểm tra `.gitignore` và chỉ bỏ các dòng liên quan nếu dự án không còn dùng chúng.

## Phiên bản

`1.0.0`, ưu tiên Codex và Claude Code.

## Nền tảng thiết kế

AI Agent Tool được thiết kế lại từ mô hình workspace Markdown của các AI agent hiện đại. Cơ chế Codex bám theo [hướng dẫn `AGENTS.md` chính thức](https://learn.chatgpt.com/docs/agent-configuration/agents-md); cơ chế Claude Code bám theo [hướng dẫn bộ nhớ và `@import`](https://docs.anthropic.com/en/docs/claude-code/memory).

## Giấy phép

MIT. Xem `LICENSE`.
