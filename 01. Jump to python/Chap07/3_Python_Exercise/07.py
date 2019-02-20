import re
# Write a Python program to find sequences of lowercase letters joined with a underscore

# p = re.compile("[a-z][_]")
p = re.compile("[a-z]+[_][a-z]+$")

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