# set operation method union(), intersection(), difference(), symmetric_difference()

x ={1,2,3,4}
y={2,4,5,6}
print(f"x = {x}")
print(f"y = {y}")

print(x.union(y)) #{1, 2, 3, 4, 5, 6}
print(y.union(x))
print(x | y)

print(x.intersection(y)) #{2, 4}
print(y.intersection(x))
print(x & y)

print(x.difference(y)) #{1, 3}
print(x - y)
print(y.difference(x)) #{5, 6}

print(x.symmetric_difference(y)) #{1, 3, 5, 6}
print(x ^ y)