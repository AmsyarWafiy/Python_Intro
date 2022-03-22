x = 3.3
y = 3.3
if x is y:    # x and y (are operands) operand is (operator)
    print("x & y  is of same identity")
y = 6
if x is not y:
    print("x & y have different identity")
x = 5
if type(x) is int:
    print("X is integer data type")
else:
    print("X is not integer data type")
#True
print(type(x) is not float)
#True
y = 3.23
print(type(y) is not float)
#False
print(type(y) is int)
#False

list1 = [1, 2, 3, 'a']
list2 = [10, 20, 30]
# using is operator
if list1 is list2:
 print("True")
else:
 print("False")
