student = ("Diep", 25, "female", "Diep")
print(student)

# dem so lan phan tu xuat hien trong danh sach
print(student.count("Diep"))
print(student.index("female"))

for i, val in enumerate(student, start=1):
    print(f"{i}. {val}")

if "Diep" in student:
    print("True")

#  slicing -----------------------
numbers = (22, 3, 4, 18.5, 6, 8, 20, 680)
numbers[1:3]
numbers[:2]
numbers[2:]
numbers[:]
numbers[::3] # step
numbers[::-1] # dao nguoc danh sach
numbers[-4]
numbers[-4:-2]