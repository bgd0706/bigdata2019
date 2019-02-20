import re 
# Write a Python program that matches a word containing 'z', not start or end of the word.

# p = re.compile("^[^z]\w*z.\w*[^z]$")
p = re.compile("\Bz\B")

while True :
    original_setence = input("입력하세요 : ")

    if original_setence == 0 :
        exit()

    m = p.search(original_setence)

    print(m)
