class Service :
    secret = "영구는 배꼽이 두 개 다." # 클래스가 가지는 고유의 공통 속성
    name = "" 

    def __init__ (self, name) :
        self.name = name

    def sum (self, a, b) :
        result = a + b
        print("%s님 %s + %s = %s입니다." % (self.name, a, b, result))

pey = Service("홍길동")
print(pey.secret) # 정말로 보호되어야 하는 변수라면 이렇게 제공하면 안됨

