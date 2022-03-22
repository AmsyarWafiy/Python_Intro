#Create python program to perform arithmetic operation using single inheritance
class Readnum: #Parent class
  def __init__(self,f,s):#parameterized constructor
    self.first=f
    self.second=s

  def displaynumber(self):
    print("First number is",self.first)
    print("Second number is",self.second)

class Myarithmetic(Readnum):  #Child/Derived class
     #def __init__(self,f,s):
     #  Readnum.__init__(self,f,s)
    def arith_operations(self):
        print("Addition value is",self.first+self.second)
        print("Subtraction value is",self.first-self.second)
        print("Multiplication value",self.first*self.second)
        print("Division value",self.first/self.second)
        print("Modulus value",self.first%self.second)

num1=int(input("Enter First number"))
num2=int(input("Enter Second number"))
op=Myarithmetic(num1,num2) #create object for child class
print()
op.displaynumber() #Invoke parent class method
print("\nArithmetic Operations")
print("---------------------")
op.arith_operations() #Invoke child class method