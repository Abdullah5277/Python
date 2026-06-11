import numpy as np
a1=np.arange(10)
a2=np.arange(12).reshape((3,4))
a3=np.arange(8).reshape(((2,2,2))) #tensor matrix 

# for i in a1:
#     print(i)
    
# for i in a2:
#     print(i)     # IT HAS two d array but in loops they are get in 1 d array
    
# for i in a3:
#     print(i)  # IT HAS three d array but in loops they are get in 2 d array  
    
# for i in np.nditer(a3):  # nditer in a fun that converts all 2d,3d arrays into 1d 
#     print(i)    
    
    
# Transpose of a matrix   
print( np.transpose(a2))

#ravel 
print(np.ravel(a2)) # that converts all 2d,3d arrays into 

#Stacking means to connect to np arrays by using vertiacll or horizentall

a4=np.arange(12).reshape(3,4)
a5=np.arange(12,24).reshape(3,4)
print(np.hstack((a4,a5))) #Horizentally
print(np.vstack((a4,a5)))  # Vertically


#Splitting is oppaosite of stacking
print(np.hsplit(a4,2))#Horizentally
print(np.vsplit(a4,3))  # Vertically