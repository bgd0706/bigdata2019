try :
    def sum (a, b) :
        return a+b

    while True :
        number = input("두 수를 입력하세요 ('종료' 입력시 프로그램 종료): ").split(' ')
        print(sum( int(number[0]), int(number[1]) ))
        if number[0].isdigit() :
            raise ValueError("%s번째 입력이 [%s]입니다. 숫자를 입력하세요." % (0, int(number[0])))
        if int(number[1]) != int() :
            raise ValueError("%s번째 입력이 [%s]입니다. 숫자를 입력하세요." % (1, int(number[1])))

        if number == '종료' :
            exit()
except ValueError  as  e:
    print(e)