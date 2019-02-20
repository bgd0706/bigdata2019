class Restaurant :
    def __init__ (self, name, type) : # name은 레스토랑 이름, type은 레스토랑 종류
        self.restaurant_name = name
        self.cuisine_type = type

    def describe_restaurant(self) :
        print ("저희 레스토랑 명칭은 [%s] 이고 [%s] 전문점입니다." %(self.restaurant_name, self.cuisine_type))

    def open_restaurant(self) :
        print ("저희 [%s] 레스토랑 오픈했습니다. 어서오세요." %(self.restaurant_name))

menu = input("레스토랑 이름과 요리 종류를 선택하시오.(공백으로 구분) : ").split(" ")
res = Restaurant(menu[0], menu[1])

res.describe_restaurant()
res.open_restaurant()