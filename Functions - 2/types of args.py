# TYPES OF ARGUMENTS
name = 'Raj'
rollno = 69

# 1) Positional Arguments

#Example #1
'''
def display(x,y=23):
    print(f"My name is {x}, My roll number is {y}")

display(name)
'''

#Example #2
'''
def display(x="Yo",y): #Problem / Error --> Non-default argument follows default argument
    print(f"My name is {x}, My roll number is {y}")

display(rollno)
'''

#Example #3
'''
def display(x='komal',y=23):
    print(f"My name is {x}, My roll number is {y}")

display() #My name is komal, My roll number is 23
display(name,rollno) #My name is Raj, My roll number is 69
display(rollno) #My name is 69, My roll number is 23
'''

# ------------------------------------------------------------------- #

# 2) Keyword Argument

def getbooks(isbn,title):
    print(f"ISBN: {isbn} Title: {title}")

getbooks(isbn=15987, title= "Python")

# ------------------------------------------------------------------- #

#3) Positional and Keyword Argument

def addition(a,b=5):
    return a+b

print(addition(a=10))
