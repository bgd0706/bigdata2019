# coding: cp949

age = int(input("나이를 입력하세요: "))
price = 0
grade = ""

if age < 0 :
    print ("다시 입력하세요.")
    exit()

if 0 < age <= 3:
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

