import pandas as pd
import numpy as np

a = pd.Series([100,200])
print(a)
print('Total value of data set is=',np.sum(a))

#Count data set
print('Count number of values in the data set is=',len(s))

#Fetch the information from begining to end

s+=10 #adds two to each item in s using broadcasting
s.head() #head()-which is used to fetch data from begining

s = pd.Series(np.random.randint(0,1000,10000))
print(s)
print(s.head())