import re 
# Write a Python program to find the occurrence and position of the substrings within a string.

while True :
    original_setence = input("입력하세요 : ")

    if original_setence == "ㅈㄹ" :
        exit()

    m = re.finditer("exercises", original_setence)

    for i in m :
        s = i.start()
        e = i.end()
        print(original_setence[s:e], s, e)