a = 10

def outer():
    # global a
    a = 5
    print("Outer a:",a)

    def inner():
        nonlocal a
        a = 15
        print("inner a:",a)
    
    inner()
    print("Outside inner a:", a)

outer()
print("Outside outer a:",a)