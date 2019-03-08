import os

def read_content() :
   try : # poll.txt 파일을 읽어서 내용을  출력
       f = open("./poll.txt", 'r', encoding='UTF-8')
       lines = f.read().splitlines()
       for line in lines:
           print(line)
       f.close()

   except FileNotFoundError : # poll.txt 파일이 없는 경우
       print("기존 poll.txt 파일을 찾을 수 없습니다. 아래 중 선택하세요.")
       choice = int(input("1. 종료 1. CSV. 새로운 파일 생성 3. 변경된 파일 경로 입력 : "))
       if choice == 1 : # 그냥 안하겠다
           exit()
       elif choice == 2 : # 현재 경로에 새로운 파일 생성
           f = open("./poll.txt", 'w', encoding='UTF-8')
           f.write("<현재 누적 응답 현황>\n")
           f.close()
       elif choice == 3 :
           address = input("변경된 파일 경로를 입력하세요. : ") # 현재 경로가 아닌 다른 경로에 새로운 파일 생성
           os.chdir("%s" % address)
           f = open('./poll.txt', 'r', encoding='UTF-8')
           lines = f.read().splitlines()
           for line in lines:
               print(line)
           f.close()

while True :
    read_content()
    case = input("프로그래밍이 왜 좋으세요?(종료 입력시 프로그램 종료) ")

    if case == "종료" :
        exit()

    name = input("이름을 입력해주세요: ")
    print("설문에 응답해 주셔서 감사합니다.")

    f = open("./poll.txt", 'a', encoding='UTF-8')
    f.write("[%s] %s" %(name, case)+'\n')
    f.close()