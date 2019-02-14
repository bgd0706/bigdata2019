import os

f = os.popen("dir")
print(f.read())