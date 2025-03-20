'''
s=""
print(s,type(s))

msg= str()
print(msg,type(msg))

s="a"
print(s,type(s))

s1="python is easy"
print(s1,type(s1))

s2="1598753642"
print(s2, type(s2))

# features = '''#Dynamic
# easy
# case-sensitive
'''
print(features,type(features))

name=input("Enter you name: ")
print(name,type(name))

per = str(58.9634)
print(per, type(per))
'''


#Accessing string elements via Index
'''
Types of Index: 
    1) Positive: Starts with 0 Left to Right
    2) Negative: Starts with -1 Right to Left 
'''

msg="Welcome"

# Positive Index
'''
print(f"First Character of {msg}: {msg[0]}")
print(f"Second Character of {msg}: {msg[1]}")

print(f"Length of {msg}: {len(msg)}")
print(f"Middle character of {msg}: {msg[len(msg)//2]}")

print(f"Second last character of {msg}: {msg[len(msg)-2]}")
'''

# Negative Index

print(f"First Character of {msg}: {msg[-len(msg)]}")
print(f"Second Character of {msg}: {msg[-len(msg)+1]}")

print(f"Length of {msg}: {-len(msg)}")
print(f"Middle character of {msg}: {msg[-len(msg)//2]}")

print(f"Last character of {msg}: {msg[-1]}")
print(f"Second last character of {msg}: {msg[-2]}")
