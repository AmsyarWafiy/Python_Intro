#panda library to store big data
import pandas as pd
#create dictionary
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
print(type(mydataset)) #data type of dictionary

myvar = pd.DataFrame(mydataset)
print(myvar)
print(type(myvar))

