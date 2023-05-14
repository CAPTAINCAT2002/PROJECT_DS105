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

![image](https://github.com/CAPTAINCAT2002/PROJECT_DS105/assets/133556107/2e40c255-5304-4e7e-982c-a508e4d7551c)


# 3. PHÂN TÍCH THĂM DÒ DỮ LIỆU

Đầu tiên, chúng tôi có cái nhìn tổng quan về biến target price. Chúng tôi thấy hiện
nay laptop trên thị trường tập trung nhiều nhất ở phân khúc từ 200 đến dưới 1000 đô.Tuy nhiên, ta thấy có một số laptop có giá rất cao trên 5000 đô, thì đây hầu như là các máy chơi gaming, hoặc dành cho creator chuyên nghiệp. Bên cạnh các mẫu laptop giá rẻ chiếm đa số trên thị trường. 

![image](https://github.com/CAPTAINCAT2002/PROJECT_DS105/assets/133556107/0752d803-234f-405f-8038-3f809f7fee10)
![image](https://github.com/CAPTAINCAT2002/PROJECT_DS105/assets/133556107/2ae6d8a5-194f-4626-8420-4d449d9ac7f2)
![image](https://github.com/CAPTAINCAT2002/PROJECT_DS105/assets/133556107/fa37222b-5258-4594-a196-9052bfa2f4c3)
![image](https://github.com/CAPTAINCAT2002/PROJECT_DS105/assets/133556107/e13d6faa-ef7a-41a4-b512-122b7794d085)
![image](https://github.com/CAPTAINCAT2002/PROJECT_DS105/assets/133556107/d45e8f69-f422-4439-b43e-68e14cf0fdce)
![image](https://github.com/CAPTAINCAT2002/PROJECT_DS105/assets/133556107/4877b97c-04d9-4c30-98a9-ff3ba9778d7b)
![image](https://github.com/CAPTAINCAT2002/PROJECT_DS105/assets/133556107/8c452602-9e24-40ae-8cf5-bd1b530b112b)
![image](https://github.com/CAPTAINCAT2002/PROJECT_DS105/assets/133556107/5677649c-c76c-4d47-92d9-e276d8792712)
![image](https://github.com/CAPTAINCAT2002/PROJECT_DS105/assets/133556107/202f9e14-0625-4a89-a3aa-2f32fb03eaea)
![image](https://github.com/CAPTAINCAT2002/PROJECT_DS105/assets/133556107/f95ee091-e8e0-435f-b4c7-be363d5c9635)










