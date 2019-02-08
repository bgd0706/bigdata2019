def fib(n) :
    if n == 0 :
        return 0
    if n == 1 :
        return 1
    return fib(n-1)+fib(n-2)

num = int(input("숫자를 입력하세요 : "))

for i in range(0, num+1) :
    if i == num :
        print(str(fib(i)), end='')
    else :
        print(str(fib(i))+', ', end='')
