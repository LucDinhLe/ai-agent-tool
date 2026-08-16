# Bảo mật và quyền riêng tư

## Mặc định an toàn

- `.ai-agent/private/` bị Git bỏ qua.
- Không lưu mật khẩu, API key, token, cookie, khóa riêng, mã OTP hoặc dữ liệu xác thực vào Markdown.
- Không đưa nội dung riêng tư vào `SOUL.md`, `WORKSPACE.md`, `AGENTS.md` hoặc `CLAUDE.md` nếu repository có thể được chia sẻ.
- Quyết định gửi email, đăng bài, phát hành, thanh toán hoặc thay đổi hệ thống bên ngoài cần người dùng xác nhận.
- Thao tác xóa, ghi đè, di chuyển hàng loạt, thay đổi quyền hoặc sửa dữ liệu thật cần xác định chính xác mục tiêu và đường khôi phục.

## Giới hạn

Các tệp Markdown chỉ tạo chỉ dẫn. Sandbox, quyền tệp, quyền mạng, phê duyệt công cụ và nhật ký kiểm toán vẫn phải được cấu hình trong Codex hoặc Claude Code.

Agent có thể ghi sai ký ức. `MEMORY_POLICY.md` giảm rủi ro bằng nguồn gốc và trạng thái, nhưng người dùng vẫn cần rà soát định kỳ.

## Trước khi đưa repository lên mạng

1. Chạy `git status` và kiểm tra mọi tệp chưa theo dõi.
2. Xác nhận `.ai-agent/private/` không xuất hiện trong danh sách commit.
3. Tìm credential bằng công cụ quét bí mật phù hợp với dự án.
4. Nếu dữ liệu riêng tư từng được commit, xóa tệp hiện tại chưa đủ; cần thu hồi credential và làm sạch lịch sử Git theo quy trình của tổ chức.
