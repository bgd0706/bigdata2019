import numpy as np

A = np.array([[1,2],[3,4]])
print(A.shape)

B = np.array([[5,6], [7,8]])
print(B.shape)

# np.dot : 행렬의 내적
print(np.dot(A,B))