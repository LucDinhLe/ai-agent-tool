# Changelog

## 2.2.0 — 2026-08-28

- Thay toàn bộ adapter Claude Cowork bằng bộ khai sinh Markdown thuần `khai-sinh/`, bỏ hẳn kiến trúc skill/`.ai-agent/` runtime mà Cowork chưa hỗ trợ tự khám phá.
- Cowork không còn dùng alias `@agents`; kích hoạt bằng cách mở phiên mới và gõ "bắt đầu đi", agent tự dẫn qua nghi thức trong `BOOTSTRAP.md`.
- Danh tính, người dùng, bài toán và ký ức chắt lọc chuyển thẳng vào `IDENTITY.md`, `USER.md`, `PROJECT.md`, `MEMORY.md` ở root, không còn `.ai-agent/private/`.
- Bỏ gói `AI-Agent-Tool-Claude-Cowork-Skill.zip` khỏi luồng phát hành vì không còn skill để upload qua Customize.
- Cập nhật validator, build script và smoke test cho cấu trúc mới; `claude-cowork/` giờ chỉ còn một folder cài đặt duy nhất.

## 2.1.0 — 2026-08-20

- Đổi kiến trúc cài đặt thành **một ZIP, một folder** cho từng nền tảng.
- Codex chỉ cần copy `.agents/`; Claude Code chỉ cần `.claude/`; Gemini CLI chỉ cần `.gemini/`; GitHub Copilot chỉ cần `.github/`; OpenClaw chỉ cần `skills/`; Cowork chỉ cần `AI-Agent-Tool/`.
- Chuyển toàn bộ runtime template vào bên trong adapter. Agent chỉ tạo hoặc hợp nhất entry, identity, project context và memory sau khi được kích hoạt.
- Bỏ gói tổng sáu folder khỏi luồng phát hành để người dùng không phải chọn và tự dàn nhiều file.
- Dùng tên asset ổn định để README luôn tải bản mới nhất trực tiếp.
- Claude Code chuyển sang project rule riêng, không ghi đè `CLAUDE.md`.
- GitHub Copilot dùng scoped adapter riêng để kích hoạt, rồi tạo hoặc merge root `AGENTS.md` cho context repo-wide; không ghi đè `.github/copilot-instructions.md`.
- OpenClaw chuyển sang thư mục `skills/` native, không tự tạo `HEARTBEAT.md`, `TOOLS.md` hoặc `BOOTSTRAP.md`; private memory nằm dưới `.ai-agent-tool/private/` thay vì root bootstrap files.
- Đặt tên riêng cho adapter Claude Code và Gemini để giảm xung đột khi merge vào dự án đã có cấu hình.
- Thêm kiểm thử bắt buộc mỗi ZIP chỉ có đúng một top-level install folder.

## 2.0.1 — 2026-08-20

- Thêm gói tổng `AI-Agent-Tool-CHON-NEN-TANG-v2.0.1.zip` với sáu folder nền tảng hiển thị ngay ở cấp đầu.
- Đưa sáu folder nền tảng lên root của repository để bản `Code → Download ZIP` cũng dễ chọn đúng.
- Thêm `00-BAT-DAU-O-DAY.md` để giải thích sự khác nhau giữa ZIP mã nguồn và gói cài đặt.
- Làm rõ thao tác chọn một nền tảng, mở folder và copy toàn bộ nội dung bên trong vào root dự án.
- Thêm kiểm thử tự động cho cấu trúc ZIP, đường dẫn an toàn, dữ liệu riêng tư và SHA-256.
- Bảo đảm trình đóng gói trên Windows và Linux đều giữ các thư mục bắt đầu bằng dấu chấm như `.agents/`, `.claude/`, `.github/` và `.ai-agent/`.

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
