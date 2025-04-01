# .append()

mylist=[]
print(mylist)

mylist.append(125)
print(mylist)

mylist.append("python")
print(mylist)

mylist.append(("js",4500))
print(mylist)

mylist.append([100,800,300])
print(mylist)

mylist.append({1,1,2,3})
print(mylist)

# .insert()
x=[]
print(x,id(x))

x.insert(4,"red")
print(x)
print(x[0])

x.insert(0,"green")
print(x)

x.insert(4,"blue")
print(x)


#WAP to take student count from user and neter student name then after show all student name
count=int(input("Enter count of students: "))
students=[]

for i in range(1,count+1):
    name=input(f"Enter {i} Student name: ")
    students.append(name)

print(f"Names:{students}")