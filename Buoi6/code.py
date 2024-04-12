# sắp xếp danh sách theo thứ tự tăng dần mà không dùng hàm sort/ sorted

l1=[76, 23, 45, 12, 54, 9, 54, 76, 76]  
# sorting list using nested loops
for i in range(0, len(l1)):
    for j in range(i+1, len(l1)):
        if l1[i] >= l1[j]:
            l1[i], l1[j] = l1[j],l1[i]
 
print("Sorted List", l1)

# Không cho danh sách trùng dữ liệu
for item in l1:
    if(l1.count(item) > 1):
        l1.remove(item)

print("No duplicate item", l1)
