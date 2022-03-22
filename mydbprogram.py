# Import data visualization packages
import matplotlib.pyplot as plt
import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-9OO4SGRU\SQLEXPRESS;'
                      'Database = IRAcademy;'
                      'Trusted_Connection = yes;')
cursor = conn.cursor()
# Selecting first column to select name and second column
# to select marks
cursor.execute('Select  science, sname from IRAcademy.dbo.M1')
result = cursor.fetchall()
# 'Converting Data Set into a List '
sciencemarks = [i[0] for i in result]
print(sciencemarks)
studentnames = [i[1] for i in result]
print(studentnames)
conn.commit()
# x-coordinates of left sides of bars
x = studentnames
# y-coordinates height of of bars
y = sciencemarks
# labels for bars - Name of student
tick_label = [i[1] for i in result]
# plotting a bar chart
plt.bar(x, y, tick_label=tick_label,
        width=0.5, color=['orange','red', 'green', 'blue', 'black'])
# plot title
plt.title('Students Science Marks Details')
# naming the x-axis
plt.xlabel('Names of Students')
# naming the y-axis
plt.ylabel('Science Marks')

# function to show the plot
plt.show()