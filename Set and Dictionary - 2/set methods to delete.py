# POP(), REMOVE(), DISCARD()
x = {1,2}

x.update({6,7,8,11,10})
print(x)

#1) POP()
'''
x.pop()
print(x)

x.pop()
print(x)
'''

#2) REMOVE()
'''
x.remove(10)
print(x) 
'''

#3) DISCARD()
'''
x.discard(100)
print(x)

x.discard(11)
print(x)
'''

#CLEAR
'''
x.clear()
print(x)
'''

#DEL
'''
del x
print(x)
'''