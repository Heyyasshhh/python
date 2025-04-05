numbers = {1:100,2:200,3:300}

# Values()
print(numbers.values())

# GET()
print(numbers.get(2)) #Returns key respective value 
print(numbers.get(200)) # returns none if key is not existing

# KEYS()
print(numbers.keys())

# ITEMS()
print(numbers.items())

# FROMKEYS()
n = [1,3,45,3]
print(n)
n = dict.fromkeys(n,"itv")
print(n)

#SETDEFAULT()
movies={"name":"kgf",'stars':5}
print(movies)

x = movies.setdefault("duraion","2.10mins")
print(movies)

movies.update({"duration":"3hr"})
print(movies)

movies.update({"duration":x})
print(movies)