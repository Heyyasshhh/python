names1=['amir','bear','charlton','daman']
names2= names1
names3= names1[:]
names2[0]='Alice'
names3[1]='Bob'
sum = 0
for ls in (names1,names2,names3):
    if ls[0]=='Alice':
        sum+=1
    if ls[1] == 'Bob':
        sum+=10

print(sum)

print(names1,id(names1))
print(names2,id(names2))
print(names3,id(names3))