# HƯỚNG DẪN — Khai sinh agent trong Google Antigravity

## Cài đặt

1. Tạo hoặc mở Antigravity Project có thư mục local cần làm việc.
2. Chép toàn bộ tám file `.md` của gói này vào root của thư mục đó.
3. Nếu project đã có `AGENTS.md` hoặc file trùng tên, dừng lại và hợp nhất nội dung; không ghi đè.
4. Mở một cuộc trò chuyện mới và chọn **Local Mode** để làm trực tiếp trong thư mục vừa chép file.
5. Nói `Đọc AGENTS.md ở root của thư mục này, rồi bắt đầu khai sinh agent cho dự án này`.
6. Trả lời từng câu và duyệt bản tóm tắt cuối.
7. Kiểm tra `BOOTSTRAP.md` đã chuyển thành `Status: COMPLETE`.

Không cần cài skill, plugin, workflow hoặc dùng ký hiệu gọi đặc biệt. Câu ở bước 5 là đường kích hoạt phẳng, rõ ràng cho Antigravity Desktop. Nếu dùng Antigravity CLI, công cụ tự đọc `AGENTS.md` ở workspace root khi khởi động nên có thể nói ngắn gọn `Bắt đầu khai sinh agent cho dự án này`.

## Kiểm tra nhanh

Trong cuộc trò chuyện mới, hỏi:

> Đọc AGENTS.md, cho biết trạng thái khai sinh hiện tại và những file phải đọc trước công việc đáng kể.

Antigravity phải đọc đúng trạng thái trong `BOOTSTRAP.md` và nêu đúng các file hồ sơ. Nếu không, kiểm tra tám file có nằm ở root của đúng thư mục đang hoạt động, cuộc trò chuyện đang ở Local Mode và câu yêu cầu có gọi rõ `AGENTS.md` hay chưa.

## Bộ này giúp gì?

Nó giúp Antigravity biết mình phục vụ ai, giải bài toán gì, đâu là nguồn sự thật, đầu ra thế nào mới đạt, việc gì cần hỏi trước và quyết định nào cần mang sang phiên sau. Nó không thay đổi model, quyền hay các agent có sẵn của Antigravity.

## Lưu ý

- Bộ này phù hợp nhất với project mới và Local Mode.
- New Worktree Mode có thể không mang theo file chưa được commit từ thư mục hiện tại.
- Không lưu credential hoặc dữ liệu cá nhân không cần thiết.
- `MEMORY.md` có thể bị commit cùng project. Hãy rà lại trước khi chia sẻ công khai.

Tài liệu chính thức:

- [Google Antigravity — Best practices for AGENTS.md](https://antigravity.google/docs/cli/best-practices/)
- [Google Antigravity — Projects and Local Mode](https://antigravity.google/docs/projects)
- [Google Antigravity — Changelog 2.11.0](https://antigravity.google/changelog)
