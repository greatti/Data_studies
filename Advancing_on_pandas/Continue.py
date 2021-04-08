import pandas as pd
import numpy as np
import timeit

df = pd.read_csv('C:/Users/great/Documents/GitHub/Data_studies/Advancing_on_pandas/census.csv') #You need to put your path here
pd.options.display.max_columns = None #para nao ter limite de colunas
pd.options.display.max_rows = None #para nao ter limite de linhas
print(df.head())

'''
So, ultill now we did many processes one at a time, but we can use CHAINING to do all at once:
Lets get this dataframe df, use STNAME and CTYNAME as multiindexes and load the dataframe only
to data where ['SUMLEV'] == 50, and rename a column 
'''

df = (df.where(df['SUMLEV'] == 50)
    .dropna()
    .set_index(['STNAME'], ['CTYNAME'])
    .rename(columns = { 'ESTIMATESBASE2010' : 'Estimates Base 2010'}))

print(df.head())

'''
We can question: how fast is realiza all this processes at once when comparad to doing one at a time?

For that we use 'timeit' library in two different functions
'''

def first_approach(): #Doing all at once in 'df'
    global df 
    return (df.where(df['SUMLEV'] == 50)
            .dropna()
            .set_index(['STNAME', 'CTYNAME'])
            .rename(columns = { 'ESTIMATESBASE2010' : 'Estimates Base 2010'}))
    
df = pd.read_csv('census.csv')
timeit.timeit(first_approach, number = 10) #Calculate the time to run this function 10 times 

def second_approach(): #Doing one action at a time in 'df'
    new_df = df[df['SUMLEV'] == 50]
    new_df.set_index(['STNAME', 'CTYNAME'], inplace = True)
    return new_df.rename(columns = {'ESTIMATESBASE2010' : 'Estimates Base 2010'})

df = pd.read_csv('census.csv')
timeit.timeit(second_approach, number = 10)