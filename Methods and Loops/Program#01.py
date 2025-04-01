# WAP to find enter elements and replace elements as per asked new element
# NOTE: Create list from user

mylist = []
count = int(input("Enter count: "))

for i in range(count):
    n = input(f"Enter {i+1} element: ")
    mylist.append(n)

print(mylist)

find = input("Find: ")
flag = False
for i in range(len(mylist)):
    if find == mylist[i]:
        flag = True
        print(f"{find} found!")
        replace = input(f"Replace {find} wih: ")
        mylist[i] = replace

if flag == False:
    print("Element Not Found")
else:
    print("Updated List:",mylist)
