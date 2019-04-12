import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split

# 데이터 읽어 들이기
mr = pd.read_csv("mushroom.csv", header=None)

# 고정변수 값을 넣어 줄 자리
X = tf.placeholder(tf.float32, [None, 22])
# 독립변수 값을 넣어 줄 자리
Y = tf.placeholder(tf.float32, [None, 2])

# 데이터 전처리
label = []
data = []

label_p = [0, 0]
label_e = [1, 1]

for row_index, row in mr.iterrows() :
    if row.loc[0] == 'p' :
        label.append(label_p)
    else :
        label.append(label_e)
    row_data = []
    for v in row.loc[1:]:
        row_data.append(ord(v))
    data.append(row_data)

# Variable : tensorFlow의 계산 그래프 안에 있는 값으로 머신 러닝에 활용되는 모델 매개변수로 변수의 초기값을 지정
W = tf.Variable(tf.zeros([22, 2])) # 22 X 2 행렬로 모두 0으로 초기화 (고정변수가 22가지, 종속변수는 2종류이기 때문에)
b = tf.Variable(tf.zeros([2])) # 2차원 벡터

# 행렬내적 곱 구하는 공식
logit_y = tf.matmul (X,W) + b

# softmax 함수는 벡터화된 입력 변수인 x를 가중치 행렬인 W와 곱하고, 여기에 편향 b를 더한 뒤, 각각의 클래스에 대한 소프트맥스
# 함수의 결과를 계산
softmax_y = tf.nn.softmax(logit_y)

# cross entropy는 최소화될 비용 함수로 실제 클래스와 모델의 예측 결과 간을 보여주는 것이다.
# reduce_sum은 모든 클래스에 대한 결과를 합하는 함수
# reduce_mean은 사용된 변수들 각각에서 계산된 합의 평균을 구하는 함수
cross_entropy = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(softmax_y), reduction_indices=[1]))
# 미분을 통해 각각의 변수에 대한 비용 함수의 기울기를 계산하여 0.1의 경사하강법 알고리즘을 사용하여 크로스 엔트로피를 최소화
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)

# 테스트 분리
data_train, data_test, label_train, label_test = train_test_split(data, label)

# 경사하강법으로 모델을 학습한다.
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
for i in range(1000) : # 길이로 할 수 있지만 시간이 많이 걸려 1000개로 학습
    sess.run(train_step, feed_dict={X: data_train, Y: label_train})

# 학습된 모델이 얼마나 정확한지를 계산하고 출력한다.
correct_prediction = tf.equal(tf.argmax(softmax_y,1), tf.argmax(Y,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print("정확도 : ", sess.run(accuracy, feed_dict={X: data_test, Y: label_test}))