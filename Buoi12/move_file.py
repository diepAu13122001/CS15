import os
# move file ----------------------------------------------------------
scr = "C:\\Users\\diepa\\OneDrive\\Documents\\Working\\MindX\\CS15\\a\\test.txt"
dst = "C:\\Users\\diepa\\OneDrive\\Documents\\Working\\MindX\\CS15\\b\\b.txt"
try:
    if os.path.exists(dst):
        print("There is already a file there")
    else:
        os.replace(scr, dst)
        print(scr, "was moved")
except FileNotFoundError:
    print(scr, "was not found")

# move folder ----------------------------------------------------------
scr_dir = "C:\\Users\\diepa\\OneDrive\\Documents\\Working\\MindX\\CS15\\a"
dst_dir = "C:\\Users\\diepa\\OneDrive\\Documents\\Working\\MindX\\CS15\\c"
try:
    if os.path.exists(dst_dir):
        print("There is already a folder there")
    else:
        os.replace(scr_dir, dst_dir)
        print(scr_dir, "was moved")
except FileNotFoundError:
    print(scr_dir, "was not found")
