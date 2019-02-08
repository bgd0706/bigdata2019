print("반복문 디버그")
task=0
for i in range(1, 101) :
    print ("반복문 실행")
    task += 1
    print ("%d번째 업무 실행" %task)
    # 반복문에서 변수값이 루프를 돌면서 잘못된 값으로 변경되는 것을 찾을시
    # Alt+F9으로 디버깅하면 루프단위로 디버깅이 가능하다 (커서가 있었던 곳들을 중점으로)
    print ("해당 업무 종료 \n")
    if task == 10 :
        task  -= 1

print("반복문 종료")