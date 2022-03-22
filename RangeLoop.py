"""
#Display numbers - for loop using range function with one parameter

for i in range(6):  # Taken value between 0-5 (6-1)
 print(i)

#Display numbers - for loop use range function with two parameter
for i in range(1,6): # Taken value between 1-5
 print(i)

#Display numbers - for loop use range function with three parameter
for i in range(1,10,2):
 print(i)


num = 5
for i in range (1,19):
    print(num, 'x', i, '=', num*i)

for i in range (10):
    print(i)
    pass

for i in range (10):
    if i ==5: #break at 5
        break
        print(i)

for i in range (10):
    if i == 3:
        continue #missing 3 and continue at 4
    print(i)

for i in range (10):
    pass #nothing lmao
"""
#with break statement
for i in range (10):
    if i==3:
        break
    print(i)
else:
    print("Successfully exit for loop")
print("Exit")