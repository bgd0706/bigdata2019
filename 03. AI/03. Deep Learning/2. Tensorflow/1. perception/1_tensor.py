import tensorflow as tf

# . 반드시 (()) 로 인자를 사용해야 한다.
ta = tf.zeros((2,2))

# print(ta.eval()) # 에러 발생

session = tf.InteractiveSession()
print(ta.eval())
session.close()