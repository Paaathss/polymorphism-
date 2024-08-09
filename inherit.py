class A:
    def printa(self,num):
        self.num = num
        print('inside class A')

class B(A):
    def printb(self):
        print('inside class B')

obj = B()
obj.printa(3)
obj.printb()


class Person:
    def __init__(self,name):
        name = input('Enter the name')
        self.name = name
    def new(self):
        print(self.name)

class Person2(Person):
    def __init__(self, name,age):
        Person.__init__(self, name)
        age = int(input('Enter your age'))
        self.age = age

    def new1(self):
        print(self.name)
        print(self.age)

obj = Person2('fathima',10)
obj.new1()



class A:
    def printa(self):

        print('inside class A')
class B:
    def printb(self):

        print('inside class B')
class C(A,B):
    def printc(self):

        print('inside class C')
obj = C()
obj.printc()
obj.printb()
obj.printa()
