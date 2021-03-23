# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 10:23:33 2021

@author: great
"""

#To start with every project in data, we import pandas and numpy, and define the max display of rows and columns:

import pandas as pd
import numpy as np 

pd.options.display.max_columns = None
pd.options.display.max_rows = None

#Then, we get our dataframe from NISPUF17.csv and we can print out the head of it 

df = pd.read_csv('NISPUF17.csv') #Please, note that the csv file need to be at the same directory as your code file, or you can copy the path
print(df.head())

'''
Notice that we dont have idea of what all this variables in columns represent, so we need to study the ones
we want to work with, and this is part of the work of a data scientist too, so open the NIS-PUF17-DUG.pdf 
and read about the variables we will work first

In this first part we want to discover the PROPROTION OF CHILDREN who had the MOTHER with EDUCATION LEVELS 
equal to: LESS THAN HIGHSCHOOL, EQUAL TO HIGHSCHOOL, MORE THAN HIGHSCHOOL BUT NOT COLLEGE GRADUATE and
COLLEGE DEGREE
'''

'''
Page 55 says: "The age, education level, and marital status of the mother of the child are
stored in variables M_AGEGRP2, EDUC1, and MARITAL2 (married vs. not married), with missing
values imputed."

That means that our mother education level is stored in EDUC1 variable, and that is confirmed in page 51:

EDUC1 – education of the mother : 
                                - <12 years
                                - 12 years
                                - >12 years, not a college graduate
                                - College graduate

So the thing is: we need to get each one of this data and divide for the total of mothers
'''

#We will work with only one column, so we dont need to focus in dataframe, we can use only Series, that is a part of a df

MOM = df['EDUC1']
mom = np.sort(MOM.values) #And this way we create a series called 'mom' that is just a copy of MUM but SORTED
print(mom)

n = len(mom) #Its the number of elements, that is, the total number of mothers
print(n)