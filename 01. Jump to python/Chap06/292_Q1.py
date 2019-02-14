case = input("입력 : ")
case = list(case)
i = 0
while i < len(case) :
    j = i+1
    while True :
        if (j<len(case) and case[i] == case[j]) :
            j+=1
        else :
            break
    print(case[i] + str(j-i), end='')
    i += j-i