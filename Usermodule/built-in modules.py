# Random module

import random
print(random.randrange(1,50))
print(random.randrange(1,51,2))
print(random.randint(1,51))
print(random.choice(range(1,51)))

names = ['jeet','rahul','rohit']
print(random.choice(names))
print(random.choices(names,k=2))
print(random.sample(names,k=2))

