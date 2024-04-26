# cach 1 --------------------------
def factorial(n):
    giai_thua = 1
    if n == 0:
        return "0! = 1"
    else:
        for i in range(1, n + 1):
            giai_thua *= i
        return f"{n}! = {giai_thua}"

number = int(input("Nhập một số nguyên: "))
print(factorial(number))

#cach 2 ------------------------------
def factorial_recursion(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursion(n-1)

