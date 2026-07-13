import pandas as pd

x=pd.Series([12,23,45,65,5,34,433,3,89,9,10])
# seris work on +ve indexing not for -ve indexing 
print(x[1])#23
#print(x[-1])#it gives error 

movies=pd.read_csv(r'D:\Pandas\pandas\bollywood.csv')
print(movies)
choklii=pd.read_csv(r'D:\Pandas\pandas\kohli_ipl.csv')
print(choklii [['match_no', 'runs']])

# # print(movies['Vicky Kaushal'])
# print(choklii[-5:])
# #slicing is +ve
# print(choklii[5:15])

# #Fancy Indexing means has no pattren 
# print(choklii.iloc[[1,2,3,15]])



# # Editing Series 

# #By using dict 
# marks={
#     'PF':50,
#     'DSA':54,
#     'CN':30,
#     'OOPS':56
# }
# marks_series=pd.Series(marks,name="Abdullah ka numbers")
# print(marks_series)
# #we can make same work by indexing slicing or fencing indexing
# marks_series['DSA']=60
# marks_series['SE']=53
# print(marks_series) 
# # Slicing 
# choklii[2:4]=[100,100]
# print(choklii)
# # fancy indexing
# # choklii.iloc[[0,4,3]]=[0,0,0]
# # print(choklii)
# #By usimg label also but in real life ma hmm data ko read krta Write ni krta 

# #Series Wirh python Fuctionalities len/type/sorted/max/min
# print(len(choklii))
# print(type(choklii))
# #print(sorted(choklii))
# print(choklii.max())
# print(choklii.min())

#type converstion 

# print(list(marks_series))
# print(dict(marks_series))

#looping
for i in movies.index:
    print(i)
# Arithmatic opeartor 
