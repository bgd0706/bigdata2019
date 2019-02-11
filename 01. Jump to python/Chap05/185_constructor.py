class Service :
    secret = "영구는 배꼽이 두 개 다." # 클래스가 가지는 고유의 공통 속성
    name = ""

    def __init__ (self, name) :
        self.name = name

    def sum (self, a, b) :
        result = a + b
        print("%s님 %s + %s = %s입니다." % (self.name, a, b, result))

pey = Service("홍길동")
 # 객체만이 가지는 고유의 초기값을 설정하고 싶을 때 생성자를 활용한다.
pey.sum(1,1)
