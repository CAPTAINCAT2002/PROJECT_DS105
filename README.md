# PROJECT_DS105
# PHÂN TÍCH CÁC YẾU TỐ ẢNH HƯỞNG ĐẾN  GIÁ LAPTOP VÀ DỰ ĐOÁN
# 1. GIỚI THIỆU 

  Chúng tôi xây dựng bộ dữ liệu bao gồm về thông số cấu hình, giá cả của những chiếc laptop và xây dựng mô hình máy học dự đoán.
  
# 2. DỮ LIỆU
## 2.1. Quy trình thu thập bộ dữ liệu

  Chúng tôi quyết định tự xây dựng bộ dữ liệu và thực hiện thu thập dữ liệu từ 3
nguồn khác nhau, bao gồm:
− amazon.com (là nguồn chính để lấy danh sách và thông tin laptop).
− cpubenchmark.net và notebookcheck.net (thu thập thông tin về xếp hạng
cũng như hiệu năng của từng CPU và Card đồ hoạ của Laptop).

## 2.2. Tiền xử lý dữ liệu

Phần tiền xử lý gồm các bước:
− Xóa cột dư thừa & cột có tỷ lệ missing data cao
− Trích thông tin cần thiết từ một số cột, tạo cột mới, feature engineering
− Điền các giá trị bị khuyết

## 2.3. Khảo sát bộ dữ liệu

Sau khi thực hiện bước tiền xử lý dữ liệu, file dữ liệu sạch (Tidy Data) có kích
thước 378 KB, bao gồm 1159 dòng dữ liệu và 24 thuộc tính. Thông tin cụ thể của các
thuộc tính được thể hiện ở bảng sau:
![image](https://github.com/CAPTAINCAT2002/PROJECT_DS105/assets/133556107/e3737525-49c0-4038-9863-99fd82027d38)


# 3. 
