import tensorflow as tf
import matplotlib.pyplot as plt

X = [1,2,3]
Y = [1,2,3]

W =  tf.placeholder(tf.float32)

hypothesis = X * W

# 경사 하강법 공식
# reduce_mean : 특정 차원을 제거한 모든 요소에 대한 평균값
cost = tf.reduce_mean(tf.square(hypothesis - Y))

with tf.Session() as sess :
    W_val = []
    cost_val = []

    for i in range(-30, 50) :
        # feed_W : 학습률 => 너무 크거나 최적의 cost를 찾기 어렵고, 너무 작으면 성능상의 문제가 발생한다.
        feed_W = i * 0.1

        curr_cost, curr_W = sess.run([cost, W], feed_dict={W: feed_W})
        W_val.append(curr_W)
        cost_val.append(curr_cost)

    plt.plot(W_val, cost_val)
    plt.show()
