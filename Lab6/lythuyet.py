# tuple
employee = ('Jane', 22, 'Engineer')
new_employee = list(employee)
new_employee[1] = 23
employee = tuple(new_employee)
print(employee)

# index (slicing)
cars = ['Mercedes', 'Rolls Royce', 'Lamborghini', 'Range Rover']
print(cars[-1:])

arr = [1, 2, 3, 4]
arr.append(5)
arr_2 = arr.copy()
arr = []
print(arr_2)