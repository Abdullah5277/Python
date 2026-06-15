# we use indexing to fetch data from array
import numpy as np
a1=np.arange(10)
a2=np.arange(12).reshape((3,4))
a3=np.arange(8).reshape(((2,2,2))) #tensor matrix 
# print(a1, a2, a3)

# print(a1[-1])

# print(a2[1,1]) #5
# print(a2[2,3]) #11
# print(a3[1,0,1]) #5


# #Slicing it means multiple items are get 
# print(a1[2:5:1]) #1d
# print(a2[1,:]) #if we want row then [1,:]4 5 6 7
# print(a2[:,2]) #if we want row then [:,2] 2,6,10
# print(a2[::2,1::2]) #if we want row then [:,2] 2,6,10
# print(a2[0:2,1:]) #if we want row then [:,2] 2,6,10

a3=np.arange(27).reshape(3,3,3)
print(a3)
print(a3[::2]) #::means ka 2 ko nkal do baqii sb print kr 
print(a3[0,1,:]) #::means ka 2 ko nkal do baqii sb print kr 
print(a3[1,:1]) #::means ka 2 ko nkal do baqii sb print kr 
print(a3[2,1:,1:]) #::means ka 2 ko nkal do baqii sb print kr 
print(a3[0:2:,2:]) #::means ka 2 ko nkal do baqii sb print kr 
