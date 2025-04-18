from datetime import datetime
class Emp:
    officename = "Tata"
    def __init__(self, eid): #Instance Method
        self.eid = eid

    def setdetails(self, name, jobprofile): #Local Method
        self.name = name
        self.jobprofile = jobprofile
        # doj = datetime.now().date()
        self.doj = datetime.now().date()

    def getdetails(self): #Local Method
        print(f"Object: {self.officename} {self.eid} {self.name} {self.jobprofile} {self.doj}")
        print(f"Class:  {Emp.officename} {self.eid} {self.name} {self.jobprofile}")

    @classmethod #Buit-in Decorator
    def setofficename(cls):
        cls.officename = "TCS"

    @staticmethod #Buit-in Decorator
    def getsalary(salary):
        print("Salary: {salary}")

e = Emp(101)
e.setdetails("Rahul", "Software Engineer")
e.getdetails()

e.setofficename()
e.setdetails("Rahul", "Software Engineer")
e.getdetails()

e1 = Emp(102)
Emp.setofficename
e1.setdetails("Raj", "Data Analyst")
e1.getdetails()

Emp.setofficename

e1.getsalary(80000000)
Emp.getsalary(78965200)