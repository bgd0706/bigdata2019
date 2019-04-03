# 목적 : 퍼셉트론 가중치와 편향 도입
# coding : utf-8
import numpy as np

def AND (x1, x2) :
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7 # 편향 (뉴런이 얼마나 쉽게 활성화하느냐를 조정하는 매개변수)
    tmp = np.sum(w*x) + b
    if tmp <= 0 :
        return 0
    else :
        return 1

if __name__ == '__main__' :
    for xs in [(0,0), (1,0), (0,1), (1,1)] :
        y = AND(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))

# 가중치는 각 입력 신호가 결과에 주는 영향력(중요도)를 조절하는 매개변수
# 편향은 뉴런이 얼마나 쉽게 활성화 (결과로 1을 출력) 하느냐를 조정하는 매개변수