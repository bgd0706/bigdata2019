# coding: cp949

age = int(input("나이를 입력하세요: "))
price = 0
grade = ""

if age < 0 :
    print ("다시 입력하세요.")
    exit()
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

if price == 0 :
    print("감사합니다. 티켓을 발행합니다.")
    exit()

input_price = int(input("요금을 입력하세요."))

if input_price < price :
    print("%d가 모자랍니다. 입력하신 %d를 반환합니다." %(price-input_price, input_price))
elif input_price == price :
    print("감사합니다. 티켓을 발행합니다.")
else :
    print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환 합니다." %(input_price-price))



