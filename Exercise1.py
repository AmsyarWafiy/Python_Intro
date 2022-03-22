nameList = ['Ali','Abu','Amin','Ah meng','Wafiy']
process = 1

while process == 1:
    print('MENU')
    print('=========')
    print('1 -> Add name to the list ')
    print('2 -> Remove name from list ')
    print('3 -> Search name from list ')
    print('4 -> Display the list\n ')

    choice = int(input('Enter your choice :\n'))

    if choice == 1:
        name = input('Enter Name :')
        nameList.append(name)

    elif choice == 2:
        name = input('Enter a name to remove :')
        nameList.remove(name)
        print(name, ' is successfully removed')

    elif choice == 3:
        name = input('Enter name to search :')
        for i in range(0,len(nameList)):
            if nameList[i] == name:
                print (name,'is in the list ')
            else:
                print (name,' is not in the list \n')

    else:
        for a in range(0,len(nameList)):
            print ((a+1), 'Name :', nameList[a])

    process = int(input('Press 1 to continue, Press 0 to exit '))
if process == 0:
    print("Bye-bye")
