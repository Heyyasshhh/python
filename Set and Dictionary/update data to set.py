colors = {"red", "green"}
colors.update({800})
print(colors)

x = {34,56,67}
x.update(colors)
print(x)

colors.update({"blue","white"})
print(colors)

colors.update((("blue","grey")))
print(colors)