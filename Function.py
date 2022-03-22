
##define a function

def display():
    print("IRAcademy")

#function call
display()

#create read() function to read two numbers
num1=int(input("put num1 "))
num2=int(input("put num2 "))

def read(num1,num2):
    print("num1:",num1,"\nnum2:",num2)
read(num1,num2)

#create add() function to find sum of two numbers

def add():
    print('Addition of two numbers is: ',num1+num2)
add()

#create display() function to display output

def display():
    print("addition of two numbers:",+str(num1+num2))
display()

#local and global; variable
n1=10 #global variable
def getnumber():
    #local variable
    #n1=20
    x=200
    print('Local variable n1 '+str(n1 ))
    print('Local variable x',x)

getnumber()
#cant print local varible
#print ('local variable',x)
print('GLobal variable '+str(n1 ))

#function with arguement passing
def readme(myname):
    print("Your name is",myname)

#function call
readme('Wafiy')

