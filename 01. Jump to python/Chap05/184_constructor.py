class Service :
    secret = "영구는 배꼽이 두 개 다."
    name = "" # 가독성을 위해 중복 코드 생성 -> self. 에 추가되었으면 바로 쌔리넣으

    def setname (self, name) :
        self.name = name

    def sum (self, a, b) :
        result = a + b
        print("%s님 %s + %s = %s입니다." % (self.name, a, b, result))

pey = Service()
pey.sum(1,1)
 # 이름이 설정되어 있지 않았기 때문에 sum함수 출력이 완벽하게 되지 않는다.