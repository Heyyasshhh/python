# Empty Class:
'''
class EmptyClass:
    pass
'''

# Class college
'''
class College:
    collegeid=1111
    collegename="Ruparel"
    address="Matunga"
'''

# Accessing data within Class
'''
print(College)
print(College.collegeid, College.address, College.collegename)

col1=College()
print(col1, id(col1))
print(col1.address, col1.collegeid, col1.collegename)
'''

class College:
    collegeid = 1111
    collegename = 'Ruparel'
    address = "Matunga"

    def collegedata(self):
        collegeid=2222
        collegename = "Acharya"
        address = "Chembur"
        print(collegeid,collegename,address)

print(College.collegeid, College.collegename, College.address)
col1 = College()
print(col1.collegeid, col1.collegename, col1.address)

# College.collegedata()
col1.collegedata()

College.address = "Borivali"
print(College.collegeid, College.collegename, College.address)
print(col1.collegeid, col1.collegename, col1.address)

col1.address = "Dadar"
print(College.collegeid, College.collegename, College.address)
print(col1.collegeid, col1.collegename, col1.address)