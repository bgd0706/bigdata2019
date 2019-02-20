import re 
# Write a Python program to replace whitespaces with an underscore and vice versa.

p = re.compile('\s')
r = re.compile('_')

while True :
    original_setence = input("입력하세요 : ")

    if original_setence == "ㅈㄹ" :
        exit()

    m = p.sub("_", original_setence)
    n = r.sub(" ", original_setence)
    print(m)
    print(n)

# import re
# text = 'Python Exercises'
# text =text.replace (" ", "_")
# print(text)
# text =text.replace ("_", " ")
# print(text)