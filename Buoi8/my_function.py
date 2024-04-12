def my_sum(a, b):
    print("sum", a + b)


def my_sum1(a:int, b:int):
    if not a.isdigit():
        return "error"
    return a + b

# call func
my_sum(12, 5)
print(my_sum1("a", "b"))
