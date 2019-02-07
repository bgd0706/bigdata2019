def Ari_Op (choice, *args) :
    result = args[0]
    if choice == 1 :
        for i in args :
            if (i==args[0]) :
                continue
            result += int(i)
    elif choice == 2 :
        for i in args :
            if (i==args[0]) :
                continue
            result *= int(i)
    elif choice == 3 :
        for i in args :
            if (i==args[0]) :
                continue
            result -= int(i)
    elif choice == 4 :
        for i in args :
            if (i==args[0]) :
                continue
            result /= int(i)
    return result

num = input("숫자를 입력하세요(1 : 덧셈, 2 : 곱셈, 3 : 뺄셈, 4 : 나눗셈) : ")
oper = input("피연산자를 입력하세요 : ").split()
answer = Ari_Op(num, oper)
print(answer)
