'''
#Left Incremental Triangle
row = int(input("Enter the number of rows for Star Pattern: "))
for i in range(1, row+1):
    for j in range(i):
        print("*", end=" ")
    print()

OUTPUT:
Enter the number of rows for Star Pattern: 3
* 
* * 
* * * 



#Left Decremental Triangle
row = int(input("Enter the number of rows for Star Pattern: "))
for i in range(row, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

OUTPUT:
Enter the number of rows for Star Pattern: 3
* * * 
* * 
* 

'''


'''
row = int(input("Enter the number of rows for Number Pattern: "))
for i in range(1, row+1):
    for j in range(i):
        print(i, end=" ")
    print()

OUTPUT:
Enter the number of rows for Number Pattern: 3
1 
2 2 
3 3 3


row = int(input("Enter the number of rows for Number Pattern: "))
for i in range(1, row+1):
    for j in range(i):
        print(j+1, end=" ")
    print()

OUTPUT:
Enter the number of rows for Matrix Box Number Pattern: 3
1 
1 2 
1 2 3 


row = int(input("Enter the number of rows for Number Pattern: "))
count=0
for i in range(1, row+1):
    for j in range(i):
        count+=1
        print(count, end=" ")
    print()

OUTPUT:
Enter the number of rows for Matrix Box Number Pattern: 3
1 
2 3 
4 5 6
'''

row = int(input("Enter the number of rows for Number Pattern: "))
count=0
for i in range(1,row+1):
    for j in range(i):
    print()


