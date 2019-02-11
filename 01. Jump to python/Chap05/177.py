class Service :
    secret = "영구는 배꼽이 두 개 다."
    name = "" # 가독성을 위해 중복 코드 생성 -> self. 에 추가되었으면 바로 쌔리넣으

    def setname (self, name) :
        self.name = name

    def sum (self, a, b) :
        result = a + b
        print("%s님 %s + %s = %s입니다." % (self.name, a, b, result))

pey = Service()
pey.setname("홍길동")



# print(pey.secret)
# pey.sum(pey,1,1)
pey.sum(1,1) # pey.sum을 통하여 pey가 호출한지 알기 때문에 pey는 생략 가능
# pey.sum("1", "1") # %s는 모든 데이터 타입이 허용이기 때문에 문자열 +로 변환
