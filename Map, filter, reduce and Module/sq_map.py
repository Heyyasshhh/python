#WAP to find square of 1 to 10 numbers

# without lambda
def square(x):
    return x**2
print(list(map(square, range(1,11))))

# With list comprehension
print([i**2 for i in range(1,11)])

# With Lambda 
print(list(map(lambda x: x**2, range(1,11))))

