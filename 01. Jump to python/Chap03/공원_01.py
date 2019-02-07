# coding: cp949

age = int(input("나이를 입력하세요: "))
price = 0

if 3 < age <= 13:
    price = 2000
elif 13 < age <= 18:
    price = 3000
elif 18 < age <= 65:
    price = 5000

print("요금은 %d원 입니다." % price)
