import numpy as np

#isin():are used to search multiple items from array
a=np.array([3,5,75,25,45,6,78,80,60])

items=[10,20,30,40,50,60,]
print(np.isin(a,items))

# flip func reversed the order in the array  
print(np.flip(a  ))

#Put relaces the element of array with given values of p_array.
print(np.put(a,[0,1],[110,34]))
print(a)

# Delete 
# Set f
m=np.array( [1,2,3,456])
n=np.array( [1,2,3,456])
print(np.union1d(m,n))
           

# clip() the value in the array
print(np.clip(a,a_min=25,a_max=75))