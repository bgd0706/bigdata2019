import re
# write a Python program that matches a string that has an a followed by zero or more b's.

p = re.compile("ab*")

original_setence = input("입력하세요 : ")
m = p.search(original_setence)

print(m)

if m :
    print ('Found a match!')
else :
    print ('Not matched')