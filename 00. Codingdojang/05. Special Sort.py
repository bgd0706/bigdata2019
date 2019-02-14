num = input("숫자들을 입력하시오. : ").split(" ")
answer = []
for i in range(len(num)) :
    if (int(num[i]) < 0 ) :
        answer.append(int(num[i]))
for i in range(len(num)):
    if (int(num[i]) > 0) :
        answer.append(int(num[i]))
print(answer)