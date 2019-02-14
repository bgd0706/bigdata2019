num=input('배수를 구하고 싶은 두 수를 입력해라. ').split(" ")

sum = 0
for i in range (1, 1000) :
    if (i % int(num[0]) == 0 or i % int(num[1]) == 0) :
        sum += i
print(sum)