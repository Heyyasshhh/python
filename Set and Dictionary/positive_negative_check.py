# WAP to print true for +ve number and false for -ve number but take any 10 number from user 
myList=[int(input("Enter count: ")) for i in range(11)]
print(myList)
print([True if i>0 else False for i in myList])