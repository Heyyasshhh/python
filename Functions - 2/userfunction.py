
name = input("Enter Name: ")
rollno = int(input("Enter Roll Number: "))

# 1) Default Function (Without parameters and without return type)
'''
def display():
    print(f"My name is {name} and my Roll Number is {rollno}")

display()
'''

# 2) Function with Parameters and without Return type
'''
def display(x,y):
    print(f"My name is {x} and my Roll Number is {y}")

display(name,rollno)
'''

# 3) Function without Parameters but with Return type
'''
def display():
    return f"My name is {name} and my Roll Number is {rollno}"

print(display())
'''

# 4) Function with Parameters and with Return type 
'''
def display(x,y):
    return f"My name is {x} and my Roll Number is {y}"

print(display(name,rollno))
'''