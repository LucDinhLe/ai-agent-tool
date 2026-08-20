# Bảo mật và quyền riêng tư

## Mặc định an toàn

- Trong các bundle Codex, Claude, Gemini và Copilot, adapter chỉ tạo `.ai-agent/private/` sau khi memory mode được chọn; `.ai-agent/.gitignore` bỏ qua vùng này mà không cần sửa `.gitignore` của project.
- Trong OpenClaw, dữ liệu riêng chỉ được tạo dưới `.ai-agent-tool/private/` sau khi xác nhận `.ai-agent-tool/.gitignore` có rule `/private/`. Tool không tạo root `USER.md`, `MEMORY.md` hoặc dated memory làm kho private vì OpenClaw có thể tự nạp chúng vào session.
- Không lưu mật khẩu, API key, token, cookie, khóa riêng, mã OTP hoặc dữ liệu xác thực vào Markdown.
- Không đưa nội dung riêng tư vào `SOUL.md`, `WORKSPACE.md`, `AGENTS.md` hoặc `CLAUDE.md` nếu repository có thể được chia sẻ.
- Quyết định gửi email, đăng bài, phát hành, thanh toán hoặc thay đổi hệ thống bên ngoài cần người dùng xác nhận.
- Thao tác xóa, ghi đè, di chuyển hàng loạt, thay đổi quyền hoặc sửa dữ liệu thật cần xác định chính xác mục tiêu và đường khôi phục.

## Giới hạn

Các tệp Markdown và Agent Skill tạo chỉ dẫn cho model. Sandbox, quyền tệp, quyền mạng, phê duyệt công cụ, hooks, firewall và nhật ký kiểm toán vẫn phải được cấu hình trong host.

Agent có thể ghi sai ký ức. `MEMORY_POLICY.md` giảm rủi ro bằng nguồn gốc và trạng thái, nhưng người dùng vẫn cần rà soát định kỳ.

Lời gọi birth như `@agents`, `$agents` hoặc `/agent-birth` chỉ cấp phạm vi khởi tạo cục bộ được mô tả trong protocol. Nó không cấp quyền gửi, publish, deploy, chi tiền, sửa tài khoản hoặc mở rộng sandbox.

Skill là code/instruction có khả năng ảnh hưởng hành vi agent. Hãy đọc `SKILL.md` và script đi kèm trước khi cài một fork hoặc bản phát hành bên thứ ba.

## Trước khi đưa repository lên mạng

1. Chạy `git status` và kiểm tra mọi tệp chưa theo dõi.
2. Xác nhận `.ai-agent/private/` hoặc `.ai-agent-tool/private/` không xuất hiện trong danh sách commit.
3. Tìm credential bằng công cụ quét bí mật phù hợp với dự án.
4. Nếu dữ liệu riêng tư từng được commit, xóa tệp hiện tại chưa đủ; cần thu hồi credential và làm sạch lịch sử Git theo quy trình của tổ chức.

## Báo cáo lỗ hổng

Không mở public issue có chứa credential, dữ liệu cá nhân hay proof-of-concept gây hại. Dùng GitHub private vulnerability reporting của repository khi tính năng này được bật.
