# empty function
def display():
    pass

display()


#Example 1 (without parameter, without return statement)
def printstr():
    print("Hello world!")

printstr()


# Function without return
def show():
    print("Welcome with print")

show()


# Function with return
def show():
    return("Welcome with return")

print(show())


# Examples
def show():
    s = 56
    return 56 ** 3

print(show())
ans = 190 + show()
print()


def addition():
    a = 6
    b = 7
    print(a+b)
    return a-b

print(addition())


def validate():
    n = int(input("Enter Number: "))
    if n>500:
        print(n,"is greater than 500")
        return
    else:
        return
    
validate()


def division():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    if b == 0:
        print("Cannot Divide by zero")
        return
    else:
        print("Division:",a/b)

division()