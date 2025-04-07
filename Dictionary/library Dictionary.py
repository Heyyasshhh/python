# WAP to create library dictionary and add isbn, title, auuthor and price from user as per count entered
count=int(input("Enter Count: "))
lib={}
for i in range(count):
    isbn=int(input("Enter isbn: "))
    title=input("Enter Title: ")
    author=input("Enter Author: ")
    price=float(input("Enter Price: "))
    lib.update({isbn:{"Title":title,"Author":author,"Price":price}})

for k,v in lib.items():
    print(k, end=" ")
    for val in v.values():
        print(val, end=" ")
    print()