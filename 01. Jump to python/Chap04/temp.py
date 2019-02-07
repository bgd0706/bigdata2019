def Ari_Ope (choice) :
    result = int(num[0])

    for i in num :
        if (i!=num[0]) :
            if (choice == 1) :
                result += int(i)
            elif (choice == 2) :
                result -= int(i)
            elif (choice == 3) :
                result *= int(i)
            elif (choice == 4) :
                result /= int(i)
        break

    return result # for문 연고나 다시 생각

choice = input("사용한 사칙연산을 번호로 적으시오(1: 덧셈, 2: 뺄셈, 3: 곱셈, 4: 나눗셈) : ")
num = input("숫자를 입력하세요 : ").split()
print(Ari_Ope(choice))
