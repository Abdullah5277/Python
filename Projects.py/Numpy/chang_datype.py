# astype means that agr mujha kisi ki age store krni ha to max 120 saal ho gi ma apni 
# memory zaroor 64 bit use kru ya kam mera 32 bits bhi kr skta ha 
 
import numpy as np


a1 = np.arange(10)
a1= a1.astype(np.int32)
print(a1.dtype)

a2=np.arange(12,dtype=float)
a2=a2.astype(np.int8)
print(a2.dtype)

#Array Opperation
a3=np.arange(12).reshape(3,4)
print(a3)
a4=np.arange(12,24).reshape(3,4)
print(a4)
#Scalar or arithmatic operation 
print(a1*2)
print(a1/2)
print(a3+3)

#relation Operator for comapre 
print(a3<3)

#vector Operations

print(a1**a1)