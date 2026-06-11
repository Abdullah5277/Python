import numpy as np
a1=np.arange(10)
a2=np.arange(12,dtype=float).reshape(2,6)
a3=np.arange(8).reshape(2,2,2)


print(a1.ndim)# 1d array
print(a2.ndim)# 2d array
print(a3.ndim)# 3d array

# shape 
print(a1.shape)
print(a2.shape)
print(a3.shape)

#size 
print(a1.size)
print(a2.size)
print(a3.size)

#itemsize
print(a1.itemsize)
print(a2.itemsize)
print(a3.itemsize)