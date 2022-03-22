# Parent class
class FulltimeEmp:
    def __init__(self, name, age):  # Automatically initialize attributes
        self.name = name
        self.age = age

    def info(self):
        print(f"Employee. My name is {self.name}. "
              f"I am {self.age} years old.")

    def EPF(self):
        print("EPF is deducted for my Salary")


# Child class
class ParttimeEmp(FulltimeEmp):
    def __init__(self, name, age):
        FulltimeEmp.__init__(self, name, age)  # Automatically invoke the parent class init method

    def EPF(self):
        print("EPF is not deducted for my Salary")


# Creating Objects of the Class
E1 = FulltimeEmp("Mr. Aysraf", 26)

E2 = ParttimeEmp("Mr. Phan", 44)

for persons in (E1, E2):
    persons.info()
    persons.EPF()