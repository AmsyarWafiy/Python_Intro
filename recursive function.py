#Find Factorial of given number using function
def findfact(num):
  f=1
  for i in range(1,num+1):
     if num==0:
       return 1
     else:
        f=f*i
  return f

num=int(input("Enter the number"))
print("Factorial value is",findfact(num))

#Find Factorial of number using recursive function
def recur_fact(n): #Function definition
   if n == 0:
       return 1
   else:
       return n*recur_fact(n-1)  #Recursive function - function call itself

num =int(input("Enter your number"))
print('Factorial of given number is =',recur_fact(num))
print('Factorial of {} is ='.format(num),recur_fact(num))