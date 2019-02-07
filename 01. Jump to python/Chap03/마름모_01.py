#coding: cp949

while True :
    num = int(input("홀수를 입력하세요(0 <- 종료): "))

    if (num == 0) : break
    
    row = int(num / 2) + 1
    col = num
    start = row-1
    finish = row-1

    if (start >=0 and finish <=col) :
        for j in range(0, row) :
            for i in range(0, col+1) :
                # print(start, finish)
                if start <= i <= finish :
                    print ('*', end='')
                else :
                    print ('', end=' ')
            
            start -= 1
            finish += 1

            print(" ")

    
            
