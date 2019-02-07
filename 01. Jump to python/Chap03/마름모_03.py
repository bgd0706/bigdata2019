#coding: cp949

while True :
    num = int(input("홀수를 입력하세요(0 <- 종료): ")) # 밑변의 길이

    if (num == 0) : break # 0일 때 종료
     
    row = int(num / 2) + 1 # 높이 -> 행의 개수
    col = num # 밑변의 길이 -> 열의 개수
    start = row-1 # 별을 만들 시작 위치
    finish = row-1 # 별을 만들 끝 위치

    print(' ', end='') 
    print('-'*(col), end='') # 윗 테두리 
    print(" ")

    if (start >=0 and finish <=col) : # 위에서 밑변까지 
        for j in range(0, row) : # 0부터 행의 개수까지 
            print ('|', end='') # 왼쪽 테두리

            for i in range(0, col) : # 0부터 열의 개수까지
                if start <= i <= finish : # i가 별을 만들 시작과 끝 위치 사이 있는 동안
                    print ('*', end='') # 별을 그린다.
                else : # 사이에 없을 동안
                    print ('', end=' ') # 공백을 넣는다.
            print ('|', end='') # 오른쪽 테두리
            start -= 1 # 이전 start의 값을 기준으로 -1
            finish += 1 # 이전 finish의 값을 기준으로 +1

            print(" ") # 별을 다음 행에 그릴 준비 


    if (start <= row-1 and finish >= row-1) : # 밑변에서 아래까지
        start += 2 # +1이 아닌 +2를 한 이유는 밑변이 중복으로 찍히기 때문이다.
        finish -= 2
        for j in range(0, row-1) :
            print('|', end='')

            for i in range(0, col) :
                if start <= i <= finish :
                    print ('*', end='')
                else :
                    print ('', end=' ')
            print ('|', end='')            
            start += 1
            finish -= 1

            print(" ")
   
    print(' ', end='')
    print('-'*(col), end='') # 아랫쪽 테두리
    print(" ")
