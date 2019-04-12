# 목적 : 활성화 함수 - 계단 함수 (Step Function)
# coding : utf-8
import numpy as np
import matplotlib.pylab as plt

def step_function (x) :
    # x>0 True 이면 1 , False이면 0
    return np.array(x > 0 , dtype=np.int)

# -5.0 ~ 5.0 까지 0.1 delta
X = np.arange(-5.0, 5.0, 0.1)
Y = step_function(X)
plt.plot(X, Y)
plt.ylim(-0.1, 1.1) # y축의 범위 지정
plt.show()