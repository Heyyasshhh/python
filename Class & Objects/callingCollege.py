'''
import classdemo

print(classdemo.College.address)
print(classdemo.col1.address)
'''

# OR


from classdemo import College, col1

print(College.address)
print(col1.address)


from classdemo import College as c, col1 as c1

print(c.address)
print(c1.address)
c1.collegedata()