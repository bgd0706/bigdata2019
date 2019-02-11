class HousePark :
    __last_name__ = "박"
    full_name = ""

    def __init__(self,name):
        self.full_name = self.__last_name__ + name
    def travel(self,where):
        print("%s, %s 여행을 가다" %(self.full_name, where))

pey = HousePark("응용")
pey.travel("부산")
