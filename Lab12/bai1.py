file_path = 'C:\\Users\\diepa\\OneDrive\\Documents\\Working\\MindX\\CS15\\Lab12\\test\\a.txt'

with open(file_path, 'r') as file: 
    list_name = [('- ' +item.replace('\n', '')) for item in file.readlines()]
    print('List of name:')
    for i in list_name:
        print(i)
