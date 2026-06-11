import numpy as np

a=np.array([1,2,3,4])
print(a)
# print(type(a))

# 2D array it is also called matric
b=np.array([[12,3,4,2],[234,5,6,7]])
print(b)

# if we want diffrent data type of then syntax are np.array([1,23,4],d=str,float)
c=np.array([1,23,4],dtype=float)
print(c)

# arange such that loop so syntax are
print(np.arange(1,11))

# reshape means divide into such parts syntax are 
print(np.arange(1,11).reshape(5,2))
#example are 
#[[ 1  2]
#  [ 3  4]
#  [ 5  6]
#  [ 7  8]
#  [ 9 10]]

# Np.zeros or ones 
print("Ones arrray")
print(np.ones((3,4)))
print("Zeros arrray")
print(np.zeros((3,4)))
print("Linespace arrray")
print(np.linspace(3,4,5))
print("identity arrray")
print(np.identity(3))
print("Random arrray")
print(np.random.random((1,4,4)))