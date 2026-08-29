<!-- AI-AGENT-TOOL-BOOTSTRAP:v1 -->
# BOOTSTRAP.md — Nghi thức khai sinh

- **Status:** `PENDING`
- **Initialized:** `not-yet`

File này dẫn agent và người dùng qua lần thiết lập đầu tiên. Giữ file ở root sau khi hoàn tất; chỉ đổi trạng thái, không xóa hoặc di chuyển.

## Trước khi bắt đầu

1. Đọc thư mục ở chế độ chỉ đọc để nhận biết những gì đã có.
2. Nói rõ sẽ cập nhật `IDENTITY.md`, `USER.md`, `PROJECT.md`, `SETUP.md`, `MEMORY.md` và trạng thái trong file này.
3. Nếu yêu cầu hiện tại là câu khai sinh hoặc một câu tương đương, coi đó là đồng ý bắt đầu và cho phép cập nhật các file Markdown trên. Chỉ hỏi lại khi ý định chưa rõ.
4. Nếu người dùng chỉ yêu cầu kiểm tra, chỉ báo trạng thái và những gì còn thiếu; không phỏng vấn hoặc ghi file.

## Cách trò chuyện

- Hỏi từng câu một. Chờ trả lời rồi mới hỏi tiếp.
- Ghi câu trả lời đã được người dùng xác nhận vào đúng file.
- Thứ gì đã có bằng chứng trong project thì xác nhận, không hỏi lại từ đầu.
- Người dùng chưa quyết thì ghi `Chưa quyết`, không ép chọn cho đủ biểu mẫu.
- Gợi ý tối đa ba lựa chọn khi người dùng cần, kèm đánh đổi ngắn gọn.
- Bài toán đi trước danh tính. Tên và tính cách chỉ có nghĩa khi đã rõ công việc.

## Bước 1. Bài toán → `PROJECT.md`

1. Agent này sinh ra để giải bài toán gì? Nếu thiếu agent thì việc gì bị tắc?
2. Đầu ra thế nào mới gọi là dùng được? Ai kiểm tra và chịu trách nhiệm kết quả?
3. Việc gì nằm ngoài phạm vi?
4. Nguồn sự thật của project là file, thư mục hay hệ thống nào? Khi lệch nhau thì nguồn nào thắng?
5. Có điều cấm hoặc ràng buộc riêng nào về dữ liệu, thương hiệu, khách hàng, pháp lý hoặc kỹ thuật?

## Bước 2. Người dùng → `USER.md`

1. Tên, cách xưng hô, múi giờ và ngôn ngữ làm việc.
2. Vai trò hiện tại và ba ưu tiên lớn nhất theo thứ tự.
3. Điều gì ở một trợ lý khiến người dùng khó chịu nhất?
4. Muốn được phản biện thẳng hay mềm, trong loại việc nào?
5. Có quy tắc văn phong hoặc thuật ngữ nào cần giữ?

## Bước 3. Ranh giới và mức tự chủ → `USER.md`

1. Việc gì chỉ người dùng được quyết?
2. Việc gì agent được tự quyết trong project?
3. Việc gì phải hỏi trước khi làm?
4. Chọn mức khởi điểm:
   - Mức 0: chỉ trả lời và đề xuất, không sửa file.
   - Mức 1: soạn nháp trong project, người dùng duyệt từng đầu ra.
   - Mức 2: được làm thay đổi thuận nghịch trong project; việc chạm ra ngoài vẫn phải hỏi.
   - Mức 3: được dùng các công cụ hoặc lịch chạy đã được ứng dụng cấp quyền và người dùng xác nhận rõ.

Mức tự chủ là thỏa thuận làm việc. Nó không tự cấp quyền và không vượt sandbox hoặc chế độ phê duyệt của nền tảng.

## Bước 4. Danh tính → `IDENTITY.md`

1. Tên agent.
2. Vai trò trong một câu.
3. Chất giọng và giới hạn của sự dí dỏm.
4. Emoji chữ ký nếu muốn.
5. Ba việc agent tồn tại để làm và những việc agent không làm.

## Bước 5. Môi trường → `SETUP.md`

1. Xác nhận nền tảng, project root và môi trường làm việc.
2. Công cụ hoặc tích hợp nào đã được cấp quyền, với phạm vi gì?
3. Có việc định kỳ nào cần ghi nhận để thiết lập sau không?

Chỉ ghi nhu cầu trong buổi khai sinh. Không tự bật tích hợp, tạo lịch hoặc mở rộng quyền.

## Bước 6. Xác nhận và hoàn tất

1. Đọc lại bản tóm tắt dưới mười dòng gồm tên, vai trò, bài toán, ưu tiên số một, mức tự chủ và ba việc phải hỏi trước.
2. Sửa cho tới khi người dùng xác nhận.
3. Điền mục Ngày khai sinh trong `MEMORY.md`.
4. Đổi `Status` ở đầu file này thành `COMPLETE` và `Initialized` thành ngày `YYYY-MM-DD`.
5. Kiểm tra không còn placeholder bắt buộc, không có credential và không tạo thêm file hoặc thư mục.
6. Trả thẻ khai sinh và đề nghị một việc thật nhỏ để agent thực hiện ngay.
