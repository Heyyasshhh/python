#1) WAP to show entered string without vowels 
'''
str=input("String: ")
newstr=""
for i in str:
    if i not in "aeiou":
        newstr+=i

print(newstr)
'''


#2) WAP to show vowels and count from entered string 
'''
str=input("String: ")
vowels=""
count = 0
for i in str:
    if i.lower() in "aeiou":
        vowels += i
        count += 1

print("Vowels:", vowels)
print("Number of Vowels:", count)
'''

#3) WAP to show vowels and consonent seperately with total count from entered string
'''
str=input("String: ")
vowels=""
consonants=""
count_vowels=0
count_consonants=0

for i in str:
    if i.lower() in "aeiou":
        vowels += i
        count_vowels+=1
    else:
        consonants += i
        count_consonants += 1

print("Vowels:",vowels)
print("Number of Vowels:",count_vowels)
print("Consonants:",consonants)
print("Number of Consonants",count_consonants)
print(f"Total Alphabets in {str}: {count_consonants+count_vowels}")
'''

#4) WAP to find and replace a character in string
str=input("Enter the String: ")
find=input("Find: ")
newstr=""
flag=False
for i in str:
    if i==find:
        if flag == False:
            print(f"{find} found in {str}")
            replace=input("Replace: ")
            flag=True
        newstr+=replace
    else:
        newstr+=i


print(newstr)

#HOMEWORK
#Customization in Q4)