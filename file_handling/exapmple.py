import os

file_name = "text.txt"

path = os.path.join('..','my_folder', 'nested_folder', file_name)

try:
    file = open(path)
    print('File found')
except FileNotFoundError:
    print('File is not found')