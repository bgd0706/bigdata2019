import tensorflow as tf

# 학습데이터 (X,Y)
x_train = [1,2,3,4]
y_train = [6,5,7,10]

# 변수선언
# tf.random_normal : 0~1 사이의 정규확률 분포 값을 생성
W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

# 가설식 정의 H(x) = Wx+b
hypothesis = x_train * W + b

# cost / loss function
# reduce_mean : 모든 차원을 제거되고 평균을 구함, enumerative 타입의 모든 요소의 평균값
# loss function : 손실함수 => 각 데이터에 대한 예측값과 실제 관측값의 차이를 산술적으로 계산
cost = tf.reduce_mean(tf.square(hypothesis - y_train))

# Minimize, 최적화 함수
# GradientDescentOptimizer : 경사하강법 적용
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

# Launch the graph in a session
sess = tf.Session()

# Initializes global variables in the graph
sess.run(tf.global_variables_initializer())

# 최적값 찾기
for step in range(2000) :
    sess.run(train)
    print(step, sess.run(cost), sess.run(W), sess.run(b))