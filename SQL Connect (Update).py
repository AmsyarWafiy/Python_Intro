import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-9OO4SGRU\SQLEXPRESS;'
                      'Database = IRAcademy;'
                      'Trusted_Connection = yes;')

cursor = conn.cursor()
cursor.execute('''
                Update IRAcademy.dbo.Table_Python
                set address = 'Johor' where id = 1
                ''')
conn.commit()