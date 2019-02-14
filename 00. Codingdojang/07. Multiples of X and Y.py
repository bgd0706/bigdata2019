case = input("공배수를 구할 두 수를 입력하시오. : ").split(" ")
scale = int(input("범위를 입력하시오. : "))
if (case[0] == '0' or case[1] == '0' or scale == '0') : exit()
sum = 0
for i in range(1, scale+1) :
    if(i % int(case[0]) == 0 and i % int(case[1]) == 0) :
        sum += i
        print(i, end=' ')
print("\n총합은 %s이다." %sum)