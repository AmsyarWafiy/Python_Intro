#Delete records
import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-9OO4SGRU\SQLEXPRESS;'
                      'Database = IRAcademy;'
                      'Trusted_Connection = yes;')

cursor = conn.cursor()
cursor.execute('Delete IRAcademy.dbo.Table_Python where id = 2')
print('Record successfully deleted...........')
#cursor.execute('Delete CityLabs.dbo.Socso_Python where id = %s, @id)
conn.commit()