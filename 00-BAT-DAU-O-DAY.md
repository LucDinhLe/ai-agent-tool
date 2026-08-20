# Bắt đầu ở đây

## Nếu bạn tải bằng nút Code → Download ZIP

GitHub đã tải toàn bộ mã nguồn của AI Agent Tool. Sáu folder cài đặt nằm ngay ở cấp đầu:

1. `codex/`
2. `claude-code/`
3. `claude-cowork/`
4. `gemini-cli/`
5. `github-copilot/`
6. `openclaw/`

Các thư mục `docs/`, `scripts/`, `tests/` và `.github/` phục vụ phát triển bộ công cụ. Người cài chỉ cần chọn một trong sáu folder nền tảng.

## Cách tải dễ nhất

Tải trực tiếp tại [AI-Agent-Tool-CHON-NEN-TANG-v2.0.1.zip](https://github.com/LucDinhLe/ai-agent-tool/releases/download/v2.0.1/AI-Agent-Tool-CHON-NEN-TANG-v2.0.1.zip).

`AI-Agent-Tool-CHON-NEN-TANG-v2.0.1.zip`

Giải nén file này sẽ thấy ngay sáu folder ở cấp đầu:

- `01-CODEX/`
- `02-CLAUDE-CODE/`
- `03-CLAUDE-COWORK/`
- `04-GEMINI-CLI/`
- `05-GITHUB-COPILOT/`
- `06-OPENCLAW/`

## Cài vào dự án

1. Chọn đúng **một** folder theo công cụ AI đang dùng.
2. Mở folder đó, chọn toàn bộ nội dung bên trong, gồm cả các thư mục bắt đầu bằng dấu chấm.
3. Copy nội dung vào root của dự án. Không đặt cả folder `01-CODEX` hay `03-CLAUDE-COWORK` thành một thư mục con trong dự án.
4. Nếu dự án đã có file hướng dẫn AI, hãy merge nội dung thay vì ghi đè.
5. Mở phiên AI mới và dùng lệnh ghi trong `AI-AGENT-TOOL.md`.

Claude Cowork cần thêm một bước: dán nội dung `COWORK-PROJECT-INSTRUCTIONS.txt` vào Project Instructions một lần.
