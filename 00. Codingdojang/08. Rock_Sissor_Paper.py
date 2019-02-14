import random
rsp = input("가위바위보 게임을 시작합니다. \n가위, 바위, 보 중 하나를 고르세요. ")

com = random.randrange(1, 3) # 1은 가위, 2는 바위, 3은 보

if (rsp=='가위' and com == 3 ) or (rsp=='바위' and com ==1) or (rsp== '보' and com ==2) :
    print("너님이 승리하셨습니다.")
elif (rsp=='가위' and com==1) or (rsp=='바위' and com==2) or (rsp=='보' and com==3) :
    print("비겼습니다.")
else :
    print("너님이 졋어요.")