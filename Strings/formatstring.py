# string format 
name="Rohit"
place="Mumbai"
ans1="My name is",name,"and I am from",place
print(ans1)
print("My name is",name,"and I am from",place)
print("My name is:",name,"and I am from:",place)

# f string 
print(f"My name is:{name} and I am from:{place}")

# %s string format specifier
ans2="My name is %s and I am from %s"%(name,place)
print(ans2)

ans3="My name is %s and I am from %s"%(name,place,"Pune")
print(ans3)

# .format()
ans4="My name is {0} and I am from {1} and {2}".format(name,place,"Pune")
print(ans4)

per = 96.56479542
ans5 =  f"My name  is {name} and I am from {place} and I got {per:0.2f} percentage"