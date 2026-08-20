# Changelog

## 2.0.1 — 2026-08-20

- Thêm gói tổng `AI-Agent-Tool-CHON-NEN-TANG-v2.0.1.zip` với sáu folder nền tảng hiển thị ngay ở cấp đầu.
- Đưa sáu folder nền tảng lên root của repository để bản `Code → Download ZIP` cũng dễ chọn đúng.
- Thêm `00-BAT-DAU-O-DAY.md` để giải thích sự khác nhau giữa ZIP mã nguồn và gói cài đặt.
- Làm rõ thao tác chọn một nền tảng, mở folder và copy toàn bộ nội dung bên trong vào root dự án.
- Thêm kiểm thử tự động cho cấu trúc ZIP, đường dẫn an toàn, dữ liệu riêng tư và SHA-256.

## 2.0.0 — 2026-08-19

- Chuyển từ template điền tay sang workflow copy → paste → gọi `@agents` → birth card.
- Đóng gói sáu folder tự chứa cho Codex, Claude Code, Claude Cowork, Gemini CLI, GitHub Copilot và OpenClaw.
- Thêm entry file, Agent Skill, native fallback và adapter riêng theo convention chính thức của từng host.
- Thêm state schema, memory modes `off|minimal|full`, private templates và doctor workflow.
- Thêm exact `@agents` native subagent cho Gemini CLI và skill invocation chính thức cho Codex/Copilot.
- Ghi rõ bước Project Instructions bắt buộc của Claude Cowork và giới hạn của portable alias trên các host giữ ký hiệu `@`.
- Thêm tài liệu “vì sao cần”, kiến trúc agent, support matrix, nguồn chính thức và giới hạn bảo mật.
- Thêm validator, release builder và gói ZIP riêng cho từng nền tảng.

## 1.0.0 — 2026-08-17

- Ra mắt tên gọi AI Agent Tool.
- Thêm bundle tối ưu cho Codex với `AGENTS.md` ngắn và phân tầng chỉ dẫn.
- Thêm bundle tối ưu cho Claude Code với cơ chế `@import`.
- Tách dữ liệu riêng tư khỏi Git và cung cấp `private.example/` cho người cài bằng clone.
- Thêm chính sách ký ức có nguồn, ngày kiểm chứng, trạng thái và cơ chế sửa sai.
- Bỏ heartbeat giả, tự commit/push và các chỉ dẫn không liên quan đến Codex hoặc Claude Code.
- Thêm tài liệu bảo mật, kiểm tra cài đặt, gỡ cài đặt và giấy phép MIT.
