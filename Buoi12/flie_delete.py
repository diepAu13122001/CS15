import os
import shutil

scr = "C:\\Users\\diepa\\OneDrive\\Documents\\Working\\MindX\\CS15\\b\\b.txt"

# Xoa File
try: 
    os.remove(scr)
except FileNotFoundError:
    print('File not found!') 
else:
    print('File is deleted')

# Xoa folder
path_dir = 'C:\\Users\\diepa\\OneDrive\\Documents\\Working\\MindX\\CS15\\c'
try: 
    os.rmdir(path_dir)
except FileNotFoundError:
    print('Folder not found!')
except PermissionError:
    print("You do not have permission")
except OSError:
    print('You can not delete by this function')
    shutil.rmtree(path_dir) # delete folder with files 
    print('Deleted files and folder')
else:
    print('Folder is deleted')