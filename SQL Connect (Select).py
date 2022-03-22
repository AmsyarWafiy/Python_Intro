import pyodbc  # Library
# Connection String # conn Connection name
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-9OO4SGRU\SQLEXPRESS;'
                      'Database = IRAcademy;'
                      'Trusted_Connection = yes;') # Windows Authentication
cursor = conn.cursor()
cursor.execute('Select * from IRAcademy.dbo.Table_Python')
result = cursor.fetchall() # result = (1, 2, 3,) or result = ((1, 3), (4, 5),)
for x in result:
    print(x)
conn.commit()