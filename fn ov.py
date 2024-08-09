class Studend:
    def sum(self,a,b):
        self.a = a
        self.b = b
    def sum(self,x = None, y = None, z = None ):
        self.x = x
        self.y = y
        self.z = z

        s = 0

        if x!=None and y!=None and z!=None:
            s = x+y+z
        elif x!=None and y!=None:
            s = x+y
        else:
            s = x
        return s
s1 = Studend()
s1.sum(3,4,5)


