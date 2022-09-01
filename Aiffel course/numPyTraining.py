import numpy as np


# Input Dictionary object to np.array parameter
A = np.array({1:1,2:2,3:3})
print(A)

# Creating n-d matrices

B = np.array([[1,2],[3,4]])
print(B)

C = np.array([[1,2,3],[4,5,6]])
print(C)

ones_col = np.ones(3)

print(C+ones_col)