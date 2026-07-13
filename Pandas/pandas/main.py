# Pandas is a fast ,powerfull ,flexible and easy to use open source data analysis and multiplying tool
# ,built on the top of the python

'''is a library just like numpy in ml prediction model we know how was the data ,data analyse krna ka lia hmain pandas jasa tool zaroori ha ya bht powerfull ha 
,ya data ka postmatm kr deta ha

a panda is a series is like a colmn in a table 
in pandas there are 2 main types
1)series :A Pandas Series is like a column in a table. It is a 1-D array holding data of any type
2)


Series define:A Pandas Series is like a column in a table. It is a 1-D array holding data of any type
'''
import numpy as np
import pandas as pd
# Series is a class in pandasseries object always have
# two things 1 are index  are auto genrated and 2 are value
country=['pakistan','india','USa','bangali']
print(pd.Series(country))

#index 
runs=[12,23,45,56,67,78]
print(pd.Series(runs))

#custom index 
print("custom indexing ")
marks=[12,23,45,56,67]
country=['pakistan','india','USa','bangali','KSA']
print(pd.Series(marks,index=country))

#setting a name 
print(pd.Series(marks,index=country,name='Country nuclear acids '))
#By using dict 
marks={
    'PF':50,
    'DSA':54,
    'CN':30,
    'OOPS':56
}
marks_series=pd.Series(marks,name="Abdullah ka numbers")
print(marks_series)
# Series Methood
print("Series Methood")
print(marks_series.size)
print(marks_series.dtype)# datatype int
print(marks_series.name)
print(marks_series.is_unique)# gives uniques
print(marks_series.index)
