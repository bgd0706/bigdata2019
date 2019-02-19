import re
# write a Python program that matches a string that has an a followed by zero or one 'b'

p = re.compile("ab?")

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