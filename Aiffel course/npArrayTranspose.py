import numpy as np

A = np.arange(24).reshape(2,3,4)

print("A:", A)

print("A의 전치행렬:", A.T)

print("A의 전치행렬의 shape:", A.T.shape)