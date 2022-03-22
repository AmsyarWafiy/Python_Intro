# Python SQL Create DB Example
# Library of Codes with various functionalities
import pyodbc  #  Python Open Database Connectivity

# Connection String
# Server Name or SQL Server Instance Name
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-9OO4SGRU\SQLEXPRESS;'
                      'Trusted_Connection = yes;'
                      ) # Windows Authentication
conn.autocommit = True
cursor = conn.cursor()  # initialization of Cursor
cursor.execute("CREATE DATABASE [Big_Data_IRAcademy2]")
print("Database has been created successfully")
