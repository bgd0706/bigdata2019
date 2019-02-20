while True :
    case = input("프로그래밍이 왜 좋으세요?(종료 입력시 프로그램 종료) ")

    if case == "종료" :
        exit()

    name = input("이름을 입력해주세요: ")
    print("설문에 응답해 주셔서 감사합니다.")
    f = open("./poll.txt", 'a', encoding='UTF-8')
    f.write("[%s] %s" %(name, case)+'\n')
    f.close()