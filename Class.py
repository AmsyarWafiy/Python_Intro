#create class with property

class stdclass:
    rollno=101 #one attributes

#create Object
stdobj = stdclass()
print(stdobj.rollno)

#class with method
class stdclass:
    rollno=101 #one attributes
    def display(self):
        print("Rollnp",self.rollno)

#create object
stdobj = stdclass()
stdobj.display()

stdobj2=stdclass
stdobj2.rollno =102 #modify the object properties
stdobj2.display()

class Employee:
    empid : 100
    empname = 'Mr Jai'
    empage = 30
    empadress = 'Perak'
    empjob = 'Programmer'

    def displayemp(self): #method
        print(self.empid, self.empname, self.empadress)

emp = Employee()
emp.displayemp()
emp2= Employee
emp2.empid = 1002
emp2.empname = 'Mr Ali'
emp2.empadress = 'Kedah'
emp2.displayemp()

#self Parameter
class Employee:
    def __init__(my, name1, age1, salary1):
        my.name = name1
        my.age = age1
        my.salary = salary1
#create Object
emp = Employee("William", 36, 1500)

print(emp.name)
print(emp.age)
print(emp.salary)


# Create Class
class Addition:
    first = 0
    second = 0
    answer = 0

    # parameterized constructor
    def __init__(self, f, s1):
        self.first = f
        self.second = s1

    def display(self):
        print("First number = " + str(self.first))
        # print("First number = ",self.first)
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second


# creating object of the class
# this will invoke parameterized constructor

obj = Addition(10, 20)
# perform Addition
obj.calculate()
# display result
obj.display()

