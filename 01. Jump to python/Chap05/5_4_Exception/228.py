print("progress 1")
f = open("새파일.txt","r")
print("progress 2")
f.close()
print("progress 3")
f = open("나없는파일.txt", "r") # 파일이 없기 때문에 오류가 발생한다. 이 이후는 실행되지 않는다.
print("progress 4")
f.close()
print("progress 5")