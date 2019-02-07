# 입력(parameter)이 있고, 출력(return)이 없는 함수
# def my_sum(num1, num2) :
def my_sum() :
    #  함수 정의(define)
    num1 = num1+1000 # 여기서 num1과 10번 라인의 num1은 다르다.
    num2 = num2+1000 # 여기서 num2과 10번 라인의 num2은 다르다.
    print("num1+num2="+str(num1+num2))

num1, num2 = input("두 수를 입력하세요: ").split()
num1 = int(num1)
num2 = int(num2)
my_sum()