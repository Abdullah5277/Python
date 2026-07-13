''' Data frames are two or more dimmensional data 
if there are only one column in data set we called series if there are 2 or above then data yhen it is called dataset'''
import numpy as np
import pandas as pd

# we can make dataframes by using many things such as list ,dict or many more 
# by making Lists 
student_list=[
    ['100%',80,10],
    ['75%',65,8],
    ['98%',78,9.5],
    ['60%',60,7.2]
]
sl=pd.DataFrame(student_list,columns=['iq','marks','pkg'])
print(sl)

# by making dataframe using dict
student_dict={
    'IQ':['100%','85%','90%','70%'],
    'MARKS':[80,77,81,65],
   'PAKAGE':[10,9,9.5,7.8]
}
sd=pd.DataFrame(student_dict)
print(sd)

# in real word data we cannot write datframes we can import by using 
movies=pd.read_csv(r'D:\Pandas\DataFrames_Pandas\movies.csv')
print(movies)
IPL=pd.read_csv(r'D:\Pandas\DataFrames_Pandas\ipl-matches.csv')
print(IPL)
# DataFrame Methods (need parentheses):

#     df.head(n) - first n rows

#     df.tail(n) - last n rows

#     df.sample(n) - random n rows

#     df.info() - DataFrame summary

#   DataFrame Attributes (no parentheses):

#    df.size - total elements

#DataFrame Attributes and Methods Shape,dtypes,index,head and tail sample
print(IPL.shape)
print(movies.dtypes)
print(IPL.index)
print(IPL.head())# default it fetch first  5 items if we fetch 2 items we use indexin
print(IPL.tail())
print(IPL.columns)
print(IPL.rpow)
print(IPL.sample(5))   
print(IPL.info()) 
print(IPL.duplicated().sum()) 

