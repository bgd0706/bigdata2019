import re 
# Write a Python program where a string will start with a specific number.

# p = re.compile("^[0].*")
p = re.compile(r"^5")

while True :
    original_setence = input("입력하세요 : ")

    if original_setence == "ㅈㄹ" :
        exit()

    m = p.search(original_setence)

    print(m)
