students=(11,"raj","A+","Mumbai",989756)
'''
for i in students:
    print(i)

i=0
while i < len(students):
    print(i, students[i])
    i += 1
'''

#WAP to count elements which is entered by user from below tuple 
colors=("red", "green", "blue","white","black","red","pink")
str=input("Enter color: ")
count=0
for i in colors:
    if i == str:
        count+=1
    
if count > 0:
    print(f'{str} found in colors')
else:
    print(f'{str} not found in colors')

print(f'{count} results found')