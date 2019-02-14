class Restaurant :
    def __init__ (self, name) :
        self.restaurant_name = name

    def open_restaurant(self) :
        print ("저희 [%s] 레스토랑 오픈했습니다. 어서오세요." %(self.restaurant_name))

class Korean_food(Restaurant) :
    cuisine_type = "한식"

    def describe_restaurant(self):
        print ("저희 레스토랑 명칭은 [%s] 이며, [%s] 전문점입니다. " %(self.restaurant_name, self.cuisine_type))

class Chinese_food(Restaurant) :
    cuisine_type = "중식"

    def describe_restaurant(self):
        print ("저희 레스토랑 명칭은 [%s] 이며, [%s] 전문점입니다. " %(self.restaurant_name, self.cuisine_type))

class Japanese_food(Restaurant) :
    cuisine_type = "일식"

    def describe_restaurant(self):
        print ("저희 레스토랑 명칭은 [%s] 이며, [%s] 전문점입니다. " %(self.restaurant_name, self.cuisine_type))

res_list = []

for i in range (0, 3) :
    menu = input("레스토랑 이름과 요리 종류를 선택하시오.(공백으로 구분) : ").split(" ")
    if (menu[1] != "한식" or menu[1] != "중식" or menu[1] != "일식") :
        print("다른 전문점은 없습니다. 다른 곳으로 찾아봐주세요")
        exit()

    res = Restaurant(menu[0])
    res.open_restaurant()

    res_list.append(i)
    if (menu[1] == "한식"):
        res_list[i] = Korean_food(menu[0])
    elif (menu[1] == "중식"):
        res_list[i] = Chinese_food(menu[0])
    elif (menu[1] == "일식"):
        res_list[i] = Japanese_food(menu[0])

    res_list[i].describe_restaurant()