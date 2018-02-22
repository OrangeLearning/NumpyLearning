import numpy as np

print('ndarray数组与标量/数组的运算')
x = np.array([1,2,3])
print(x*2) # [2 4 6]
print(x>2) # [False False  True]
y = np.array([3,4,5])
print(x+y) # [4 6 8]
print(x>y) # [False False False]