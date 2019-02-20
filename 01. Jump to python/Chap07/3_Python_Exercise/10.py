import re
# Write a Python program that matches a word at the beginning of a string.

p = re.compile("^[\w]+")

while True :
    original_setence = input("입력하세요 : ")

    if original_setence == 0 :
        exit()

    m = p.search(original_setence)

    print(m)
