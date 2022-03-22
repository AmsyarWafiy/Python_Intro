#display the number
try:
    print(x) #try block will generate an exception, because x is not defined
except:
    print("kindly define x value and display")

#division of two number using except handling
try:
    n1=int(input('Enter the first number'))
    n2=int(input('Enter the second number'))
    print('division of two numbers= ', n1/n2)
except:
    print('Exception occurs')

#Multiple exception
try:
  x=[1,10,3,4]
  #print(x)
  #print(x[6])
  print(x[1]/0)
except NameError:
  print("Variable x is not defined")
except IndexError:
  print("Your are try to fetch out of range indexed value")
except ZeroDivisionError:
  print("Your are try to find division by zero")
except:
  print("Something else went wrong")
else:
  print("Nothing went wrong")

# Does the except ... order matter?
try:
    5/0
except ArithmeticError:
    print("Bad Divison")
except ZeroDivisionError:
    print("Division by Zero")

# Does the except ... order matter?
try:
    5/0
except ZeroDivisionError:
    print("Division by Zero")
except ArithmeticError:
    print("Bad Division")

# Does the except ... order matter?
try:
    5/0
except Exception:
    print('Catch All')
except ArithmeticError:
    print("Bad Division")
except ZeroDivisionError:
    print("Division by Zero")