class Calculator : # 사용자 정의 클래스
    def __init__(self): # 생성자(Constructor) : 객체 생성시 최초로 수행되는 함수 self로 인해 일반 함수와 비교
        self.result = 0 # Class의 멤버 변수

    def adder(self, num): # 멤버 함수(Member Function)
        print("[%d]값을 입력 받았습니다." %num)
        self.result += num+100
        self.num1 = 100 # 멤버변수로 등록은 가능하나 가독성은 떨어진다.
        return self.result

cal1 = Calculator()
cal2 = Calculator()
cal3 = Calculator()

print(cal1.adder(3))
print(cal1.adder(4))
print(cal2.adder(3))
print(cal2.adder(7))
print(cal3.adder(2))
print(cal3.adder(6))
