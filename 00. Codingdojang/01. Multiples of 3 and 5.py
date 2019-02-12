print ("1000미만의 자연수에서 3,5의 배수의 총합을 구하라.")

sum = 0
for i in range (1, 1000) :
    if (i % 3 == 0 or i % 5 == 0) :
        sum += i
print(sum)