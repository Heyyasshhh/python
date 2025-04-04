# WAP to take number from user and add into list and show even and odd numbers seperately
count = int(input("Count of number: "))
mylist = [int(input(f"Enter {i+1} number: ")) for i in range(count)]
print(mylist)
odd = []
even = []
[even.append(i) if i % 2 == 0 else odd.append(i) for i in mylist]
print(f"Even Numbers: {even}")
print(f"Odd Numbers: {odd}")