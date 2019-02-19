import re
# Write a Python program that matches a word at end of string, with optional punctuation.

# p = re.compile("[\w]+$")
p = re.compile("[\w]+[.]*$") # [.] 대신에 \S 사용해도 됨

while True :
    original_setence = input("입력하세요 : ")

    if original_setence == 0 :
        exit()

    m = p.search(original_setence)

    print(m)
