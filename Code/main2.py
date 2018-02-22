import numpy as np

print('生成指定元素类型的数组:设置dtype属性')
x = np.array([1,2.6,3],dtype = np.int64)
print(x) # 元素类型为int64
print(x.dtype)
x = np.array([1,2,3],dtype = np.float64)
print(x) # 元素类型为float64
print(x.dtype)

print('使用astype复制数组，并转换类型')
x = np.array([1,2.6,3],dtype = np.float64)
y = x.astype(np.int32)
print(y) # [1 2 3]
print(x) # [ 1.   2.6  3. ]
z = y.astype(np.float64)
print(z) # [ 1.  2.  3.]

print('将字符串元素转换为数值元素')
x = np.array(['1','2','3'],dtype = np.string_)
y = x.astype(np.int32)
print(x) # ['1' '2' '3']
print(y) # [1 2 3] 若转换失败会抛出异常

print('使用其他数组的数据类型作为参数')
x = np.array([ 1., 2.6,3. ],dtype = np.float32)
y = np.arange(3,dtype=np.int32)
print(y) # [0 1 2]
print(y.astype(x.dtype)) # [ 0.  1.  2.]