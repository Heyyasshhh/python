colors = ("red", "green", "blue", 59, 90, 23, "white", "red")

# functions
print(colors)
print(len(colors))

x = (21, 25, 89, 75, 26, 35)
print(min(x))
print(max(x))
print(sum(x))
print(sorted(x))

# Operators
print(colors + x)
print(x * 3)
print("red" in colors)
print("Found" if ("red" in colors) else "NotFound")

a = (1, 2, 3)
b = a
c = (1, 2, 3)
print(a is c)

# Methods
print(colors.count(59))
print(colors.count("red"))

print(colors.index("red"))

del colors
print(colors)

