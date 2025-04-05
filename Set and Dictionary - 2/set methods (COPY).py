# Copy Method
x = {1,2}
y = {4,5}

print(x, id(x)) #1839086764768
print(y, id(y)) #1839087048896

z=x.copy() 
print(z,id(z)) #1839087048448 Different ID's 

m = x
print(m,id(m)) #1839086764768 Same ID's

y=x.copy()
print(y, id(y)) #1931644263712

print(m==x) #True
print(m is x) #True

print(z==x) #True
print(z is x) #False