#Left Incremental Triangle
'''
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
'''


#Left Decremental Triangle
'''
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


'''
row = int(input("Enter the number of rows for Number Pattern: "))
for i in range(1,row+1):
    count=i
    for j in range(1,i+1):
        print(count, end=" ")
        count= count + (row-j)
    print()

OUTPUT:
Enter the number of rows for Number Pattern: 7
1 
2 8 
3 9 14 
4 10 15 19 
5 11 16 20 23 
6 12 17 21 24 26 
7 13 18 22 25 27 28 
'''

# Right Incrememental Triangle
'''
row=int(input("Enter rows: "))
for i in range(1,row+1):
    for j in range(row-i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()

OUTPUT:
Enter rows: 5
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
'''

# Right Drecremental Triangle
'''
row=int(input("Enter rows: "))
for i in range(1,row+1):
    for j in range(i):
        print(" ", end=" ")
    for k in range(row-i):
        print("*", end=" ")
    print()

OUTPUT:
Enter rows: 6
  * * * * * 
    * * * * 
      * * * 
        * * 
          * 
'''

# Pyramid 
'''
row=int(input("Enter rows: "))
for i in range(1,row+1):
    for j in range(row-i):
        print(end=" ")
    for k in range(i):
        print("*", end=" ")
    print()

OUTPUT:
Enter rows: 6
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
* * * * * * 
'''

# Reverse Pyramid
'''
row=int(input("Enter rows: "))
for i in range(row,0,-1):
    for j in range(row-i):
        print(end=" ")
    for k in range(i):
        print("*", end=" ")
    print()

OUTPUT:
Enter rows: 6
* * * * * * 
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 
'''

# Diamond
'''
row=int(input("Enter rows: "))
for i in range(1,row+1):
    for j in range(row-i):
        print(end=" ")
    for k in range(i):
        print("*", end=" ")
    print()
for i in range(row-1,0,-1):
    for a in range(row-i):
        print(end=" ")
    for b in range(i):
        print("*", end=" ")
    print()

OUTPUT:
Enter rows: 5
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
'''


# Pyramid of odd nummber of stars / Hill Incremental 1
'''
row=int(input("Enter rows: "))
for i in range(1,row+1):
    for j in range(row-i):
        print(end="  ")
    for k in range(2*i-1):
        print("*", end=" ")
    print()

OUTPUT:
Enter rows: 5
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
'''

# Hill decremental
'''
row=int(input("Enter rows: "))
for i in range(row,0,-1):
    for j in range(row-i):
        print(end="  ")
    for k in range(2*i-1):
        print("*", end=" ")
    print()

OUTPUT:
Enter rows: 5
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
'''


# Aptitude question 1: 8*8 matrix of 0's and 1's while 1's must be on left diagonal
'''
1 0 0 0 0 0 0 0 
0 1 0 0 0 0 0 0 
0 0 1 0 0 0 0 0 
0 0 0 1 0 0 0 0 
0 0 0 0 1 0 0 0 
0 0 0 0 0 1 0 0 
0 0 0 0 0 0 1 0 
0 0 0 0 0 0 0 1 
'''
# Answer
'''
row = 8
for i in range(1, row+1):
    for j in range(1,row+1):
        if i==j:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()

OUTPUT:
1 0 0 0 0 0 0 0 
0 1 0 0 0 0 0 0 
0 0 1 0 0 0 0 0 
0 0 0 1 0 0 0 0 
0 0 0 0 1 0 0 0 
0 0 0 0 0 1 0 0 
0 0 0 0 0 0 1 0 
0 0 0 0 0 0 0 1 
'''

row=5
count=1
for i in range(1,row+1):
    for j in range(1,row+2):
        if i%2==0:
            if j%2==0:
                print(count, end=" ")
                count+=1
            else:
                print("*", end=" ")
        else:
            if j%2==0:
                print("*", end =" ")
            else:
                print(count, end=" ")
                count =  count +1
    print()