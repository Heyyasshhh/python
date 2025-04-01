print("METHODS IN PYTHON")
'''
a = "java"
b = "python"
print(a, b)
a += b
print(a)
'''

s="welcome to python"

# COUNT() method
'''
s="welcome to python"
print("-------COUNT-------")
print(len(s))
print(s.count("o"))
print(s.count(""))

s1=""
print(s1.count(""))

print(s.count("om"))
print(s.count("jkjkj"))
print(s.count("o",4,12))
'''

#FIND() method
'''
print("-------FIND-------")
print(s.find("o"))
print(s.find(""))
print(s.find("w"))
print(s.find("om"))
print(s.find("ot"))
print(s.find("j"))

print(s.find("o",4,12))
'''

# INDEX() method
'''
print("-------INDEX-------")
print(s.index("o"))
print(s.index(""))
print(s.index("w"))
print(s.index("om"))
# print(s.index("ot")) #ValueError
# print(s.index("j")) #ValueError
'''

# REPLACE() method
'''
print("-------REPLACE-------")
print(s.replace("o","z"))
print(s)
print(s.replace("o","z",1))
print(s.replace("q","z",1))
print(s.replace("","z"))
'''

# JOIN() method
'''
print("-------JOIN-------")
print(s.join("JAVA"))
print("x".join(s))
print(" ".join(s))

str = "ceadb"
print(str)
print(sorted(str))
print("".join(sorted(str)))
'''

# SPLIT() method
'''
print("-------SPLIT-------")
print(s.split())
print(s.split(" ",0))

s1="python,java,html,sql,css"
print(s1.split())
print(s1.split(",",4))
'''

# SPLITLINES() method 
'''
print("-------SPLITLINES-------")
s3="hi\nhow are you?\nwhat is your name?"
print(s3.split())
print(s3.splitlines())
'''

# ZFILL() method
'''
print("-------ZFILL-------")
print(s.zfill(30))
'''

# STRIP() method
print("-------STRIP-------")
z="                   masjdhg dsf      "
print(z)
print(z.strip())