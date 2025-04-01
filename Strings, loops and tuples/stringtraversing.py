msg="Welcome"

# Traversing string using oor loops
'''
for i in msg:
    print(i,end="")

OUTPUT: Welcome
'''

# To print indexing with characters of string 
# Using For Loop
'''
for i in range(len(msg)):
    print(i,msg[i])
'''

# Using While Loop
'''
i=0
while i < len(msg):
    print(i,msg[i])
    i+=1
'''

'''
OUTPUT:
0 W
1 e
2 l
3 c
4 o
5 m
6 e
'''

#WAP to traverse every second character of any string entered by user
'''
str=input("String: ")
for i in range(0,len(str),2):
    print(str[i], end="")

for i in str[0::2]:
    print(i,end="")
'''

#WAP to print number of occurance of entered character/word from any string
# For Char
'''
str=input("String: ")
count=0
for i in str[0::1]:
    if char==i:
        count=count+1
if count==0:
    print("Not Found")
else:
    print("Number of Occurances:",count)
'''

# For Word

'''
str=input("String: ")
word=input("Character To Search: ")
count=0
charcheck=""
for i in range(len(str)):
    k=i
    for j in range(len(word)):
        try:
            charcheck += str[k]
            k+=1
        except:
            None
    if charcheck == word:
        count+=1
    charcheck=""

(
    print(f"'{word}' present in '{str}' for {count} time")
    if count !=0
    else print(f"'{word}' is not present in '{str}'")
)
'''

#WAP to show index position of entered character
'''
str=input("String: ")
word=input("Character To Search: ")
find=""

for i in range(len(str)):
    if word == str[i]:
        indexnum=i
        find=f"{indexnum}"

if find=="":
    print("Not Found")
else:
    print(f"{word} in {str} at position {find}")
'''

#WAP to reverse a string
str=input("String: ")

#By slicing method
'''
for i in str[::-1]:
    print(i, end="")
'''
'''
for i in reversed(str):
    print(i, end="")
'''
'''
revstr=""
for i in str:
    revstr = i + revstr
print(revstr)
'''
'''
for i in range(len(str)-1,-1,-1):
    print(str[i],end="")
'''