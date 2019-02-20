class Restaurant :
    def __init__ (self, name, type, total) :
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = total # 가게 총 누적고객수 (3번과는 다름)
        self.f = open("고객서빙현황로그.txt", 'r+')

    todays_customer = 0 # 오늘 총 누적고객수
    reset_accum = 0 # reset_number_served에서 0을 초기화하기 위한 변수

    def describe_restaurant(self) :
        print ("저희 레스토랑 명칭은 [%s] 이고 [%s] 전문점입니다." %(self.restaurant_name, self.cuisine_type))

    def open_restaurant(self) :
        print ("저희 [%s] 레스토랑이 오픈했습니다." %(self.restaurant_name))

    def reset_number_served(self, number):
        self.reset_accum = number
        print("손님 카운팅을 %s으로 초기화 하였습니다." % (number))

    def increment_number_served(self, number):
        self.reset_accum += number
        self.todays_customer += number
        print("손님 %s명 들어오셨습니다. 자리를 안내해 드리겠습니다." %(number))

    def check_customer_number(self):
        print("지금까지 총 %s명 손님께서 오셨습니다." %(self.reset_accum))

    def __del__(self):
        self.f.write(str(int(self.todays_customer)+int(self.number_served))) # 누적된 손님 = 어제까지 누적된 손님 + 오늘 누적된 손님
        self.f.close()

menu = input("레스토랑 이름과 요리 종류를 선택하시오.(공백으로 구분) : ").split(" ")

with open('고객서빙현황로그.txt') as f:
    line = [lines.rstrip() for lines in f]
for i in line:
    total = int(i) #int형으로 해주어야 함
res = Restaurant(menu[0], menu[1], total) # 프로그램이 항상 실행될 때 마다 누적된 값을 저장해야 하기 위해

res.describe_restaurant()

opening = input("레스토랑을 오픈하시겠습니까? (y/n) ")

if opening == 'y' :
    res.open_restaurant()

    while True :
        choice = input("어서오세요. 몇명이십니까? (초기화:0, 종료:-1, 누적고객 확인:p)")

        if choice == 'p' :
            res.check_customer_number()
        else:
            choice = int(choice)
            if choice == 0:
                res.reset_number_served(choice)
            elif choice == -1:
                print("%s 레스토랑 문닫습니다." % (res.restaurant_name))
                exit()
            else:
                res.increment_number_served(choice)