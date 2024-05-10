# lambda -----------------------------------------------
# rut gon code func 1 dong
# def sum(x, y):
#     return x + y


# sum_lambda = lambda x, y: x + y
# print(sum_lambda(10, 2))

# # sort, map, filter ------------------------------------
# # sort() method = used with lists
# # sorted() function = used with iterables
# students = (
#     ("A", 12),
#     ("E", 15),
#     ("B", 13),
#     ("D", 14),
#     ("C", 11),
#     ("F", 16),
# )
# sorted_students = sorted(students)
# print(sorted_students)

# students_name = ["A", "B", "C", "D", "E", "F"]
# students_name.sort()  # A => Z
# students_name.sort(reverse=True)  # Z => A
# print(students_name)

# age = lambda item: item[1]
# sorted_ages = sorted(students, key=age)
# print(sorted_ages)

# # map() = applies a function to each item in an iterable (list, tuple, ...)
# # map(function, iterable)
# store_dollars = [("apple", 1), ("jacket", 50), ("paints", 40), ("skirt", 80)]
# def change_euros(item):
#     return (item[0], item[1] * 0.82)
# #  => lambda
# change_euros_2 = lambda item: (item[0], item[1] * 0.82)
# # store_euros = list(map((lambda item: (item[0], item[1] * 0.82)), store_dollars))
# store_euros = list(map(change_euros_2, store_dollars))
# print(store_euros)

# # filter() = creates a collection of elements from an iterable for which a func returns
# # filter(function, iterable)
# filter_students = tuple(filter((lambda item: item[1] >= 14), students))
# print(filter_students)


# List/ dictionary comprehension --------------------------------------------------
# rut gon for + lambda

# TH1 ----------------------------------------------------------------
# list = [expression for item in iterable]
cols = 5
rows = 3
new_map = []
for i in range(rows):
    col = []
    for j in range(cols):
        col.append("-")
    new_map.append(col)

print(new_map)

# way 2
new_map_2 = [["-"] * cols for i in range(rows)]
print(new_map_2)

# dictionary = {key: expression for (key, value) in iterable}
cities_in_F = {"New York": 32, "Boston": 75, "Los Angles": 100, "Chicago": 50}
cities_in_C = {
    key: round((value - 32) * (5 / 9)) for (key, value) in cities_in_F.items()
}
# TH2 ----------------------------------------------------------------
# if viet tat
print("TRUE") if 10 % 2 == 0 else print("FALSE")
# list = [expression for item in iterable if conditional]
odd_list = [item for item in range(1, 11) if item % 2 == 0]
print(odd_list)
# dictionary = {key: expression for (key, value) in iterable if conditional}
warn_cities = {key: value for (key, value) in cities_in_F.items() if value > 40}
print(warn_cities)
# TH3 ----------------------------------------------------------------
# list = [expression if/else for item in iterable]
students = [50, 40, 70, 60, 80, 100, 0]
passed_list = list(filter(lambda sc: sc >= 60, students))
new_class = [item if item >= 60 else "FALSE" for item in students]
# dictionary = {key: if/else for (key, value) in iterable}
cities_status = {
    key: "WARM" if value > 40 else "COLD" for (key, value) in cities_in_F.items()
}
print(cities_status)
# TH4 ----------------------------------------------------------------
# dictionary = {key: function(value) for (key, value) in iterable}
def check_temp(value):
    if value > 60:
        return "HOT"
    elif 40 <= value < 60:
        return "WARM"
    else:
        return "COLD"

cities_weather = {key: check_temp(value) for (key, value) in cities_in_F.items()}
print(cities_weather)
