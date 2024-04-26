import os
import msvcrt  # Windows
import random

# 1. Viết hàm khởi tạo bản đồ game.
# Tạo bản đồ rỗng
def generate_map(rows, cols):
  map = [['-']*cols for i in range(rows)]  # initialize empty map as a list of list
  map[0][0] = 'P'  # set player position at top left
  return map  # return map as a list of list

# Tạo object (cần nhập vị trí đứng)
def generate_object(map, rows, cols, obj_char):
  while True:  # randomize a position until found an empty one
    r_K = random.randint(0, rows-1)  # generate random row coordinate
    c_K = random.randint(0, cols-1)  # generate random column coordinate
    if map[r_K][c_K] == '-':    # if found empty position
      map[r_K][c_K] = obj_char  # set object there
      break                     # break out of loop
    
# Hàm in vị trí

# 2. Viết hàm xác định hướng di chuyển dựa vào phím người dùng nhập.
# Hàm di chuyển + kiểm tra trường hợp không thể đi được

# 3. Viết hàm thay đổi vị trí Player sau mỗi lần di chuyển. 
# Kiểm tra Player có đi vào ô K hay D không.

