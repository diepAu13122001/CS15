scr = "C:\\Users\\diepa\\OneDrive\\Documents\\Working\\MindX\\CS15\\a\\test.txt"
scr2 = "C:\\Users\\diepa\\OneDrive\\Documents\\Working\\MindX\\CS15\\b\\test.txt"
text = 'Hello World\nHello World\nHello World\nHello World\nHello World\nHello World\n'
text2 = 'Hi hi hi'

# 'r' Đọc file (read) Báo lỗi nếu file không tồn tại ---------------------------
with open(scr, 'r') as file:
    file.read()

# with open(scr2, 'r') as file: 
#     file.read() # bao loi do khong co file 

# 'x' Tạo file mới (exclusive create) Báo lỗi nếu file đã tồn tại --------------
# with open(scr, 'x') as file:
#     file.write(text)  # bao loi do da co file

# with open(scr2, 'x') as file: 
#     file.write(text) 

# 'w' Xóa nội dung và ghi đè nội dung mới (write) Tạo file mới nếu file không tồn tại
with open(scr2, 'w') as file: 
    file.write(text2) 

# 'a' Thêm nội dung (append) Tạo file mới nếu file không tồn tại
with open(scr, 'a') as file: 
    file.write(text2) 

print(file.closed)