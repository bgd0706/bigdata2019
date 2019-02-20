def sum (a,b) :
    return print(a+b)

while True :
    number = input("두 수를 입력하세요 ('종료' 입력시 프로그램 종료) : ").split(' ')
    if number == '종료' :
        exit()
    find =0
    try :
        a = int(number[0])
    except ValueError :
        print("죄송합니다. 첫번째 입력을 %s 입력하셨습니다. 숫자를 입력하세요." %number[0])
        find +=1
    try :
        b = int(number[1])
    except ValueError :
        print("죄송합니다. 두번째 입력을 %s 입력하셨습니다. 숫자를 입력하세요." %number[1])
        find +=1
    if find == 0 : sum(a,b)