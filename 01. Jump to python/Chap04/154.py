a = 1 # 전역변수(Global variable)
# 전역변수는 힙(Heap)에 저장되며  프로그램이 끝날때 까지 유효
# 어디에서도 접근 가능하다.
def vartest(a) :
    a += 1 # 지역변수(Local variable)
    # 지역변수는 스택(Stack)에 저장되며, 함수호출이 끝나면 사라진다.
    # 해당 함수에서만 접근 가능하다.

vartest(a)

print(a)