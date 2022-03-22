def display():
    print()
display()

def read():
    num1 = int(input("put num1 "))
    num2 = int(input("put num2 "))
    add(num1,num2)#nested function

def add(num1,num2):
    result=num1+num2
    display(result)#nested function

def display(result):
    print("addition of two numbers= ",result)

#function call
read()

#display number from 1 to 10 using function
def display():
    for i in range(1,11):
        print(i)
display()

#Student mark calculation using function
#Create a function with name  Readstdinfo() which is used to read student information like stdrollno, stdname,Malay,Maths & Science
#Create a function with name  Calculate() which is used to calculate total and find result of the student
#Create a function with name  Display() which is used to display student details

def readstdinfo():
    global stdrollno,stdname,Malay,Math,Science
    stdrollno = int(input("Student Roll No: "))
    stdname = input("Students name:  ")
    Malay = int(input("Malay mark: "))
    Math = int(input("Math mark: "))
    Science = int(input("Science mark: "))

   # Calculate (Malay,Math,Science)

def Calculate():
    global total,result

    if Malay >= 40 and Math >= 40 and Science >= 40:
        result='Pass'
    else:
        result='Pass'
    total = Malay+Math+Science

def Display():
    print("stdrollno",stdrollno)
    print("name",stdname)
    print("malay",Malay)
    print("math",Math)
    print("science",Science)

