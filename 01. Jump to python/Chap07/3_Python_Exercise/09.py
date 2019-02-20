import re
# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

# p = re.compile("^a.b$")
p = re.compile("^a.+b$") # 점에도 +나 *를

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