File game XO: demo_Caro.py
File game XO beta (terminal): tutorial.py

Hướng dẫn sử dụng:

*** tutorial.py:
- Nhập lần lượt số hàng và cột của bàn cờ
- Nhập tọa độ của điểm cần đánh dấu dưới dạng str: '{0x} {0y}' ( X và O thay phiên nhau )

*** demo_Caro.py
* Chế độ chơi với người
  - Nhập số hàng và cột vào 2 entry tương ứng, nhấn bắt đầu chơi để khởi tạo bàn cờ
  - Trải nghiệm trò chơi XD
* Chế độ chơi với máy
  - Lựa chọn đánh X hoặc O
  - Hành hạ máy thôi chứ còn chờ gì

Sửa đổi hàm heuristic:
- Bỏ qua những tọa độ nếu vị trí đằng trước nó là điểm cùng kiểu ( chỉ lấy những điểm ngoài cùng )
- Bỏ qua những điểm mà 2 ô liên tiếp trên cạnh đều là khoảng trống ( tồi )
