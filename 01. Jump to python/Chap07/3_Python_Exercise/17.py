import re 
# Write a Python program to check for a number at the end of a string.

p = re.compile(r".*[0-9]$")

while True :
    original_setence = input("입력하세요 : ")

    if original_setence == "ㅈㄹ" :
        exit()

    m = p.search(original_setence)

    print(m)
