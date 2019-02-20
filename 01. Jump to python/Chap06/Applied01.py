import shutil

f = open('learning_python.txt', 'r+')
lines = f.read().splitlines()

for line in lines :
    line = line.replace("python", "C")
    f.write(line+'\n')
f.close()

shutil.copy('learning_python.txt', 'learning_python_copied.txt')

f = open('learning_python_copied.txt', 'r')
lines = f.read().splitlines()
for line in lines :
    print(line)
f.close()