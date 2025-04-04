x ={1,2,3,4}
y={2,4,5,6}
z={1,2}
p={11,12}
# print(f"x = {x}")
# print(f"y = {y}")

# True for superset
print(x.issuperset(z))
print(x>z)

# True for subset
print(z.issubset(x))
print(z<x)

# True for Null Intersection
print(x.isdisjoint(y))
print(x.isdisjoint(p))

