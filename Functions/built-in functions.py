# BUILT-IN Functions

# print(help(list))
print(bin(12))
print(hex(12))
print(oct(12))
print(pow(12,2))
print(round(12.89))
print(divmod(12,5))

print("-------------------------------------------")
print("-------------------------------------------")

#zip() -> packing data into one element

names = ["raj", 'pooja', 'komal']
grades = ['A','O','B']
per = [89,90, None]

print(list(zip(names,grades)))
print(list(zip(names,grades,per)))

print("-------------------------------------------")

for i in names, grades, per:
    print(i)

print("-------------------------------------------")

print(list(zip(names,grades,per)))
print(set(zip(names,grades,per)))
print(tuple(zip(names,grades,per)))
print(dict(zip(names,grades)))

print("-------------------------------------------")
print("-------------------------------------------")


#zip(*var) -> unzipping a variable
students = [('raj', 'A', 89), ('pooja', 'O', 90), ('komal', 'B', None)]

print(list(zip(*students)))
print(tuple(zip(*students)))
print(set(zip(*students)))
# print(dict(zip(*students)))


print("-------------------------------------------")
print("-------------------------------------------")

# slice()
colors = ["red","green","blue","white","black","brown"]
ans = slice(2,4)
print(colors[ans])
print(colors[2:4])


print("-------------------------------------------")
print("-------------------------------------------")

# enumrate()
vowels = {"a","e","i","o","u"}
print(vowels)
print(list(enumerate(vowels)))
print(set(enumerate(vowels)))
print(tuple(enumerate(vowels)))
print(dict(enumerate(vowels)))


print("-------------------------------------------")
print("-------------------------------------------")

# iter()
colors = ["red","green","blue"]
print(colors)
newcolors = iter(colors)
first = next(newcolors)
print(first)
second = next(newcolors)
print(second)
third = next(newcolors)
print(third)