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



class A:
    def printa(self):
        print('inside class A')

class B(A):
    def printb(self):
        print('inside class B')

class C(B):
    def printc(self):
        print('inside class C')

obj = C()
obj.printa()
obj.printb()
obj.printb()

