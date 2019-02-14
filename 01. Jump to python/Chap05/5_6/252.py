import os

print(os.getcwd())
# os.system("dir")
# os.system("notepad")
# os.system("notepad test.txt")  # 현재 경로에 test.txt가 없어서 해당파일을 열수 없다.
os.chdir("d:/temp")
os.system("notepad test.txt")