# append(), insert()

# WAP create mylist add numbers as per asked count from user and show sum of elements.
"""
mylist=[]
count=int(input("Enter count: "))
sum=0

for i in range(count):
    n= int(input(f"Enter {i+1} Number: "))
    mylist.append(n)
    sum += n

print(f"MyList: {mylist}")
print(f"Sum of elements: {sum}")

"""
# WAP create mylist add numbers as per asked count from user and show sum of elements.
"""
oddList=[]
evenList=[]
count=int(input("Enter count: "))

for i in range(count):
    n=int(input(f"Enter {i+1} Number: "))
    mylist.append(n)
    if n%2==0:
        evenList.append(n)
    else:
        oddList.append(n)

print(f"My List: {mylist}")
print(f"Odd List: {oddList}")
print(f"Even List: {evenList}")
"""

# Update elements from list
"""
mylist=["red",45,"white","pooja"]
mylist[0]="black"
print(mylist)

mylist[-2]="Orange"
print(mylist)

x=[1]
print(len(x))

#Deleting element by using pop(), remove() and del
mylist.pop()
print(mylist)

mylist.pop(1)
print(mylist)

mylist.remove("black")
print(mylist)

del mylist[0]
print(mylist)
"""

# reverse()
"""
colors = ["red", "green", "blue"]
print(colors)
colors.reverse()
print(colors)

colors[::-1]
print(colors)

#sort
colors.sort()
print(colors)

x=[2.3,3.1,4.5,7.8]
x.sort(reverse=True)
print(x)

y=[2,5,7,9,6]
x.extend(y)
print(x)

x.extend(["red", "green","blue"])
print(x)
"""

# WAP to create studentList ask name and grades from user as per the count
# Nested List

# Approach 1: Using .append()
"""
studentList=[]
count=int(input("Enter Count for student: "))

for i in range(count):
    name=input(f'Enter {i+1} student name: ')
    grade=input(f'Enter {i+1} Grade: ')
    studentList.append([name,grade])

print(studentList)
"""

# Approach 2: Using .extend
"""
studentList=[]
count=int(input("Enter Count for student: "))

for i in range(count):
    name=input(f'Enter {i+1} student name: ')
    grade=input(f'Enter {i+1} Grade: ')
    studentList.extend([name,grade])

print(studentList)
"""


# .copy()
'''
a = [1, 1, 1]
print(a, id(a))

b = [2, 2, 2]
print(b, id(b))

c = a.copy()
print(c, id(c))

z = a
print(z, id(z))

x = a[::]
print(x, id(x))
'''

#.clear()
'''
a = [1, 1, 1]
a.clear()
print(a)
'''

# .count()
'''
y=[23,2,23,45,12,1,23]
print(y.count(23))
print(y.count(230))
print(y.count(""))
'''