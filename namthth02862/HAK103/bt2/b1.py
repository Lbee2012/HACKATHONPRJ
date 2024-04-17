#          PYTHON BASIC DATA TYPE
'''
+ Str (String): Kiểu chuỗi hay gọi là kiểu ký tự chữ
+ Int (integer): Kiểu số nguyên, số nguyên dương hoặc âm chứ không phải thập phân hay số phẩy
+ Bool (Boolean): Kiểu true/false, đúng sai
'''

# GIẢI QUYẾT BÀI TOÁN VẤN ĐỀ
"""Dữ liệu đầu vào thí sinh"""
print("============= Bài toán \"Đặt vấn đề\" [START] ===========")
name = "Nam"
year = 2007
mark = 10

if(mark < 5):
    print("Trượt rồi thím, đóng 600 học lại")
if(mark > 5): 
    print("Quá đỉnh, quá xuất sắc, xuất sắc cái con khỉ, bạn đã đỗ")

print("============= Bài toán \"Đặt vấn đề\" [END] =============")


# KIỂM TRA DATA TYPE CỦA 1 BIẾN
"""Sử dụng lệnh: type"""
print(type(name))
"""Trong đó biến \"name\" là 1 kiểu chuỗi ===> Output: str (string/chuỗi)"""

# GÁN NHIỀU BIẾN VÀO MỘT GIÁ TRỊ
a = b = c = 10
print("a = ", a)
print("b = ", b)
print("c = ", c)

# GÁN LIÊN TIẾP GIÁ TRỊ VÀO CÁC BIẾN
d, e, f = 99, True, "HALLO"
print("d = ", d)
print("e = ", e)
print("f = ", f)

# TOP CÁC TỪ KHÓA KHÔNG ĐƯỢC ĐẶT THEO HÀM
'''
AND
- Dùng trong câu lệnh điều kiện, dùng để lấy so sánh của cả 2 biến
'''
so1, so2 = 4, 3
if so1 > so2 and so1 < 10:
    print(f"{so1} lớn hơn {so2} và bé hơn 10")
else:
    print(f"{so1} đéo ổn định")


'''
AS
- Dùng để bí danh chỉ định thay cho tên, hay dùng trong import
'''
import os as m

'''
BREAK
- Phá vỡ vòng lặp ngay lập tức
'''
array = [1, 2, 3, 4, 5]
for number in array:
    if(number == 4):
        print(f"Vòng lặp đã bị phá vỡ khi biến number trả về là số {number}")
        break

