x = "Python"
print(x)
print(x[0])
print(x[1])
print(x[2])

print(x, id(x))

y = "Python"
print(y, id(y))


# Modifying Strings
# Using .replace() method
print(x.replace("Py","j"))
print(y.replace("th","s"))


# Using Slicing method
x= "k" + x[1:]
print(x, id(x))