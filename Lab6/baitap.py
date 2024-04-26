# Cho một mảng các số nguyên được lưu dưới dạng cấu trúc dữ liệu list như sau:
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Hãy dùng kiến thức đã học để tạo các list mới dựa vào mảng đã cho, với tính chất:
# Mảng dịch 2: Chứa các giá trị như mảng đã cho, nhưng dịch chuyển 2 vị trí về bên trái. 2 giá trị đầu tiên được đưa về cuối mảng.
# for i in range(2, len(arr)):
#     temp = arr[i]
#     arr.remove(arr[i])
#     arr.insert(i - 2, temp)

# print(arr)


# Cho một mảng chứa thông tin của một chuỗi ký tự đã được mã hóa như sau:
arr = [
    "l",
    "o",
    "o",
    "h",
    "c",
    "S",
    " ",
    "y",
    "g",
    "o",
    "l",
    "o",
    "n",
    "h",
    "c",
    "e",
    "T",
    " ",
    "X",
    "d",
    "n",
    "i",
    "M",
]
# Hãy tìm quy luật mã hóa và xây dựng lại chuỗi ký tự ban đầu. Kết quả mong đợi của chương trình là chuỗi ký tự trước khi được mã hóa.
# arr.reverse()
# print(arr)

# Dãy Fibonacci là một dãy vô hạn các số nguyên với tính chất: Giá trị của một phần tử bằng tổng giá trị hai phần tử đứng trước nó.
# Dãy Fibonacci bắt đầu bằng hai phần tử có giá trị 1 và có các phần tử đầu tiên như sau:
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# Hãy viết một chương trình in ra n phần tử đầu tiên của dãy Fibonacci, với n là một số nguyên dương do người dùng nhập.
# user_range = int(input("Range: "))
# arr = [1, 1]

# def printList (arr):
#     result = "Fibonacci number(s):"
#     for item in arr:
#         result += str(item) + " "
#     return result

# if user_range < 3:
#     print(printList(arr[:user_range]))
# else:
#     for i in range(len(arr),user_range):
#         new_item = arr[i-1] + arr[i-2]
#         arr.insert(i, new_item)
#     print(printList(arr))


# Hôm nay là ngày nhận lương của Bình. Bình tự thưởng cho mình bằng cách ăn một bữa thật ngon ở nhà hàng.
# Thực đơn của nhà hàng bao gồm n món với các giá khác nhau. Bình chỉ muốn chọn món ăn từ các món có giá trên trung bình. Hãy viết chương trình giúp Bình tìm giá trung bình và lọc ra các món có giá trên trung bình từ thực đơn.
# num_of_item = int(input("Number of item in menu: "))
# menu = []
# for i in range(num_of_item):
#     name = input(f"Name of item {i} : ")
#     price = float(input(f"Price of item {i} : "))
#     menu.append((name, price))


# def avgPrice(arr):
#     my_sum = 0
#     for i in arr:
#         my_sum += i[1]
#     return round((my_sum / num_of_item) * 100) / 100


# avg = avgPrice(menu)
# print("Average price:", avg)
# result = "Item(s) above average price: "
# for i in menu:
#     if i[1] > avg:
#         result += str(i) + ", "

# print(result)


# Cho một câu bao gồm nhiều từ được nhập từ người dùng. Hãy đếm số từ xuất hiện trong câu đó. Nếu một từ xuất hiện nhiều hơn 1 lần, ta chỉ đếm 1.
# Để đơn giản, người dùng chỉ nhập các chữ cái viết thường và dấu cách, không nhập chữ viết hoa và các dấu câu khác.
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split(" ")
# unique_words = []

# for i in range(len(words)):
#     if not words[i] in unique_words:
#         unique_words.append(words[i])

# print(len(unique_words))

n = 0
while True:
    if n >= len(words):
        break
    else:
        if words.count(words[n]) > 1:
            words.remove(words[n])
            continue
        else:
            n+=1
            continue
print(len(words))
