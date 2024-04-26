import os
import msvcrt  # Windows
import random
import time

# 1. Viết hàm khởi tạo bản đồ game.
# Tạo bản đồ rỗng
def generate_map(rows, cols):
    map = [["-"] * cols for i in range(rows)]  # initialize empty map as a list of list
    map[0][0] = "P"  # set player position at top left
    return map  # return map as a list of list


# Tạo object (cần nhập vị trí đứng)
def generate_object(map, rows, cols, obj_char):
    while True:  # randomize a position until found an empty one
        r_K = random.randint(0, rows - 1)  # generate random row coordinate
        c_K = random.randint(0, cols - 1)  # generate random column coordinate
        if map[r_K][c_K] == "-":  # if found empty position
            map[r_K][c_K] = obj_char  # set object there
            break  # break out of loop


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
    r_P_new = r_P
    c_P_new = c_P
    if ch == "W":
        r_P_new = max(0, r_P - 1)
    elif ch == "S":
        r_P_new = min(rows - 1, r_P + 1)
    elif ch == "A":
        c_P_new = max(0, c_P - 1)
    elif ch == "D":
        c_P_new = min(cols - 1, c_P + 1)

    # change the content of map
    value = map[r_P_new][c_P_new]
    map[r_P][c_P] = "-"
    map[r_P_new][c_P_new] = "P"

    # change P position
    result = checkPPosition(map, value)

    # return new position and the value in new position
    return r_P_new, c_P_new, result


# 3. Viết hàm thay đổi vị trí Player sau mỗi lần di chuyển.
# Kiểm tra Player có đi vào ô K hay D không.
def checkPPosition(map, value):
    if value == "K":  # if found Key => update game state
        # found_key = True
        print("you found the key!")
        global found_key
        found_key = True

    elif value == "D":
        os.system("cls")
        print_map(map, ROWS, COLS)

        if found_key:  # if Key has been found => user win
            print("YOU WON!!!")
            return True
        else:  # if Key has not been found => user lose
            print("YOU LOSE.")
            print("Maybe find the Key first?")
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
#Tính thời gian tại thời điểm bắt đầu thuật toán
start_time = time.time()
while True:
    ch = msvcrt.getch().decode("utf-8").upper()  # Windows
    r_P, c_P, value = move(map, ROWS, COLS, ch, r_P, c_P)
    if value:
        break

    # print the updated map after every move
    os.system("cls")
    print_map(map, ROWS, COLS)

#Tính thời gian tại thời điểm kết thúc thuật toán
end_time = time.time()

#tính thời gian chạy của thuật toán Python
elapsed_time = round((end_time - start_time)*10)/10
print (f"Time for this round: {elapsed_time} [sec]")
