import numpy as np
# # Sort Function
a=np.random.randint(1,100,15)
# print(np. sort(a))

b=np.random.randint(1,12,12).reshape(4,3)
# print(np.sort(b))# Row wise soating
# print(np.sort(b,axis=0))# if we need soting by colomn we use axix=0


# #Append means attach at the end of the array
# print(np.append(a,200))
# result=np.append(b,np.ones((b.shape[0],1)),axis=1) # write braces carefully 1 brace less genrate error
# print(result)

# #Concatinate  means add the array
# c=np.arange(6).reshape(2,3)
# d=np.arange(6,12).reshape(2,3)

# huy=np.concatenate((c,d),axis=1)
# print((huy))

# #Unique it means to get a unique values 
# e=np.array([0,2,4,56,4,7,5,5,6,1,2,3,43,5,5,667,6,4,42,3,4,5,66,4,4,4,2,22,2,3,4,5])
# print(np.unique(e))

# #Expand Means to convert 1d array into 2d array
# print(np.expand_dims(e,axis=0).shape)

# # Where func that use in future imp 
# print(a)
# print(np.where(a>50))
# # replace  value >50 with 0
# print(np.where(a>50,0,a))

# # Np.argmax func() returns indix of the max element of the array
# print(np.argmax(a))
# print(np.argmin(a))
# print(b)
# print(np.argmax(b,axis=0))

# # Cumsum fun is used comulative sum 1

# # 1+2 = 3

# # 1+2+3 = 6

# # 1+2+3+4 = 10

# print(np.cumsum(a))
# print(np.cumsum(b,axis=1)) 

# # Cumprod fun is used comulative *  that multiply the values 
# print(np.cumprod(a))
# print(np.cumprod(b,axis=1))

# # percentile is used to compute the nth percentile of the given data 
# print(np.percentile(a,100))

# # Histogarm frequency count in a given range
# print(np.histogram(a,bins=[0,10,20,30,40,50,60,70,80,90]))

# corrcoef means imp returns pearsob product-moment corelation coefficiants
salary=np.array([20000,30000,40000,345000])
exper=np.array([1,2,3,4])
print(np.corrcoef(salary,exper))