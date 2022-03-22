# nested while loop
# display the numbers
"""
i=1
while i < 3: #outer loop
    j=1
    while j <= i: #inner loop
        print(i,",",j)
        j += 1
    print("........")
    i += 1

i = 1
while i <= 5:
  j = 1
  while j <= i:
    print(j, end=' ')
    j += 1
  print()
  i+= 1
"""
#find sum of digits

num = 153
res = 0
while num > 0:
    r = num % 10
    res += r
    num = int (num /10)
print('Sum =', res)