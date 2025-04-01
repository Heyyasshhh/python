#WAP to sort the elements in Ascending order
#NOTE: can not use any in build methods (except: .append())

mylist = []
count = int(input("Enter count: "))

for i in range(count):
    n = int(input(f"Enter {i+1} element: "))
    mylist.append(n)

print(mylist)

for i in range(len(mylist)):
    for j in range(i+1):
        if mylist[i] < mylist[j]:
            (mylist[i],mylist[j])=(mylist[j],mylist[i])

print(mylist) 

# FIND greatest
# FIND lowest
# FIND middle