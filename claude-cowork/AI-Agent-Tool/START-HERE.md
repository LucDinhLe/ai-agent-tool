# Cài AI Agent Tool cho Claude Cowork

Cowork hiện chưa công bố cơ chế tự nạp file dự án tương đương `CLAUDE.md` của Claude Code. Vì vậy cần thêm Project Instructions đúng một lần để alias `@agents` hoạt động ổn định.

## Kích hoạt với folder dự án đã kết nối

1. Copy nguyên folder `AI-Agent-Tool/` vào **folder chính của dự án**. Không mở folder này rồi copy từng file bên trong.
2. Tạo Cowork Project từ folder chính đó, hoặc kết nối chính folder đó làm project context. Không chọn riêng folder con `AI-Agent-Tool/`.
3. Mở `AI-Agent-Tool/COWORK-PROJECT-INSTRUCTIONS.txt`. Thêm toàn bộ nội dung file xuống dưới Project Instructions đang có. Không xóa hoặc thay thế chỉ dẫn cũ; nếu có mâu thuẫn, review và xử lý rõ ràng trước khi chạy.
4. Mở task mới và gõ `@agents`.

Adapter chỉ tạo `.ai-agent/` sau khi được kích hoạt. Bước Project Instructions là bắt buộc với luồng copy folder vì Anthropic chưa cam kết Cowork tự phát hiện local `@agents`.

## Cách cài skill vào tài khoản, tùy chọn

Trang GitHub Release có sẵn gói `AI-Agent-Tool-Claude-Cowork-Skill.zip`. Upload gói này tại **Customize → Skills**, bật skill, rồi yêu cầu Claude dùng **Agent Birth**. Tài liệu Cowork hiện không cam kết lệnh slash `/agent-birth` cho skill đã upload, nên hướng dẫn bằng tên skill là cách an toàn hơn.

Cowork chỉ truy cập các folder người dùng cấp quyền. Nên dùng một folder làm việc riêng và không để secret bên trong. AI Agent Tool không mở rộng quyền của Cowork, không thay sandbox và không bỏ qua bước xác nhận.

> English quick start: copy `AI-Agent-Tool/` into the connected project root, append the supplied instruction block without replacing existing instructions, start a new task, then type `@agents`.
