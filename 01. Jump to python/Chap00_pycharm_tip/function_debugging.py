print("실행초기화")

def simple_func1() :
    print("simple_func1 초기화") # 디버깅하지 않고 빠져나올려면 Shift+F8
    print("simple_func1 로직 수행중")
    # .....
    print("simple_func1 실행완료")

print("함수 호출 준비")
simple_func1() # 함수 안으로 디버깅 하려면 F7
print("프로그램 종료")