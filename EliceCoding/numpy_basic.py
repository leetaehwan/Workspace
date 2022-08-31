import numpy as np

arr = np.array(range(6), dtype = 'int')

print(arr.ndim)
print(arr.shape)

arr1 = arr.copy()

arr1.shape = 3,2

print(arr1.shape)
print(arr.shape)
print(arr1.size)
print(arr1.dtype)

x = np.arange(7)

print(x)