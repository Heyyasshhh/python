class TypeOfMembers:
    id = 1111 # Class Member

    def getid(self,x):
        id = x # Local Member
        print("Id:",id)

print("Accessing Member/Attributes")
t = TypeOfMembers()
print("ID:",TypeOfMembers.id)
print("ID:",t.id)
print()

print("Accessing Local Member")
t.getid(8989)
print()

print("Updating Data of Members / Attributes using Class")
TypeOfMembers.id = 5555
print("ID:",TypeOfMembers.id)
print("ID:",t.id)
print()

print("Updating Data of Members / Attributes using Object")
t.id = 9999
print("ID:",TypeOfMembers.id)
print("ID:",t.id)
print()
