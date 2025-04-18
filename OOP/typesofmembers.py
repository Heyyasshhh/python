class Student:
    sid=1111 #Class Member

    def __init__(self,name,totalmarks):
        self.name = name # Instance Member
        self.totalmarks = totalmarks #Instance Member
        self.__mobile = 78995421 #Static Member
    
    def data(self,per):  
        address = "Mumbai" #Local Member
        __country = "India"
        print(f"Name: {self.name}")
        print(f"Total Marks: {self.totalmarks}")
        print(f"Percentage: {per}%")
        print(f"Address: {address}")
        print(f"Mobile Number: {self.__mobile}")
        print(f"Country: {__country}")

s = Student("Zampy", 500)
s.data(s.totalmarks/5)
print(s.name, s.totalmarks)