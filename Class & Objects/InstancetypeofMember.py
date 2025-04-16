'''
class Area:
    radius = 4.5

    def __init__(self):
        print("init-1")
    
    def areaofcircle(self):
        return 3.14 * self.radius * self.radius
    
a = Area()
print(a.areaofcircle())
a.__init__()
'''

class Area:
    radius = float(input("Radius: "))

    def __init__(self):
        print("init-1")
    
    def areaofcircle(self):
        return 3.14 * self.radius * self.radius
    
    def __init__(self, a,b):
        self.a = a
        self.b = b
        print("Area of Rectangle:", self.a*self.b)
    
    def square(self, x):
        return x**2

a = Area(10,8)
print("Area of Circle:",a.areaofcircle())
# a.__init__()
print(a.square(5))
print(list(map(a.square,range(1,11))))

# print(dir(Area))

print(a.a,a.b)
a.a = 50
a.b = 90
print(a.a,a.b)
a = Area(a.a, a.b)

Area.a = 78
Area.b = 58
print(a.a,a.b)
print(Area.a, Area.b)
