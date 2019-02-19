import re
# Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)

p = re.compile("[a-zA-Z0-9]*")

original_setence = input("입력하세요 : ")
m = p.search(original_setence)

print(m)