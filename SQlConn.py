#python SQL Create DB Example
#library of codes with various functionality
import pyodbc #Python Open Database Connectivity

connection String
server name or SQL Server Instance Name
conn = pyodbc.connect('Driver={SQL Server};'
					   'Server=LAPTOP-9OO4SGRU\SQLEXPRESS;'
					   'Trusted_Connection = yes;'
					   )windows authentication