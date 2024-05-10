import os
import msvcrt  # Windows
import random
import time


# 1. Viết hàm khởi tạo bản đồ game.
# Tạo bản đồ rỗng
def generate_map(rows, cols):
    map = []
    # for r in range(rows):
    #     for c in range(cols):
    #         map[r][c] = "-"

    map = [["-"] * cols for i in range(rows)]
    map[0][0] = "P"
    return map


# Tạo object (cần nhập vị trí đứng)
def generate_object(map, rows, cols, obj_char):
    while True:
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        if map[r][c] == "-":
            map[r][c] = obj_char
            break


# Hàm in vị trí
def print_map(map, rows, cols):
    print()
    for r in range(rows):
        for c in range(cols):
            print(map[r][c], end=" ")
        print()


# 2. Viết hàm xác định hướng di chuyển dựa vào phím người dùng nhập.
# Hàm di chuyển + kiểm tra trường hợp không thể đi được
def move(map, rows, cols, ch, r_P, c_P):
    c_P_new = c_P
    r_P_new = r_P
    if ch == "W":
        r_P_new = max(0, r_P - 1)
    elif ch == "S":
        r_P_new = min(r_P + 1, rows - 1)
    elif ch == "A":
        c_P_new = max(0, c_P - 1)
    elif ch == "D":
        c_P_new = min(c_P + 1, cols - 1)

    #  di chuyen P
    value = map[r_P_new][c_P_new]
    map[r_P][c_P] = "-"
    map[r_P_new][c_P_new] = "P"

    # kiem tra thang thua
    result = checkPPosition(map, value)

    return r_P_new, c_P_new, result


# 3. Viết hàm thay đổi vị trí Player sau mỗi lần di chuyển.
# Kiểm tra Player có đi vào ô K hay D không.
def checkPPosition(map, value):
    if value == "K":
        global found_key
        found_key = True

    elif value == "D":
        os.system("cls")
        print(map, ROWS, COLS)

        if found_key:
            print("You win")
            return True
        else:
            print("You lose")
            return True


# == GENERATE MAP ==
ROWS = int(input("Row: "))
COLS = int(input("Col: "))
found_key = False
map = generate_map(ROWS, COLS)
generate_object(map, ROWS, COLS, "K")
generate_object(map, ROWS, COLS, "D")

# == INITIALIZE GAME STATE
r_P = 0
c_P = 0

# == PRINT STARTING SCREEN ==
os.system("cls")  # clear screen in Windows
print_map(map, ROWS, COLS)
print("\n== THE ESCAPE GAME ==")
print("Use W A S D to move (P)layer.")
print("Find (K)ey first then exit through the (D)oor.")

# == GAMEPLAY ==
# Tính thời gian tại thời điểm bắt đầu thuật toán
start_time = time.time()

while True:
    ch = msvcrt.getch().decode("utf-8").upper()
    r_P, c_P, result = move(c_P=c_P, ch=ch, cols=COLS, map=map, rows=ROWS, r_P=r_P)
    if result:
        break

    os.system("cls")
    print_map(map=map, cols=COLS, rows=ROWS)


# Tính thời gian tại thời điểm kết thúc thuật toán
end_time = time.time()

# tính thời gian chạy của thuật toán Python
print(f"Time for this round: {round((end_time-start_time)*10)/10}")
