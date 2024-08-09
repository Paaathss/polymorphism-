class Point:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __add__(self,other):
        a = self.a + other.a
        b = self.b + other.b
           return point(a,b)

p1 = point(7,9)
p2 = point(3,1)
print(p1+p2)
