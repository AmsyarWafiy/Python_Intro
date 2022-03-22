import pyodbc  # Library
# Connection String # conn Connection name
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-9OO4SGRU\SQLEXPRESS;'
                      'Database = IRAcademy;'
                      'Trusted_Connection = yes;') # Windows Authentication
cursor = conn.cursor() # initialization of connection
"""cursor.execute("Insert IRAcademy.dbo.Table_Python values"
               "(3, 'Ali', 'Kedah'),"
               "(4, 'Abu', 'Perak'),"
               "(5, 'Amsyar', 'Penang')"
                )
print('Record successfully inserted...........')
"""
myid   = int(input("Please enter id of employee "))
myname = input(" Please enter the name of employee ")
cursor.execute("Delete IRAcademy.dbo.Table_Python where id = %d or name ='%s'" %(myid, myname))
print("Selected Record has been deleted from the Database--------")
conn.commit()

#Fetch records from table

import matplotlib.pyplot as plt
import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-9OO4SGRU\SQLEXPRESS;'
                      'Database = IRAcademy;'
                      'Trusted_Connection = yes;')
cursor = conn.cursor()
cursor.execute('Select * from IRAcademy.dbo.Table_Python')
result = cursor.fetchall()              # result = (1, 2, 3,) or result = ((1, 3), (4, 5),)
print(type(result))
for x in result:
    print(x)
conn.commit()

#fetch records from table getting information from the user
import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-9OO4SGRU\SQLEXPRESS;'
                      'Database = IRAcademy;'
                      'Trusted_Connection = yes;')

myid = int(input("Please enter id of employee "))
cursor.execute('Select * from IRAcademy.dbo.Table_Python where id = %d'%myid)
result = cursor.fetchall()
for x in result:
    print(x)
conn.commit()

import numpy
arr = numpy.array([1,2,3,4,5])
print (arr)