class new:
    def hello(self,s,b):
        self.s = s
        self.b = b
        print(self.s+self.b)
    def hello(self,s,b,c):
        self.s = s
        self.b = b
        self.c = c
        print(self.s+self.b+self.c)
obj1 = new()
obj1.hello(2,3,4)


class new:
    def hello(self,s,b):
        self.s = s
        self.b = b
        print(self.s+self.b)
    def hello(self,s,b,c):
        self.s = s
        self.b = b
        self.c = c
        print(self.s+self.b+self.c)
obj1 = new()
obj1.hello(2,3)

