#What is a Series?
#A Pandas Series is like a column in a table.
# It is a one-dimensional array holding data of any type.
#Show the help
# pd.Series?
#help(pd.Series)
import pandas as pd
#Create a simple pandas series from a list
numbers = [1, 2, 3, 4]
print(pd.Series(numbers))

#Create series for Students name
studentname=['Farhana','Kam','Izuan','Anuar','Ming']
stdname=pd.Series(studentname)
print(stdname)

#Create own labels for Pandas Series
import pandas as pd
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)


#find sum of all values using numpy library

import numpy as np
total = np.sum(s)
print(total)

a = pd.Series([100,200])
print(a)
print('Total value of data set is=',np.sum(a))

#Count data set
print('Count number of values in the data set is=',len(s))

#Fetch the information from begining to end

s+=10 #adds two to each item in s using broadcasting
s.head() #head()-which is used to fetch data from begining

s = pd.Series(np.random.randint(0,1000,10000))
print(s.head())