'''
a = 10

def outer():
    a = 5
    print("Outer a:",a)

    def inner():
        a = 15
        print("inner a:",a)
    
    inner()
    print("Outside inner a:", a)

outer()
print("Outside outer a:",a)
'''

# Local Variable --> Global Variable
a = 10

def outer():
    # global a
    a = 5
    print("Outer a:",a)

    def inner():
        global a
        a = 15
        print("inner a:",a)
    
    inner()
    print("Outside inner a:", a)

outer()
print("Outside outer a:",a)