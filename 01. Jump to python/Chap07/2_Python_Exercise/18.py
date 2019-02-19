import re 
# Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string.

p = re.compile(r"([0-9]{1,3})")

while True :
    original_setence = input("입력하세요 : ")

    if original_setence == "ㅈㄹ" :
        exit()

    m = p.finditer(original_setence)

    for i in m :
        print(i.group(0))
