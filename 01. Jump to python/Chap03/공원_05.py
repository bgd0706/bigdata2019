# coding: cp949

count = 0 # 결제한 사람 확인변수
free_ticket = 3 # 무료티켓 3장
dis_ticket = 5 # 할인티켓 5장

while True : # ctrl+c를 하기 전에는 무한루프

    age = int(input("나이를 입력하세요: ")) # "나이를 입력하세요: _____ <- 입력된 나이가 int형으로 
    price = 0 # 티켓가격 변수
    grade = "유아" # 티켓등급 변수 
    
    if age < 0 :
        print ("다시 입력하세요.")
        exit() # 음수를 입력할 때 강제종료
    elif 0 < age <= 3:
        grade = "유아"
    elif 3 < age <= 13:
        price = 2000
        grade = "어린이"
    elif 13 < age <= 18:
        price = 3000
        grade = "청소년"
    elif 18 < age <= 65:
        price = 5000
        grade = "성인"
    else :
        grade = "노인"
        
    print("귀하는 %s등급이며, 요금은 %d원 입니다." %(grade, price))

    choice = int(input("요금 유형을 선택하세요. (1: 현금, 1. CSV: 공원 전용 신용카드) : ")) # 요금 유형 선택 변후

    if choice == 1 : # '현금'을 선택한 경우
        if price == 0 : # '무료'인 사람
            print("감사합니다. 티켓을 발행합니다.")
        else : # '무료'가 아닌 사람
            input_price = int(input("요금을 입력하세요.")) # 소비자가 입금할 금액
            
            if input_price < price : # 소비자가 티켓금액보다 적게 입금한 경우
                print("%d가 모자랍니다. 입력하신 %d를 반환합니다." %(price-input_price, input_price))
            elif input_price == price : # 티켓금액만큼 입금한 경우
                print("감사합니다. 티켓을 발행합니다.")
            else : # 티켓금액보다 많게 입금한 경우
                print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환 합니다." %(input_price-price))
    else : # '공원 전용 신용카드'를 선택한 경우
        dis_price = price*0.9 # 티켓 금액의 10% 할인
        if age >= 60 and age <= 65 : # 60~65세 이상인 사람인 경우
            dis_price = dis_price*0.95 # 티켓 금액의 5% 추가 할인
        print("%d원 결제 되었습니다. 티켓을 발행합니다." %(dis_price))

    if (3 < age <= 65) : # 3세 이상 60세 이하인 경우
        count +=1 ; # 결제 했으므로 count 1 증가
        if (free_ticket != 0 or dis_ticket !=0) : # 무료와 할인 티켓이 없을 때 까지  
            if (count % 7 == 0) : # 7의 배수만큼 결제한 사람인 경우
                print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓 %d장" %(free_ticket-1))
                free_ticket -= 1
            if (count % 4 == 0) : # 4의 배수만큼 결제한 사람의 경우
                print("축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d장" %(dis_ticket-1))
                dis_ticket -= 1

    print("현재 %d명이 결제했습니다." %count)
