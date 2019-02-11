class HousePark : # 부모클래스 (Super Class)
    __last_name__ = "박"
    full_name = ""

    def __init__(self,name):
        self.full_name = self.__last_name__ + name
    def travel(self,where):
        print("%s, %s 여행을 가다" %(self.full_name, where))

class HouseKim(HousePark) : # 자식클래스 (Child Class)
    pass

kitty = HouseKim("만복")
print(kitty.__last_name__)
kitty.travel("제주")