# AI Agent Tool

**Bộ tám file Markdown phẳng để khai sinh hồ sơ làm việc cho AI agent đang có trong project local.**

AI Agent Tool dành cho người đã tạo project trên Codex, Claude Cowork hoặc Google Antigravity. “Khai sinh” ở đây là thiết lập danh tính, người dùng, bài toán, ranh giới và trí nhớ mang theo project cho agent của nền tảng. Bộ file không đăng ký một custom agent mới trong menu của ứng dụng.

Bạn tải đúng gói rồi chép các file `.md` vào thư mục gốc của project. Không cần cài phần mềm bổ sung. Mỗi gói chỉ có tám file Markdown phẳng, không có thư mục con, script hay file thực thi.

Đọc [bài giới thiệu đầy đủ](GIOI-THIEU.md) để hiểu cơ chế, lợi ích, cách đo mức cải thiện hiệu suất và giới hạn thực tế của bộ tool.

## Tải đúng gói

| Nền tảng | Tải trực tiếp | File cửa vào |
|---|---|---|
| OpenAI Codex | [AI-Agent-Tool-Codex.zip](https://github.com/LucDinhLe/ai-agent-tool/releases/latest/download/AI-Agent-Tool-Codex.zip) | `AGENTS.md` |
| Claude Cowork | [AI-Agent-Tool-Claude-Cowork.zip](https://github.com/LucDinhLe/ai-agent-tool/releases/latest/download/AI-Agent-Tool-Claude-Cowork.zip) | `CLAUDE.md` |
| Google Antigravity | [AI-Agent-Tool-Antigravity.zip](https://github.com/LucDinhLe/ai-agent-tool/releases/latest/download/AI-Agent-Tool-Antigravity.zip) | `AGENTS.md` |

Nếu tải bằng nút **Code → Download ZIP**, mở đúng một trong ba thư mục `codex`, `claude-cowork` hoặc `antigravity`, rồi chỉ chép tám file bên trong thư mục đó.

## Cách sử dụng

1. Tạo một project local mới trong công cụ AI bạn đang dùng.
2. Tải đúng gói và giải nén.
3. Chép toàn bộ tám file `.md` vào thư mục gốc của project.
4. Làm theo `HUONG-DAN.md` của gói.
5. Kích hoạt theo đúng dòng tương ứng dưới đây.
6. Trả lời từng câu. Agent sẽ điền hồ sơ và đổi `BOOTSTRAP.md` từ `PENDING` sang `COMPLETE` khi hoàn tất.

| Nền tảng | Cách kích hoạt |
|---|---|
| Codex | Mở phiên mới rồi nói `Bắt đầu khai sinh agent cho dự án này` |
| Claude Cowork | Thêm một câu Project Instructions theo `HUONG-DAN.md`, mở phiên mới rồi nói câu khai sinh |
| Antigravity Desktop | Mở cuộc trò chuyện Local Mode rồi nói `Đọc AGENTS.md ở root của thư mục này, rồi bắt đầu khai sinh agent cho dự án này` |
| Antigravity CLI | Khởi động CLI ở workspace root rồi nói câu khai sinh |

Nếu project đã có file trùng tên, hãy dừng lại và hợp nhất nội dung. Không ghi đè âm thầm. Bộ này tối ưu cho project mới hoặc project chưa có hệ thống chỉ dẫn riêng.

## Tám file làm gì?

| File | Vai trò |
|---|---|
| `AGENTS.md` hoặc `CLAUDE.md` | File bắt đầu, chỉ cho nền tảng cách đọc và vận hành bộ hồ sơ |
| `BOOTSTRAP.md` | Cuộc trò chuyện khai sinh, chạy một lần và giữ trạng thái |
| `IDENTITY.md` | Tên, vai trò, chất giọng và mục đích tồn tại của agent |
| `USER.md` | Người agent phục vụ, ưu tiên, cách hợp tác và ranh giới |
| `PROJECT.md` | Bài toán, phạm vi, nguồn sự thật và tiêu chí hoàn thành |
| `SETUP.md` | Môi trường, công cụ, quyền truy cập và việc định kỳ |
| `MEMORY.md` | Quyết định và bài học bền vững đã được xác nhận |
| `HUONG-DAN.md` | Hướng dẫn cài đặt riêng cho nền tảng |

## Vì sao cần bộ này?

Model có thể rất mạnh nhưng vẫn bước vào project với nhiều khoảng trống. Nó chưa biết mục tiêu thật, ai chịu trách nhiệm kết quả, nguồn nào đáng tin, việc gì cần hỏi trước, người dùng thích cộng tác thế nào và quyết định cũ nào còn hiệu lực.

Bộ file này biến những điều đó thành ngữ cảnh có cấu trúc. Nhờ vậy AI giảm hỏi lại, ít đoán sai phạm vi, giữ cách làm việc ổn định hơn giữa các phiên và có tiêu chí rõ để biết khi nào đầu ra thực sự hoàn thành.

Nếu không dùng bộ này, AI vẫn hoạt động. Người dùng sẽ phải nhắc lại bối cảnh thường xuyên hơn, còn chất lượng dễ dao động theo từng phiên và từng cách đặt câu hỏi.

## Bộ này có và không có gì?

| Có | Không |
|---|---|
| Danh tính và vai trò rõ | Không thay model hoặc làm model thông minh hơn |
| Hồ sơ người dùng và project | Không cấp thêm quyền cho AI |
| Quy trình khai sinh có trạng thái | Không tự bật công cụ, connector hay truy cập mạng |
| Trí nhớ Markdown mang theo project | Không tạo tiến trình chạy nền |
| Ranh giới xác nhận và tiêu chí hoàn thành | Không thay thế sandbox, quyền ứng dụng hoặc trách nhiệm của người dùng |

## An toàn và quyền riêng tư

- Không ghi mật khẩu, API key, token, cookie, khóa riêng, mã OTP hoặc mã khôi phục vào các file Markdown.
- Chỉ lưu dữ liệu cá nhân thực sự cần để cộng tác.
- Mức tự chủ trong `USER.md` là thỏa thuận làm việc. Nó không vượt qua quyền, sandbox hoặc chế độ phê duyệt của nền tảng.
- Gửi tin, đăng công khai, triển khai thật, chi tiền, đổi quyền truy cập, xóa dữ liệu hoặc hành động khó khôi phục vẫn cần người dùng cho phép riêng.
- Hãy đọc lại hồ sơ trước khi commit hoặc chia sẻ project công khai.

## Cơ sở kỹ thuật

Thiết kế được đối chiếu ngày **2026-08-29** với tài liệu chính thức:

- [OpenAI Codex: Custom instructions with AGENTS.md](https://developers.openai.com/codex/guides/agents-md)
- [Anthropic: Organize work with Cowork Projects](https://claude.com/docs/cowork/guide/projects)
- [Google Antigravity: Rules and workspace context](https://antigravity.google/docs/rules-workflows/)
- [Google Antigravity: Best practices for AGENTS.md](https://antigravity.google/docs/cli/best-practices/)

## Phiên bản và giấy phép

Phiên bản hiện tại: **3.0.0**.

MIT License. Xem [LICENSE](LICENSE).
