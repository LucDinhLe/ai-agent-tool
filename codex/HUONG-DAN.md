# HƯỚNG DẪN — Khai sinh agent trong Codex

## Cài đặt

1. Tạo hoặc mở project local mà Codex sẽ làm việc.
2. Chép toàn bộ tám file `.md` của gói này vào thư mục gốc của project.
3. Nếu project đã có `AGENTS.md` hoặc file trùng tên, dừng lại và hợp nhất nội dung; không ghi đè.
4. Mở một task hoặc phiên Codex mới. Codex đọc `AGENTS.md` khi phiên bắt đầu.
5. Nói `Bắt đầu khai sinh agent cho dự án này`.
6. Trả lời từng câu và duyệt bản tóm tắt cuối.
7. Kiểm tra `BOOTSTRAP.md` đã chuyển thành `Status: COMPLETE`.

Không cần gõ ký hiệu đặc biệt. Câu khai sinh là yêu cầu bằng ngôn ngữ tự nhiên.

## Kiểm tra nhanh

Trong phiên mới, hỏi:

> Trạng thái khai sinh hiện tại là gì, và trước công việc đáng kể bạn phải đọc những file nào?

Codex phải đọc đúng trạng thái trong `BOOTSTRAP.md` và nêu đúng các file hồ sơ. Nếu không, kiểm tra tám file có nằm cùng cấp với `AGENTS.md` và bạn đã mở phiên mới hay chưa.

## Bộ này giúp gì?

Nó giúp Codex biết mình phục vụ ai, giải bài toán gì, đâu là nguồn sự thật, đầu ra thế nào mới đạt, việc gì cần hỏi trước và quyết định nào cần mang sang phiên sau. Nó không thay đổi model hoặc quyền của Codex.

## Lưu ý

- Bộ này phù hợp nhất với project mới.
- Không chạy lệnh tạo file chỉ dẫn tự động nếu việc đó có thể ghi đè `AGENTS.md`.
- Không lưu credential hoặc dữ liệu cá nhân không cần thiết.
- `MEMORY.md` có thể bị commit cùng project. Hãy rà lại trước khi chia sẻ công khai.

Tài liệu chính thức: [OpenAI — Custom instructions with AGENTS.md](https://developers.openai.com/codex/guides/agents-md).
