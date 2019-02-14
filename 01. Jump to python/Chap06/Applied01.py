import os
from os import rename

f = open('learning_python.txt', 'r+')
lines = f.read().splitlines()
for line in lines :
    line = line.replace("python", "C")
    # with open('learning_python.txt', 'a') as f :
    f.write(line+'\n')
for line in lines :
    print(line)

os.rename('learning_python.txt', 'learning_python_copyed.txt')

