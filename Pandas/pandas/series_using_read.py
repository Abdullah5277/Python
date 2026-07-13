import pandas as pd
'''There are two ways to read csv file 1 are to copy path by using double click and 2 are where you download csv file'''
result = pd.read_csv(r"C:\Users\DELL\Downloads\bollywood.csv",index_col='movie').squeeze()
#print(result)
result2 = pd.read_csv('D:\Pandas\pandas\subs.csv').squeeze()

# print("Choklii .csv")
result1 = pd.read_csv(r"C:\Users\DELL\Downloads\kohli_ipl.csv",index_col='match_no').squeeze()

print(result1)
# print("Subscribers")
#print(result2)   
'''Methods of CSV'''
# Head and tail methood,sample,value_counts,sort values
# print(result.head())
# print(result2.tail())
# print(result2.sample() )# it gives 1 row for sample
# print(result2.sample(5) )# it gives 5 when write 5 row for sample
print(result.value_counts())# agr mujha ya nkalna ha ka 1 actor na kitni movie use ki 
print(result1.sort_values())# arrange the values 
#print(result.sort_index(inplace=True))# not use inplace because they change the data permanetly in sorting or indes or ascending
print(result)


# series math methods count,sum ,product,mean .median ,mode std,var,min,max,describe
print(result.count())
print(result1.sum())
print(result1.prod())
print(result1.mean())
print(result1.median())
print(result1.mode())
print(result1.std())
print(result1.var())
print(result1.min())
print(result1.max())
print(result1.describe())



