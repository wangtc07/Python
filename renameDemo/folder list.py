import os
import pathlib

path = '../rename'

cwd = os.getcwd()

print(cwd)

# get folder
files = os.listdir(path)

print(files)

for file in files:
    fullpath = os.path.join(path, file)
    print(fullpath)
    print(pathlib.Path(fullpath).stat())
    print('-')

fileDetail = os.walk(path)

print('--------------------------')

for root, dirs, files in fileDetail:
    print(root)
    print(dirs)
    print(files)