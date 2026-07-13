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
# sd=pd.DataFrame(student_dict)
# print(sd)
# sd.set_index('name',inplace=True)
# print(sd)

# # find all winners of match
# mask=IPL['MatchNumber']=='Final'
# print(IPL[mask])
# new_Df=IPL[mask]
# print(new_Df[['Season','WinningTeam']])

mask=IPL['SuperOver']=='Y'
print(IPL[mask])
print(IPL[mask].shape)
#this was not correct syntax
# filter= IPL[(IPL['City'] == 'Kolkata')]
# csk = filter[filter['WonBy'] == 'Chennai Super Kings']
# print(csk)

data=(IPL[IPL['TossWinner']==IPL['WinningTeam'].shape[0]/IPL.shape[0]])*100
print(data)