# coding : utf-8
import sys, os
sys.path.append(os.pardir) # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
import pickle
from keras.datasets import mnist

def sigmoid (x) :
    return 1 / (1 + np.exp(-x))

def softmax (a) :
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

def get_data () :
    (x_train, t_train), (x_test, t_test) = mnist.load_data()
    x_train = x_train.reshape(60000, 784).astype('float32')
    x_test = x_test.reshape(10000, 784).astype('float')
    x_train /= 255 # 정규화 0~255 범위인 값을 0.0 ~ 1.0 범위로 변환
    # Shape만 강조하기 위하여 빅데이터 분석을 위하여 데이터 형식을 변환하는 것을 전처리(Pre-processing)이라고 한다.
    x_test /= 255
    return x_test, t_test

def init_network() :
    with open("sample_weight.pkl", 'rb') as f :
        network = pickle.load(f)
    return network

def predict (network, x) :
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y

x, t = get_data()
network = init_network()
accuracy_cnt = 0
for i in range(len(x)) :
    y = predict(network, x[i])
    p = np.argmax(y) # 확률이 가장 높은 원소의 인덱스를 얻는다.
    if p == t[i] :
        accuracy_cnt += 1

print("Accuracy:" + str(float(accuracy_cnt) / len(x)))

