case = input("입력하시요. : ")

print (list(map(lambda n:len(set(n))==10 and len(n) ==10, case.split())))
