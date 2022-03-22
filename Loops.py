'''
#Display even number
i = 1
while i <= 20:
    if i % 2 == 0:
        print(i, end=' ')
    i += 1
print('end of program')

#display your name
i = 1
while i <= 10:
    print('Wafiy')
    i += 1
print('end of program')
'''
'''
#display multiplication table

i = 1
num = int(input('Enter the multiplication value'))
while i <= 16:
    print( i,'X',num, '=', num*i )
    i += 1
'''
# Example of break statement
num = 1
while num <= 5:
    #if(num == 3):
        #break  # The break statement only terminates the loop, it does not completely stop the flow of the program.
    print(num)
    num += 1
else:
    print('Everything is fine')
print("End of program")

# Example of continue statement
num = 0
while num < 5:
    num += 1            # similiar to  num=num+1
    if num == 4:
        continue  # The continue statement only skips one iteration of the loop, it does not completely stop the flow of the program.
    print(num)
print("End of program")

# Example of pass statement
i=1
while i<5:
    pass #do nothing
i=i+1