#Logical operator

a=50
b=40

#and
if a==50 and b==41:
    print ('true')
else:
    print('false')

#or
if a==50 or b==50:
    print ('true')
else:
    print('false')

#not
if not a>= 60:
    print ('true')
else:
    print('false')

age=int(input('Enter your age '))

if age >= 21 and age >= 60:
    print('You are the eligible senior citizen')

else:
    print('You are not eligible senior citizen')

print(10<5 or 10==10)

print(not(10<5))