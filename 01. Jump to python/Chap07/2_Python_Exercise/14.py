import re 
# Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

p = re.compile("^[\w]*$") # 처음과 끝을 표시하기

while True :
    original_setence = input("입력하세요 : ")

    if original_setence == "ㅈㄹ" :
        exit()

    m = p.search(original_setence)

    print(m)
