import re 
# Write a Python program to find the substrings within a string.

while True :
    original_setence = input("입력하세요 : ")

    if original_setence == "ㅈㄹ" :
        exit()

    m = re.findall("exercises", original_setence)

    for i in m :
        print(i)
