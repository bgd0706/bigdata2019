# 목적 : 활성화 함수 - 시그모이드 함수 (Sigmold Function)
# coding : utf-8
import numpy as np
import matplotlib.pylab as plt

def sigmoid (x) :
    return 1 / (1 + np.exp(-x))

def step_function (x) :
    return np.array(x > 0, dtype=np.int)

X = np.arange(-5.0, 5.0, 0.1)
y1 = sigmoid(X)
y2 = step_function(X)
plt.plot(X, y1)
plt.plot(X, y2, 'k--')
plt.ylim(-0.1, 1.1) # y축의 범위 지정
plt.show()