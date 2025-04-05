# FROZEN SET 
colors = {"red"}
print(colors, type(colors), id(colors))

colors.add("green")
print(colors,type(colors), id(colors))

colors=frozenset(colors)
print(colors,type(colors), id(colors))

# colors.add("blue")
# print(colors,type(colors), id(colors))

