class College:
    def __init__(self, collegename, degree):
        self.collegename = collegename
        self.degree = degree

class Institute:
    def __init__(self, institutename, courses):
        self.institutename = institutename
        self.courses = courses

class Student(College,Institute):
    def __init__(self, collegename, degree, institutename, courses,sname,per):
        self.collegename = collegename
        self.degree = degree
        self.institutename = institutename
        self.courses = courses
        self.sname = sname
        self.per = per

    def show(self):
        print(f"{self.sname} {self.per}")
        print(f"{self.collegename} {self.degree}")
        print(f"{self.institutename} {self.courses}")

s = Student("Aacharaya", "MCA", "ITV", "FSD", "Rahul", 90)
s.show()