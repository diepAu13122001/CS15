# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil

scr = "C:\\Users\\diepa\\OneDrive\\Documents\\Working\\MindX\\CS15\\a\\test.txt"
dst = "C:\\Users\\diepa\\OneDrive\\Documents\\Working\\MindX\\CS15\\a\\"

shutil.copyfile(scr, dst + 'test_copyfile.txt')
shutil.copy(scr, dst + 'test_copy.txt')
shutil.copy2(scr, dst + 'test_copy2.txt')