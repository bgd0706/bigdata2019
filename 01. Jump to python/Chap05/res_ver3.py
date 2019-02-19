class Restaurant :
    def __init__ (self, name, type) :
        self.restaurant_name = name
        self.cuisine_type = type

    number_served = 0 # 손님 수를 세기 위해 0으로 초기화

    def describe_restaurant(self) :
        print ("저희 레스토랑 명칭은 [%s] 이고 [%s] 전문점입니다." %(self.restaurant_name, self.cuisine_type))

    def open_restaurant(self) :
        print ("저희 [%s] 레스토랑이 오픈했습니다." %(self.restaurant_name))

    def reset_number_served(self, number): # 손님 수를 0으로 초기화
        self.number_served = number
        print("손님 카운팅을 %s으로 초기화 하였습니다." %(number))

    def increment_number_served(self, number): # 손님 수 증가
        self.number_served += number
        print("손님 %s명 들어오셨습니다. 자리를 안내해 드리겠습니다." %(number)) # %(number_served)해도 무방

    def check_customer_number(self): # 손님 수 확인
        print("지금까지 총 %s명 손님께서 오셨습니다." %(self.number_served))

menu = input("레스토랑 이름과 요리 종류를 선택하시오.(공백으로 구분) : ").split(" ")
res = Restaurant(menu[0], menu[1])

res.describe_restaurant()

open = input("레스토랑을 오픈하시겠습니까? (y/n) ")

if open == 'y' :
    res.open_restaurant()
    while True :
        choice = input("어서오세요. 몇명이십니까? (초기화:0, 종료:-1, 누적고객 확인:p)") # choice는 str형

        if choice == 'p' : # choice == 'p'
            res.check_customer_number()
        else : # choice != 'p'
            choice = int(choice) # int형으로 변환
            if choice == 0 : # 0 이면
                res.reset_number_served(choice) # reset_number_served 함수를 choice(0)으로 매개변수로 받아 호출한다. (0으로 reset!)
            elif choice == -1 : # -1 이면
                print("%s 레스토랑 문닫습니다." %(res.restaurant_name)) # 문닫는다.
                exit()
            else : # 다른 경우에는
                res.increment_number_served(choice) # 그 숫자(choice) 만큼 count를 한다.
