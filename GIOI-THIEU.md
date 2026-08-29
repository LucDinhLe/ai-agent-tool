# AI đã đủ mạnh. Điều còn thiếu là một bộ hồ sơ để nó hiểu đúng dự án của bạn

*AI Agent Tool dùng tám file Markdown để khai sinh hồ sơ làm việc cho Codex, Claude Cowork và Google Antigravity.*

Bạn mở một project mới, giao cho AI một việc tưởng như rất rõ. Nó bắt đầu nhanh, viết trôi chảy và dùng công cụ rất thành thạo. Vài phút sau, bạn nhận ra nó chọn sai nguồn, hiểu lệch đối tượng, sửa nhầm phạm vi hoặc tạo một đầu ra đẹp nhưng chưa dùng được.

Bạn bổ sung bối cảnh. AI sửa lại. Sang phiên mới, một phần thông tin biến mất và bạn lại giải thích từ đầu.

Model đã có năng lực tổng quát. Phần còn thiếu là hồ sơ của người dùng và dự án cụ thể mà nó đang phục vụ.

Đó là lý do tôi xây dựng **AI Agent Tool**.

## Vì sao một model mạnh vẫn làm việc kém hiệu quả?

Một AI agent chỉ có thể hành động tốt khi nó biết đủ bốn điều:

1. Nó đang phục vụ ai và cần cộng tác theo cách nào.
2. Dự án đang giải bài toán gì, phạm vi kết thúc ở đâu.
3. Nguồn nào là nguồn sự thật và đầu ra nào mới được gọi là hoàn thành.
4. Việc gì được tự làm, việc gì cần hỏi và quyết định nào phải được giữ cho phiên sau.

Thiếu một trong bốn lớp này, agent vẫn có thể tạo nội dung hoặc mã nguồn. Khả năng tạo ra **kết quả dùng được** có thể giảm vì người dùng phải bù lại bằng prompt dài, nhiều vòng sửa và kiểm tra thủ công.

Tôi dùng một mô hình tư duy đơn giản:

`Hiệu suất hữu dụng ≈ Năng lực model × Bối cảnh đúng × Mục tiêu rõ × Kỷ luật xác minh`

Đây chưa phải công thức thực nghiệm. Nó giúp chỉ ra một sự thật rất thực tế: model mạnh đến đâu cũng khó cứu một dự án có bối cảnh sai, mục tiêu mơ hồ hoặc tiêu chí hoàn thành không tồn tại.

## Ba nhà phát triển lớn đang hướng dẫn điều gì?

Tên gọi khác nhau, nhưng hướng thiết kế của các nền tảng đang hội tụ.

[OpenAI hướng dẫn Codex đọc `AGENTS.md` trước khi làm việc](https://developers.openai.com/codex/guides/agents-md) và xây chuỗi chỉ dẫn áp dụng cho thư mục hiện tại. Một file ở project root có thể tạo kỳ vọng nhất quán cho toàn dự án.

[Anthropic thiết kế Cowork Projects](https://claude.com/docs/cowork/guide/projects) để gom thư mục, chỉ dẫn thường trực của project và bộ nhớ theo project vào cùng một không gian làm việc. Project Instructions được áp dụng cho mọi tác vụ và phiên trong project.

[Google hướng dẫn Antigravity CLI đặt `AGENTS.md` hoặc `GEMINI.md` ở workspace root](https://antigravity.google/docs/cli/best-practices/) để công cụ đọc quy tắc khởi động trước khi đưa ra đề xuất. [Projects và Local Mode](https://antigravity.google/docs/projects) xác định thư mục và môi trường mà agent được làm việc trực tiếp.

Từ ba cơ chế trên có thể rút ra một nguyên tắc chung. Hiệu suất của agent là kết quả của cả một hệ thống gồm model, chỉ dẫn, bối cảnh, quyền truy cập và quy trình xác minh. Chỉ nâng model thường chưa giải quyết được phần bối cảnh đang bị thất lạc.

## AI Agent Tool là gì?

AI Agent Tool là một bộ mã nguồn mở gồm **tám file Markdown phẳng**. Người dùng tải đúng gói, chép tám file vào vị trí gốc được hướng dẫn riêng cho nền tảng, làm theo bước kích hoạt rồi bắt đầu cuộc trò chuyện khai sinh.

Không có phần mềm thực thi, thư mục ẩn, skill hay plugin phải cài thêm. Bộ file cũng không tạo một custom agent mới trong menu. Nó tạo **hồ sơ vận hành cho agent đã có sẵn trong project**.

Tám file đảm nhiệm tám phần việc:

- `AGENTS.md` là file cửa vào được Codex và Antigravity nhận diện theo tài liệu chính thức. Trong gói Claude Cowork, `CLAUDE.md` là hồ sơ đầu mối được Project Instructions yêu cầu đọc trước mỗi tác vụ.
- `BOOTSTRAP.md` dẫn cuộc trò chuyện khai sinh từng bước và giữ trạng thái `PENDING` hoặc `COMPLETE`.
- `IDENTITY.md` định nghĩa tên, vai trò, chất giọng, nhiệm vụ cốt lõi và tiêu chuẩn nghề nghiệp.
- `USER.md` ghi cách xưng hô, ưu tiên, cách phản biện, quyền quyết định và mức tự chủ.
- `PROJECT.md` xác định bài toán, phạm vi, nguồn sự thật, ràng buộc và tiêu chí hoàn thành.
- `SETUP.md` ghi môi trường, công cụ, quyền đã được xác nhận và những sự cố cần nhớ.
- `MEMORY.md` giữ các quyết định và bài học bền vững, có nguồn xác nhận và trạng thái rõ ràng.
- `HUONG-DAN.md` chỉ cách cài và kiểm tra riêng cho từng nền tảng.

Toàn bộ hồ sơ nằm ngay trong project. Người dùng có thể đọc, sửa, theo dõi lịch sử khi các file được commit vào Git và mang chúng theo khi chuyển máy hoặc chuyển phiên.

## Bộ tool mở khóa hiệu suất bằng cách nào?

### 1. Giảm “thuế giải thích lại”

Khi thông tin về người dùng, dự án và môi trường chỉ nằm trong cuộc trò chuyện, mỗi phiên mới có thể trở thành một buổi nhập môn lại từ đầu. Bộ file chuyển phần bối cảnh ổn định sang một nơi agent được yêu cầu đọc trước khi làm việc.

Khi file cửa vào được nền tảng nạp và hồ sơ được duy trì đúng, người dùng có thể dành ít thời gian hơn cho việc nhắc lại đối tượng, chất giọng, nguồn tài liệu, cấu trúc thư mục và những điều đã chốt.

### 2. Giảm nguy cơ làm đúng việc nhỏ nhưng sai bài toán lớn

`PROJECT.md` yêu cầu làm rõ những câu thường bị bỏ qua: đầu ra dùng được nghĩa là gì, ai kiểm tra, nguồn nào thắng khi dữ liệu mâu thuẫn, việc gì nằm ngoài phạm vi và bằng chứng nào phải có trước khi báo hoàn thành.

Agent nhờ đó có một chiếc la bàn rõ hơn và có cơ sở để biết khi nào nên tiếp tục, khi nào cần dừng và khi nào phải hỏi người dùng.

### 3. Giảm số vòng sửa

`IDENTITY.md` và `USER.md` giúp agent giữ vai trò, chất giọng và cách phản biện ổn định hơn. File cửa vào còn yêu cầu đọc bằng chứng trước khi hỏi, giữ nguyên thay đổi không liên quan và xác minh kết quả trước khi gọi là hoàn thành.

Giá trị lớn nhất thường xuất hiện trong công việc lặp lại. Khi hồ sơ được nạp và duy trì đúng, mỗi prompt giải thích, lần sửa sai phạm vi hoặc quyết định phải tìm lại được cắt giảm sẽ tạo phần tiết kiệm cộng dồn qua nhiều phiên.

### 4. Tạo trí nhớ ngoài có thể kiểm toán

Mẫu `MEMORY.md` hướng dẫn chỉ giữ quyết định và bài học đã được xác nhận, thay vì lưu toàn bộ hội thoại. Khi có quyết định mới, quy tắc của file yêu cầu giữ dòng cũ và đánh dấu `superseded`.

Khi quy tắc đó được tuân thủ, trí nhớ có thể trở thành một tài sản của project thay vì một cảm giác mơ hồ rằng “chắc AI vẫn còn nhớ”. Đây là lớp trí nhớ do người dùng trực tiếp quản lý, bổ sung cho bộ nhớ project do Cowork cung cấp. Hai lớp có thể tồn tại song song; quyết định quan trọng nên được ghi vào file nếu người dùng muốn đọc, sửa, sao lưu hoặc chuyển giao nó.

### 5. Làm rõ mức tự chủ trong một ranh giới rõ

Người dùng có thể quy định việc nào agent được tự quyết, việc nào chỉ được soạn nháp và việc nào luôn phải xin phép. Cấu trúc này có thể giảm cả hai kiểu lãng phí: agent hỏi quá nhiều ở những việc an toàn và agent đi quá xa ở những việc có hậu quả thật.

Mức tự chủ trong bộ file chỉ là thỏa thuận làm việc. Quyền thực vẫn do nền tảng, sandbox, connector và người dùng kiểm soát.

## “Tăng x lần” phải được đo như thế nào?

Không có một con số x chung cho mọi người và mọi dự án. Một workflow đang mất nhiều thời gian để briefing và sửa sai có thể cải thiện rất lớn. Một nhiệm vụ chỉ làm một lần hoặc một project đã có hệ chỉ dẫn tốt sẽ cải thiện ít hơn.

Cách đo đơn giản nhất là:

`Hệ số cải thiện = Thời gian cũ để có đầu ra đạt chuẩn / Thời gian mới để có đầu ra đạt chuẩn`

Ví dụ minh họa, nếu trước đây cần 90 phút để đi từ yêu cầu tới đầu ra được chấp nhận và sau khi chuẩn hóa chỉ còn 30 phút, workflow đó đạt 3x. Đây là kết quả của workflow đang được đo, không phải lời hứa chung cho sản phẩm.

Muốn đánh giá nghiêm túc, hãy chọn năm tác vụ lặp lại, giữ nguyên model, quyền truy cập và tiêu chí chấp nhận rồi đo trước và sau theo bốn chỉ số:

- Tổng thời gian tới đầu ra đạt chuẩn.
- Số prompt người dùng phải gửi.
- Số vòng sửa đáng kể.
- Số lỗi do quên bối cảnh hoặc đi sai phạm vi.

Nếu ai tuyên bố 10x nhưng không đo thời gian tới đầu ra đạt chuẩn, con số đó mới dừng ở khẩu hiệu.

## Một ví dụ rất đời thường

Bạn giao cho agent: “Làm landing page cho chương trình AI dành cho chủ doanh nghiệp nhỏ.”

Khi chưa có hồ sơ project, agent phải đoán đối tượng, chất giọng, nguồn nội dung, lời kêu gọi hành động, cấu trúc kỹ thuật và quyền triển khai. Nó có thể tạo ra một trang đẹp nhưng sai định vị hoặc tự tiến gần môi trường thật hơn mức người dùng mong muốn.

Sau buổi khai sinh, agent có thể đọc ngay:

- Trong `USER.md`, người dùng ưu tiên sự rõ ràng, ghét lời quảng cáo phóng đại và giữ quyền quyết định thương hiệu.
- Trong `PROJECT.md`, nguồn sự thật là đề cương khóa học đã duyệt, đối tượng là chủ SME và đầu ra chỉ đạt khi vượt checklist cụ thể.
- Trong `SETUP.md`, agent biết công cụ nào đã được cấp quyền và môi trường nào chỉ dùng để thử nghiệm.
- Trong `MEMORY.md`, agent thấy lời kêu gọi hành động và mức giá cũ đã bị một quyết định mới thay thế.

Agent có thể bắt đầu gần đúng hơn, kiểm tra đúng thứ cần kiểm tra và dừng trước hành động cần phê duyệt. Năng lực model giữ nguyên. Chất lượng của hệ thống làm việc đã thay đổi.

## Cách cài cho từng nền tảng

### OpenAI Codex

1. Tải gói Codex và chép tám file vào project root.
2. Mở một phiên Codex mới để chuỗi chỉ dẫn được dựng lại.
3. Nói: `Bắt đầu khai sinh agent cho dự án này`.
4. Trả lời từng câu và xác nhận bản tóm tắt cuối.
5. Kiểm tra `BOOTSTRAP.md` đã chuyển sang `Status: COMPLETE`.

### Claude Cowork

1. Tải gói Claude Cowork và chép tám file vào thư mục local đầu tiên của project.
2. Đặt Project Instructions thành: `Trước mọi tác vụ, đọc CLAUDE.md trong thư mục local đầu tiên của project và làm theo. Nếu BOOTSTRAP.md có Status: PENDING, chỉ chạy quy trình khai sinh khi tôi yêu cầu.`
3. Mở một Cowork session mới.
4. Nói: `Bắt đầu khai sinh agent cho dự án này`.
5. Trả lời từng câu và kiểm tra trạng thái `COMPLETE`.

Trong Cowork cloud, file local mà Claude mở qua Desktop được xử lý trên máy chủ Anthropic, dù quyền truy cập vẫn giới hạn vào các folder bạn đã kết nối. [Anthropic khuyến nghị giới hạn thư mục được gắn và điều chỉnh mức giám sát theo độ nhạy của công việc](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely). Không đặt mật khẩu, API key, token hoặc dữ liệu nhạy cảm không cần thiết vào bộ hồ sơ.

### Google Antigravity

1. Tải gói Antigravity và chép tám file vào workspace root.
2. Với Antigravity Desktop, mở cuộc trò chuyện mới trong Local Mode.
3. Nói: `Đọc AGENTS.md ở root của thư mục này, rồi bắt đầu khai sinh agent cho dự án này`.
4. Với Antigravity CLI, khởi động CLI tại workspace root rồi nói câu khai sinh ngắn.
5. Trả lời từng câu và kiểm tra trạng thái `COMPLETE`.

CLI có cơ chế đọc `AGENTS.md` ở root theo tài liệu chính thức. Với Desktop, câu gọi rõ tên file giúp việc kích hoạt minh bạch và dễ kiểm tra hơn.

## Bộ tool này không làm gì?

AI Agent Tool không thay model, cấp thêm quyền, mở connector, truy cập mạng, chạy ngầm hoặc tạo một native custom agent. Nó cũng không loại bỏ hoàn toàn hiện tượng bịa thông tin của AI.

Hồ sơ cũ hoặc sai có thể khiến agent làm sai một cách nhất quán hơn. Vì vậy, người dùng cần rà lại `USER.md`, `PROJECT.md` và `MEMORY.md` khi mục tiêu, ưu tiên hoặc quyết định lớn thay đổi.

Với công việc pháp lý, y tế, tài chính, dữ liệu thật hoặc hành động khó khôi phục, con người vẫn phải giữ trách nhiệm cuối cùng và tăng mức kiểm tra phù hợp.

## Bắt đầu từ một project thật

Đừng thử bộ này bằng một câu hỏi chung chung. Hãy chọn một project đang khiến bạn phải giải thích lại nhiều lần, cài bộ file, hoàn tất buổi khai sinh rồi giao ngay một việc nhỏ có tiêu chí rõ.

Bạn sẽ biết bộ tool có giá trị hay không bằng một câu hỏi rất thực tế: **thời gian từ yêu cầu tới đầu ra được chấp nhận đã giảm bao nhiêu?**

- [Xem mã nguồn AI Agent Tool](https://github.com/LucDinhLe/ai-agent-tool)
- [Tải AI Agent Tool cho Codex](https://github.com/LucDinhLe/ai-agent-tool/releases/latest/download/AI-Agent-Tool-Codex.zip)
- [Tải AI Agent Tool cho Claude Cowork](https://github.com/LucDinhLe/ai-agent-tool/releases/latest/download/AI-Agent-Tool-Claude-Cowork.zip)
- [Tải AI Agent Tool cho Google Antigravity](https://github.com/LucDinhLe/ai-agent-tool/releases/latest/download/AI-Agent-Tool-Antigravity.zip)

AI agent hiện nay đã đủ mạnh để làm nhiều việc thật. Khi file cửa vào được nền tảng nạp, hồ sơ còn cập nhật và agent làm theo chỉ dẫn, một project có hồ sơ rõ có thể giúp sức mạnh đó đi đúng hướng qua nhiều phiên và tạo ra kết quả mà con người dễ kiểm tra, chịu trách nhiệm và tiếp tục cải thiện hơn.

*Bài viết đối chiếu tài liệu chính thức ngày 29/08/2026. Tác giả dự án không liên kết hoặc đại diện cho OpenAI, Anthropic hay Google.*
