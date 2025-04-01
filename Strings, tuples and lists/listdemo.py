mylist=[]
print(mylist,type(mylist))

mylist=list()
print(mylist,type(mylist))

mylist=["hello"]
print(mylist,type(mylist))

mylist=list("hello")
print(mylist,type(mylist))

#WAP to show index of elemnts which is entered by user from below list 
colors=["red", "green", "blue","white","black","red","pink"]
element = input("Element to check index number: ")
flag=False
index=[]

for i in range(len(colors)):
    if colors[i] == element:
        index.append(i)
        flag = True

if flag:
    print(f'{element} found and index position: {index}')
else:
    print(f'{element} not found.')