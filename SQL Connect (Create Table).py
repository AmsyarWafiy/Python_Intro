import pyodbc  # Library
# Connection String # conn Connection name
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-9OO4SGRU\SQLEXPRESS;'
                      'Database = IRAcademy;'
                      'Trusted_Connection = yes;') # Windows Authentication
cursor = conn.cursor() # initialization of connection
cursor.execute("Create Table IRAcademy.dbo.Table_Python"
               "(id int, name varchar(25),"
               " address varchar(25))")
cursor.execute("Insert IRAcademy.dbo.Table_Python values"
               "(1, 'Mr. Ahamad', 'Kuala Lumpur')")
cursor.execute("Insert IRAcademy.dbo.Table_Python values"
               "(2, 'Ms Nadhira', 'Kuala Lumpur')")
print("Python has successfully created Table in SQL Server")
print("And new record have been inserted successfully")
conn.commit()