# Updating and adding data without methods in Dictionary
"""
books = {}
print(books)

books["isbn"] = 1111 #Adds the key value pair to dictionary
print(books)

books["isbn"] = 5555 #Updates the value to existing key if the give key is the same
print(books)

books["title"]="python"
print(books)

books["author"]="rossom","smith"
print(books)

books['price','quantity']=800,5
print(books)

print()

books = dict(publisher='techneo', dop="12-02-2004")
print("Books:",books)
"""


# Deleting without methods in Dictionary
"""
del books['dop']
print(books)

# del books["title"]  # Key Error
# print(books)

del books
# print(books)
"""


# Methods

# UPDATE() method
'''
students = {}
print(students)

students.update({"sid": 101})
students.update({"sid": 101, "sid": 201})
students.update({"name": "pooja", "grade": "A+"})
students.update({"subjects": ["py", "js", "sql"]})
print(students)

students["sid"] = 101
print(students)

students.update({"city":"mumbai"})
print(students)
'''

#POP(), POPITEM()
'''
students.pop('city')
print(students)

students.popitem()
print(students)

del students
# print(students) #NameError student is not defined 
'''

# copy()
numbers = {1:100,2:200,3:300}
print(numbers)
x = numbers.copy()
print(x)