import re
# Write a Python program to find sequences of one upper case letter followed by lower case letters.

p = re.compile("^[A-Z]{1}[a-z]+")

while True :
    original_setence = input("입력하세요 : ")

    if original_setence == 0 :
        exit()

    m = p.search(original_setence)

    print(m)
    if m :
        print ('Found a match!\n')
    else :
        print ('Not matched\n')