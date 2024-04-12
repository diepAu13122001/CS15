from random import *

score = 0
result = True
while result:
    # tao ra bieu thuc (a, b, phep toan, ket qua dung - sai)
    a = randint(0, 10)
    b = randint(1, 10)
    operator = choice(["*", "/", "+", "-"])
    ans_false = randint(-50, 50)
    # kiem tra phep toan => tinh ket qua dung
    if operator == "*":
        ans_true = a * b
    elif operator == "/":
        ans_true = a / b
    elif operator == "+":
        ans_true = a + b
    else:
        ans_true = a - b
    # in ra man hinh
    ans = choice([ans_false, ans_true])
    print(str(a) + operator + str(b) + " = " + str(ans))
    user_ans = int(input("0 is True, 1 is False: "))
    # xet ket qua cua nguoi dung
    if (user_ans == 0):
        if (ans == ans_true):
            score+=1
            print(f"Score: {score}")
            continue
        else:
            print("Game over")
            result = False
            break
    if (user_ans == 1):
        if (ans == ans_false):
            score+=1
            print(f"Score: {score}")
            continue
        else:
            print("Game over")
            result = False
            break