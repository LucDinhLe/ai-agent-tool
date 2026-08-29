# HƯỚNG DẪN — Khai sinh agent trong Claude Cowork

Cowork có thể xử lý trên máy chủ Anthropic các file local mà người dùng cho phép đọc. Chỉ gắn thư mục cần thiết và không đặt credential hoặc dữ liệu nhạy cảm không cần thiết trong bộ hồ sơ.

## Cài đặt

1. Tạo Cowork Project mới bằng **Start from scratch** hoặc **Use an existing folder**.
2. Chép toàn bộ tám file `.md` của gói này vào thư mục local đầu tiên của project.
3. Nếu project đã có `CLAUDE.md` hoặc file trùng tên, dừng lại và hợp nhất nội dung; không ghi đè.
4. Mở phần cài đặt của project và đặt **Project Instructions** thành câu sau:

   > Trước mọi tác vụ, đọc `CLAUDE.md` trong thư mục local đầu tiên của project và làm theo. Nếu `BOOTSTRAP.md` có `Status: PENDING`, chỉ chạy quy trình khai sinh khi tôi yêu cầu.

5. Mở một Cowork session mới trong project.
6. Nói `Bắt đầu khai sinh agent cho dự án này`.
7. Trả lời từng câu và duyệt bản tóm tắt cuối.
8. Kiểm tra `BOOTSTRAP.md` đã chuyển thành `Status: COMPLETE`.

Không cần cài skill, plugin hoặc dùng ký hiệu gọi đặc biệt. Project Instructions chỉ giúp Cowork biết file nào phải đọc ở đầu mỗi phiên.

## Kiểm tra nhanh

Trong phiên mới, hỏi:

> Trạng thái khai sinh hiện tại là gì, và trước công việc đáng kể bạn phải đọc những file nào?

Cowork phải đọc đúng trạng thái trong `BOOTSTRAP.md` và nêu đúng các file hồ sơ. Nếu không, kiểm tra tám file có nằm trong thư mục local đầu tiên của project và Project Instructions đã được lưu hay chưa.

## Bộ này giúp gì?

Nó giúp Cowork biết mình phục vụ ai, giải bài toán gì, đâu là nguồn sự thật, đầu ra thế nào mới đạt, việc gì cần hỏi trước và quyết định nào cần mang sang phiên sau. Nó không thay đổi model, quyền hay bộ nhớ riêng của Cowork.

## Lưu ý

- Bộ này phù hợp nhất với project mới.
- `MEMORY.md` là hồ sơ mang theo thư mục, tách biệt với memory do Cowork quản lý.
- Không lưu credential hoặc dữ liệu cá nhân không cần thiết.
- Rà lại toàn bộ hồ sơ trước khi gắn thêm thư mục, connector hoặc chia sẻ dữ liệu ra ngoài.

Tài liệu chính thức:

- [Anthropic — Organize work with Cowork Projects](https://claude.com/docs/cowork/guide/projects)
- [Anthropic — Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)
