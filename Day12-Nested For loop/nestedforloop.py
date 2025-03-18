'''
print("Vertical 5 stars")
for i in range(5):
    print("*")


print("\nHorizontal 5 stars")
for i in range(5):
    print("*",  end=" ")


print("\n3x3 star pattern")
for i in range(3):
    print("*"*3) #Crime


print("\n3x3 star pattern using Nested Loop")
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()



print("\n3x3 star pattern using Nested Loop (Customized / Input by user)")
a = int(input("Enter the number of rows for Matrix Box Star Pattern: "))
b = int(input("Enter the number of columns for Matrix Box Star Pattern: "))
for i in range(a):
    for j in range(b):
        print("*", end=" ")
    print()
'''

'''
for i in range(1,4):
    for j in range(3):
        print(i, end=" ")
    print()

print()

#User Input 
a = int(input("Enter the number of rows for Matrix Box Star Pattern: "))
b = int(input("Enter the number of columns for Matrix Box Star Pattern: "))
for i in range(1,a+1):
    for j in range(1,b+1):
        print(i, end=" ")
    print()

print()

for i in range(1,4):
    for j in range(1,4):
        print(j, end=" ")
    print()

print()

#User Input 
a = int(input("Enter the number of rows for Matrix Box Star Pattern: "))
b = int(input("Enter the number of columns for Matrix Box Star Pattern: "))
for i in range(1,a+1):
    for j in range(1,b+1):
        print(j, end=" ")
    print()
'''


'''
row = int(input("Enter the number of rows for Matrix Box Star Pattern: "))
column = int(input("Enter the number of columns for Matrix Box Star Pattern: "))
count=0
for i in range(1,row+1):
    for j in range(1,row+1):
        count+=1
        print(count, end=" ")
    print()


Output:

Enter the number of rows for Matrix Box Star Pattern: 3
Enter the number of columns for Matrix Box Star Pattern: 2
1 2 3 
4 5 6 
7 8 9 
'''


'''
#Multiplicatioin-Table Printing 

row = int(input("Enter the number of rows for Matrix Box Star Pattern: "))
column = int(input("Enter the number of columns for Matrix Box Star Pattern: "))

for i in range(1,row+1):
    for j in range(1,row+1):
        print(i*j, end=" ")
    print()

#Output:

Enter the number of rows for Matrix Box Star Pattern: 3
Enter the number of columns for Matrix Box Star Pattern: 2
1 2 3 
2 4 6 
3 6 9 
'''