# HƯỚNG DẪN — Khai sinh một agent trong Claude Cowork

_Dành cho người lần đầu dựng agent. Làm theo thứ tự, mất khoảng 45 phút cho lần đầu. Không cần biết lập trình._

## Bộ này gồm gì

| File | Ai đọc | Để làm gì |
|---|---|---|
| `HUONG-DAN.md` | Bạn | File này. Đọc xong có thể xoá hoặc giữ |
| `CLAUDE.md` | Agent, đầu mỗi phiên | Luật chung của agent. Không cần sửa lúc đầu |
| `COWORK-PROJECT-INSTRUCTIONS.txt` | Bạn, một lần | Đoạn dán vào Project Instructions của Cowork để agent luôn đọc `CLAUDE.md` trước |
| `BOOTSTRAP.md` | Agent, đúng một lần | Kịch bản buổi khai sinh. Tự biến mất khi xong |
| `IDENTITY.md` | Agent mỗi phiên | Agent là ai. Điền trong buổi khai sinh |
| `USER.md` | Agent mỗi phiên | Bạn là ai, muốn được phục vụ thế nào. Điền trong buổi khai sinh |
| `PROJECT.md` | Agent mỗi phiên | Bài toán agent sinh ra để giải. Điền trong buổi khai sinh |
| `SETUP.md` | Agent khi cần | Thư mục, connector, việc chạy theo lịch |
| `MEMORY.md` | Agent khi cần | Quyết định và bài học đã chốt, tích luỹ dần |

Ba file `IDENTITY`, `USER`, `PROJECT` là ba câu hỏi: ai làm, làm cho ai, làm việc gì. Agent tốt hay dở phần lớn nằm ở ba file này.

## Các bước

**Bước 1. Tạo thư mục cho agent.** Chép cả bộ file này vào một thư mục mới trên máy, đặt tên theo agent hoặc dự án. Mỗi agent một thư mục riêng, đừng để hai agent chung một thư mục.

**Bước 2. Nối thư mục vào Cowork và dán chỉ dẫn dự án.** Mở app Claude trên máy, vào Cowork, tạo một Project từ thư mục vừa tạo hoặc thêm thư mục đó làm thư mục làm việc. Sau đó mở `COWORK-PROJECT-INSTRUCTIONS.txt`, chép toàn bộ nội dung dán vào Project Instructions của Project đó. Bước này bảo đảm mọi phiên đều đọc `CLAUDE.md` trước, kể cả phiên chạy theo lịch. Cowork chưa cam kết tự nạp `CLAUDE.md` như Claude Code, nên đừng bỏ qua bước này.

**Bước 3. Mở phiên đầu tiên và nói một câu.** Gõ đại ý "bắt đầu đi" hoặc "chào, mình khai sinh bạn nhé". Agent thấy `BOOTSTRAP.md` còn trong thư mục sẽ tự dẫn bạn qua buổi khai sinh.

**Bước 4. Trả lời từng câu.** Agent hỏi bài toán trước, rồi mới hỏi về bạn, ranh giới, và cuối cùng là tên với tính cách. Trả lời thật, ngắn cũng được. Chỗ nào bí thì bảo agent gợi ý. Agent ghi vào file ngay sau mỗi câu, bạn có thể mở file xem song song.

**Bước 5. Nghe tóm tắt và gật.** Cuối buổi agent đọc lại một tóm tắt dưới mười dòng. Sửa cho tới khi đúng ý. Sau đó agent chuyển `BOOTSTRAP.md` vào `_archive/` và từ đây làm việc bình thường.

**Bước 6. Giao một việc nhỏ ngay.** Đừng kết thúc buổi khai sinh bằng lời chào. Giao một việc thật, nhỏ, có đầu ra trong 15 phút. Danh tính chỉ thành thật khi có đầu ra đầu tiên.

## Sau khai sinh

Mỗi phiên sau, agent đọc `CLAUDE.md` theo chỉ dẫn dự án, rồi `IDENTITY.md`, `USER.md`, `PROJECT.md`, cộng với trí nhớ dự án mà Cowork giữ trong app. Bạn không cần nhắc lại bối cảnh.

Đổi ưu tiên, đổi phạm vi, đổi quy tắc thì sửa thẳng vào `USER.md` hoặc `PROJECT.md`, hoặc bảo agent sửa rồi kiểm tra lại. Đừng chỉ nói miệng trong phiên, vì phiên sau agent không còn nhớ câu nói đó nếu chưa ghi.

Muốn agent làm việc gì theo lịch, bảo nó tạo scheduled task và ghi vào `SETUP.md`. Mỗi lần chạy theo lịch là một phiên mới không có bạn, nên chỉ giao việc theo lịch khi agent đã ở mức tự chủ 3.

## Ba lỗi hay gặp

Khai sinh xong mà không giao việc, agent có tên nhưng chưa có kinh nghiệm. Nói miệng thay đổi mà không ghi vào file, phiên sau agent quay về hiểu cũ. Cho mức tự chủ cao ngay từ đầu, hãy bắt đầu ở mức 1, nâng lên khi đã có ba đầu ra đạt liên tiếp.

## Trí nhớ nằm ở đâu

Hai chỗ. Trí nhớ dự án của Cowork nằm trong app trên máy này, giữ trạng thái từng phiên, không đi theo thư mục. `MEMORY.md` nằm trong thư mục, giữ quyết định và bài học đã chốt, bạn đọc được và chép đi máy khác được. Nếu bạn chuyển thư mục sang máy khác, agent giữ được `MEMORY.md` và ba file danh tính, mất trạng thái phiên gần nhất. Vì vậy trước khi chuyển, bảo agent ghi những gì đang dở vào `PROJECT.md` mục Trạng thái.
