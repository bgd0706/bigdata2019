import numpy as np
import pandas
import tensorflow as tf

# Load CSV file as matrix
train_csv_data=pandas.read_csv('train.csv').as_matrix()
test_csv_data=pandas.read_csv('test.csv').as_matrix()
test_csv_sub=pandas.read_csv('gender_submission.csv').as_matrix()

# MALE -> 1
# FEMALE -> 0
for i in range(len(train_csv_data)):
    if train_csv_data[i,4]=='male':
        train_csv_data[i,4]=1
    else:
        train_csv_data[i,4]=0
for i in range(len(test_csv_data)):
    if test_csv_data[i,3]=='male':
        test_csv_data[i,3]=1
    else:
        test_csv_data[i,3]=0

# train.csv
# survival: todwhsduqn
# pclass: Ticket class(1=1st, 2=2nd, 3=3rd)
# sex: 성별
# age: 나이
# sibsp: 타이타닉에 탑승한 형제/배우자 수
# parch: 타이타닉에 탑승한 부모/자녀 수
# ticket: Ticket number
# fare: 운임요금
# cabin: 승무원 번호
# embarked: 승선항
for i in range(len(train_csv_data)):
    if train_csv_data[i,11] == 'S':
        train_csv_data[i,11]=1
    elif train_csv_data[i,11] == 'C':
        train_csv_data[i,11]=2
    elif train_csv_data[i,11] == 'Q':
        train_csv_data[i,11]=3
    if np.isnan(train_csv_data[i,11]):
        train_csv_data[i,11]=0

for i in range(len(test_csv_data)):
    if test_csv_data[i,10] == 'S':
        test_csv_data[i,10]=1
    elif test_csv_data[i,10] == 'C':
        test_csv_data[i,10]=2
    elif test_csv_data[i,10] == 'Q':
        test_csv_data[i,10]=3
    if np.isnan(test_csv_data[i,10]):
        test_csv_data[i,10]=0

X_PassengerData=train_csv_data[:,[2,4,6,7,11]]
Y_Survived=train_csv_data[:,1:2]

Test_X_PassengerData=test_csv_data[:,[1,3,5,6,10]]
Test_Y_Survived=test_csv_sub[:,1:2]

X=tf.placeholder(tf.float32,shape=[None,5])

Y=tf.placeholder(tf.float32,shape=[None,1])

W=tf.Variable(tf.random_normal([5,1]),name='weight')

b=tf.Variable(tf.random_normal([1]),name='bias')

hypothesis = tf.sigmoid(tf.matmul(X,W)+b)

cost=-tf.reduce_mean(Y*tf.log(hypothesis)+(1-Y)*tf.log(1-hypothesis))
train=tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

predicted=tf.cast(hypothesis>0.5, dtype=tf.float32)
accuracy=tf.reduce_mean(tf.cast(tf.equal(predicted,Y),dtype=tf.float32))

previous_cost=0
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(10000):
        cost_val, _=sess.run([cost,train],feed_dict={X:X_PassengerData,Y:Y_Survived})
        if step%500==0:
            print("Step=", step,", Cost:",cost_val)

        if previous_cost==cost_val:
            print("found best hypothesis when step: ",step,"\n")
            break
        else:
            previous_cost=cost_val
    h,c,a=sess.run([hypothesis,predicted,accuracy], feed_dict={X:X_PassengerData,Y:Y_Survived})
    print("\n Accuracy: ",a)
    print("\n Test CSV runningResult")
    h2, c2, a2 = sess.run([hypothesis, predicted, accuracy], feed_dict={X: Test_X_PassengerData, Y: Test_Y_Survived})
    print("\n Accuracy: ",a2)