import numpy as np
a1=np.random.random((3,3))
a1=np.round(a1*100)
print(a1)

#sum min max prod
print(np.max(a1))
#0->colmn , 1->rows
print(np.max(a1,axis=1))

print(np.min(a1))
print(np.sum(a1))
print(np.prod(a1))

#mean median std var 
print(np.mean(a1))
print(np.median(a1))
print(np.std(a1))
print(np.var(a1))

#dot product 
a2=np.arange(12).reshape(3,4)
a3=np.arange(12,24).reshape(4,3)
print(np.dot(a2,a3))

#log And exponents 
np.log(a1)
np.exp(a1)

#round /ceil /floor
print(np.round(np.random.random((2,3))*100))
print(np.ceil(np.random.random((2,3))*100))
print(np.floor(np.random.random((2,3))*100))