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

id = input("Enter Id: ")
name = input("Enter Name: ")
degree = input("Enter Degree: ")
s = Student(id,name,degree)
s.show()
