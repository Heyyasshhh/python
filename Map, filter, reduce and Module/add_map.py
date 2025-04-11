def addition(a,b):
    return a+b

print(list(map(addition, (4,5),(5,6))))
print(list(map(addition, range(1,6),range(5,8))))
print(list(map(addition, [15,189,789],[259,357,159])))
print(list(map(addition, ("kiwi-","mango-"),("100","1200"))))


animals = ["cat", "dog", "tiger"]
print(tuple(map(list, animals)))