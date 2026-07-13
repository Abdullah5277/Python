# maths methood sum min max sum var median mode 

import numpy as np
import pandas as pd


movies=pd.read_csv(r'D:\Pandas\DataFrames_Pandas\movies.csv')
print(movies)
IPL=pd.read_csv(r'D:\Pandas\DataFrames_Pandas\ipl-matches.csv')
print(IPL)

# by making dataframe using dict
student_dict={
    'name':["Mudassir","Salman","Mona","Ubaid"],
    'IQ':[100,85,90,70],
    'MARKS':[80,77,81,65],
   'PAKAGE':[10,9,9.5,7.8]
}
sd=pd.DataFrame(student_dict)
print(sd)
sd.set_index('name',inplace=True)
print(sd)
# # if we need row side sum we use hidden parameter such re axis =1 means row 0 means colmn
# print(sd.sum())
# # print(sd.mean())
# # print(sd.median())
# print(sd.min())
# print(sd.var())

## scrolling Rows from a DataFrame.

# print(type(IPL['Venue']))
# print(movies['title_x'])
# print(movies[['title_x','original_title','year_of_release']])
# in ILOC we use index such that 0,1,2,3 but in loc we get proper label name 'salman
#iloc seareches by indexing position we want 1 row 
#loc- searches using index labels 
print(movies.iloc[0]) # its type are series
print(movies.iloc[0:5]) # 

#loc work with  label
print(sd.loc['Salman'])
# By using fancy indexing
print(sd.loc[['Salman','Mudassir','Ubaid']])



# Selecting both rows and colmn 
print(movies.iloc[0:3,0:3])
# Same thing by using loc 
print(movies.loc[0:2,'title_x':'poster_path'])

