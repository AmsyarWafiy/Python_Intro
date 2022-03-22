import pyodbc  # Library
# Connection String # conn Connection name
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-9OO4SGRU\SQLEXPRESS;'
                      'Database = IRAcademy;'
                      'Trusted_Connection = yes;') # Windows Authentication
cursor = conn.cursor() # initialization of connection

print('MENU')
print('=========')
print('1 -> Add new Student to the list ')
print('2 -> Add Student Mark Detail ')
print('3 -> Delete Student Information ')
print('4 -> Update Student Information ')
print('5 -> Search Student Information ')
print('6 -> Display Student Report \n')

while True:
    choice = int(input('Enter your choice :\n'))
    if choice == 1:
        name = input('Enter Students Name :')
        Date = input("Enter Students date of birth. ")
        Age = int(input("Enter Students age. "))
        Street = input("Enter Students Street. ")
        PostalCode = input("Enter Students Postal Code. ")
        State = input("Enter student state. ")
        Country = input("Enter Students Country. ")
        Phone = input("Enter Students phone number. ")
        Email = input("Enter Students email. ")

        cursor.execute("""Insert into IRAcademy.dbo.Student_Personal(Std_Name, Std_DOB, Std_Age, Std_Street, Std_PostalCode, 
         Std_State, Std_Countryname, Std_Phoneno, Std_Email) values (?,?,?,?,?,?,?,?,?)""", (name, Date, Age, Street, PostalCode, State, Country, Phone, Email))
        print("And new record have been inserted successfully")
        conn.commit()

    elif choice == 2:
        ID = int(input("Enter student ID. "))
        Malay = int(input("Enter Malay subject mark. "))
        English = int(input("Enter English subject mark. "))
        Science = int(input("Enter Science subject mark. "))
        Maths = int(input("Enter Maths subject mark. "))
        Arts = int(input("Enter Arts subject mark. "))
        History = int(input("Enter History subject marks. "))
        Geography = int(input("Enter Geo subject marks. "))
        Total = Malay + English + Science + Maths + Arts + History + Geography
        Average = Total / 7

        if Malay >= 40 and English >= 40 and Science >= 40 and Maths >= 40 and Arts >= 40 and History >= 40 and Geography >= 40:
            Result = 'PASS'
        else:
            Result = 'FAIL'

        if Average > 80 and Result == 'PASS':
            Grade = 'A+'
        elif Average <= 80 and Average > 70 and Result == 'PASS':
            Grade = 'A'
        elif Average <= 70 and Average > 60 and Result == 'PASS':
            Grade = 'B'
        elif Average <= 60 and Average > 50 and Result == 'PASS':
            Grade = 'C'
        else:
            Grade = 'F'

        cursor.execute("""Insert into IRAcademy.dbo.Marks(Std_ID, Malay, English, Science, Maths, Arts, History, Geo, Total, Average, Result, Grade)
                                values (?,?,?,?,?,?,?,?,?,?,?,?)""",
                    (ID, Malay, English, Science, Maths, Arts, History, Geography, Total, Average, Result, Grade))
        print("All marks successfully added.")
        conn.commit()

    elif choice == 3:
        ID = int(input("Enter student ID to delete. "))

        cursor.execute("Delete from IRAcademy.dbo.Student_Personal where Std_ID = " + str(ID))

        print("The student information successfully deleted.")
        conn.commit()

    elif choice == 4:
        ID = int(input("Enter student ID to update. "))
        name = input('Update new Students Name :')
        Date = input("Update newStudents date of birth. ")
        Age = int(input("Update new Students age. "))
        Street = input("Update new Students Street. ")
        PostalCode = input("Update new Students Postal Code. ")
        State = input("Update new student state. ")
        Country = input("Update new Students Country. ")
        Phone = input("Update new Students phone number. ")
        Email = input("Update new Students email. ")

        cursor.execute("""update IRAcademy.dbo.Student_Personal set Std_Name = ?, Std_DOB = ?, Std_Age = ?, Std_Street = ?, 
          Std_PostalCode = ?, Std_State = ?, Std_Countryname = ?, Std_Phoneno = ?, Std_Email = ? where Std_ID = ?""",
                       (name, Date, Age, Street, PostalCode, State, Country, Phone, Email, ID))
        print("Student information successfully updated.")
        conn.commit()

    elif choice == 5:
        ID = int(input("Enter student ID. "))
        name = input("Enter student name. ")

        cursor.execute("Select * from IRAcademy.dbo.Student_Personal where Std_ID = %d or Std_Name ='%s'"%(ID, name))
        result = cursor.fetchall()
        for i in result:
            print(i)
        conn.commit()

    elif choice == 6:

        ID = int(input("Enter your ID for students academic report. "))
        cursor.execute("Select IRAcademy.dbo.Student_Personal.Std_ID, Std_Name, Std_Age, IRAcademy.dbo.Marks.Malay, "

                    "English, Science, Maths, Arts, History, Geo, Total, Average, Result, Grade from "

                    "IRAcademy.dbo.Student_Personal full outer join IRAcademy.dbo.Marks on "

                    "IRAcademy.dbo.Student_Personal.Std_ID = IRAcademy.dbo.Marks.Std_ID where "

                    "IRAcademy.dbo.Student_Personal.Std_ID = " + str(ID))

        result = cursor.fetchone()
        print(result)
        conn.commit()

    process = int(input('Press 1 to continue, Press 0 to exit '))
    if process == 0:
        print("Bye-bye")
    break