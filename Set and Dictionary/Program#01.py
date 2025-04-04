#WAP to take number as per count and show sum of then show via loc
count=int(input("Enter count: "))
mylist = {int(input("Enter number: ")) for i in range (count)}

sum=0

for i in mylist:
    sum += i

print("Sum:",sum)