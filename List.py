#Create List
namelist=['Sofia','Mun wai','Wafiy','Daniel','Yazmin','Syahadah']
print(namelist)

#Data type
print(type(namelist))

#Find Length of list
print(len(namelist))

#Create Empty list find length of list name2
empty_1=[]
print(empty_1)

# Positive indexing
numbers=[1,2,3,4,5]
numbers[2]

#Negative Indexing
numbers=[1,2,3,4,5]
print(numbers[-1])

#Range of Indexes
print(numbers[2:4])

#Change Item Value
numbers[0]=100
print(numbers)

#Change a Range of Item Values
numbers[1:3]=[10,20]
print(numbers)

#Insert Items
numbers.insert(0,50)
print(numbers)

"""
append() -Adds an element at the end of the list
clear() -Removes all the elements from the list
copy() -Returns a copy of the list
count() -Returns the number of elements with the specified value
extend() -Add the elements of a list (or any iterable), to the end of the current list
index() -Returns the index of the first element with the specified value
insert() -Adds an element at the specified position
pop() -Removes the element at the specified position
remove() -Removes the item with the specified value
reverse() -Reverses the order of the list
sort() -Sorts the list
"""
# assign list
numbers = [1, 2, 3, 2, 3, 4, 5]
print(numbers)
del numbers[2] # use del
print(numbers)
numbers.remove(3)
print(numbers)
numbers.pop(3)
print(numbers)

# assign list
numbers = [1, 2, 3, 2, 3, 4, 5]
print(numbers)
del numbers[2] # use del
print(numbers)
numbers.remove(3)
print(numbers)
numbers.pop(3)
print(numbers)

# operations on a list
lst = [4,5,3,5]
print(lst)
old_lst = lst[:]
# append to the exsting list
old_lst.append(80)
print("lst = ", lst)
print("old_lst = ", old_lst)

elt1 = 101, 102, 103
lst.extend(elt1)
print(lst)

elt2 = (201, 203, 205)
lst.append(elt2)
print(lst)

lst.extend('xyzw')
print(lst)

lst.append('www.google.com')
print(lst)

# insert an element into the exsting list at a particular position
# insert value 833 at index 1
lst.insert(1, 833)
print(lst)

# remove and return the last element
k = lst.pop()
print(k)
print(lst)

print(lst)

[23, 65, 76, 833, 95, 22].index(833)

"xxxxyzyzyz".rindex('yz')

# remove and return the element at index i
i = 2
k = lst.pop(2)
print(k)
print(lst)

#Clear the List
lst.clear()
print(lst)

#loop through a list
numbers=[10,20,30,40,50]
for i in numbers:
  print(i)

#Loop Through the Index Numbers
numbers=[10,20,30,40,50]
for i in range(len(numbers)):
  print(i)

#Using a While Loop

i=0
while i<len(numbers):
  print(numbers[i])
  i+=1

#Looping Using List Comprehension
names=['janu','banu','anu']
[print(i) for i in names]
pass

#Sort List Alphanumerically
names.sort()
print(names)

#Sort List Numerically
numbers=[10,5,2,90]
numbers.sort()
print(numbers)

def myfunc(n):
  return abs(n - 50) #Sort the list based on how close the number is to 50:
thislist = [100, 50, 65, 82, 23] #The function will return a number that will be used to sort the list (the lowest number first):
thislist.sort(key = myfunc) #keyword argument
print(thislist)

#Copy a List
list1=[1,2,3]
list2=[4,5,6]
list3=list1
print(list3)

list4=list1.copy() #Make a copy of a list with the copy()
print(list4)
list5=list(list1) #make a copy is to use the built-in method list()
print(list5)