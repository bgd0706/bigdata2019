def sum (a, b) :
    return print(a+b)

def sub (a, b) :
    return print(a-b)

def mul (a, b) :
    return print(a*b)

def div (a, b) :
    try :
        return print(a/b)
    except ValueError :
        pass
    except ZeroDivisionError:
        print("죄송합니다. 두 번째 입력에서 0을 입력하셨습니다. 분모는 0이 되어서는 안됩니다.")

while True :
        case = int(input("어떤 사칙연산을 하시겠습니까? (1: 덧셈, 2: 뺄셈, 3: 곱셈, 4: 나눗셈) "))
        number = input("두 수를 입력하세요 ('종료' 입력시 프로그램 종료) : ").split(' ')
        if number == '종료':
            exit()

        find = 0

        try:
            a = int(number[0])
        except ValueError:
            print("죄송합니다. 첫번째 입력을 %s 입력하셨습니다. 숫자를 입력하세요." % number[0])
            find +=1

        try:
            b = int(number[1])
        except ValueError :
            print("죄송합니다. 두번째 입력을 %s 입력하셨습니다. 숫자를 입력하세요." % number[1])
            find += 1
        if find == 0 :
            if (case == 1):
                sum(a, b)
            elif (case == 2):
                sub(a, b)
            elif (case == 3):
                mul(a, b)
            elif (case == 4) :
                div(a, b)
        if b == 0:
            div(number[0], b)
