class Person:
    def __init__(self):
        self.id = id

    def show(self):
        print(f"Person Id: {self.id}")

class Student(Person):
    def __init__(self,id,name, degree):
        # super().__init__(id)
        self.id = id
        self.name = name
        self.degree = degree

    def show(self):
        print("Person as Student")
        print(f"ID: {self.id}, Name: {self.name}, Degree: {self.degree}")

class Emp(Student):
    def __init__(self,id,name,degree,jobprofile,salary):
        super().__init__(id,name,degree)
        self.jobprofile = jobprofile
        self.salary = salary

    def show(self):
        print("Person as Employee")
        print(f"ID: {self.id}, Name: {self.name}, Degree: {self.degree}, Job Profile: {self.jobprofile}, Salary: {self.salary}")

id = input("Enter Id: ")
name = input("Enter Name: ")
degree = input("Enter Degree: ")
jobprofile = input("Enter Job Profile: ")
salary = float(input("Enter Salary: "))

s = Student(id,name,degree)
e = Emp(id,name,degree,jobprofile,salary)

print("---------------------------------------")
s.show()
print("---------------------------------------")
e.show()
