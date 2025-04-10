str = input("Enter String: ")
str1=str[:1]
str2=str[1:]
final=str1
for i in str2:
    if str1 == i:
        final += "$"
    else:
        final += i
print(final)