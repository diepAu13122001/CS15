import os

scr = "C:\\Users\\diepa\\OneDrive\\Documents\\Working\\MindX\\CS15\\a\\test.txt"

if os.path.exists(scr):
    print("File existed")
    if os.path.isfile(scr):
        print("This is a file")
    elif os.path.isdir(scr):
        print("This is a directory")
else:
    print("This location doesn't exist")

