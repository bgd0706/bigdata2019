import numpy as np
# 활성화 함수 종류
# 1. sigmoid : 결과 값이 2클래스로 분류할 경우
# 2. 소프트맥스 : 결과 값이 다중 클래스(3가지 이상)로 분류될 경우
# 3. 향등함수 : 회귀모형(값이 선형적으로 증가하는 경우)에 적용
def sigmoid(x) :
    return 1 / (1 + np.exp(-x))

def identify_function(x) :
    return x

def init_network() :
    network = {}
    network['W1'] = np.array([[0.1,0.3,0.5], [0.2,0.4,0.6]])
    network['b1'] = np.array([0.1,0.2,0.3])

    network['W2'] = np.array([[0.1,0.4], [0.2,0.5], [0.3,0.6]])
    network['b2'] = np.array([0.1,0.2])

    network['W3'] = np.array([[0.1,0.3], [0.2,0.4]])
    network['b3'] = np.array([0.1,0.2])

    return network

def forward(network, x) :
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x,W1)+b1
    z1 = sigmoid(a1)

    a2 = np.dot(z1, W2)+b2
    z2 = sigmoid(a2)

    a3 = np.dot(z2, W3) +b3
    y = identify_function(a3) # 향등 함수 : 내가 받은 값을 그대로 받는 함수

    return y

network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)

print(y)