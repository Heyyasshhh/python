# TYPES OF ARGUMENTS 

# 1) (*args) --> non keyword argument / non label arguments where we can give nth number arguments

def show(*args):
    print(args)

show('red', True, 5158, 23.38, None)

# --Combination of Non keyword amd positional argument

def students (id, *data):
    print("ID:",id)
    for i in data:
        print(i)
    print()

students(101, "riya", "A+", 90.56, 470)
students(101, "riya", "A")
students(103)


# 2) (**kwargs) --> used to pass keyword arguments

def books (**kwargs):
    print(kwargs)

books(isbn=11, title="Python", author="J.J.Kelly")


# 3) (*args) and (**kwargs)

def products(*args, **kwargs):
    print(args)
    print(kwargs)

products(11, "mobo", category="phone", price=59978797)
