class Service :
    __secret__ = "영구는 배꼽이 두 개 다." # 클래스가 가지는 고유의 공통 속성
    name = "" 

    def __init__ (self, name) :
        self.name = name

    def sum (self, a, b) :
        result = a + b
        print("%s님 %s + %s = %s입니다." % (self.name, a, b, result))

    def get_secret(self):
        return self.__secret__

pey = Service("홍길동")
print(pey.get_secret())