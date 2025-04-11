import functools

#sum of numbers from 1 to 10

def sum(x,y):
    return x+y

print(sum(15,78))
print(functools.reduce(sum, range(1,11)))

print(functools.reduce(lambda x,y:x+y,[1,2,3,4,5]))