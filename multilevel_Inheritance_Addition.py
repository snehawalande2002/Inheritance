class Cse:
    def read(self,a):
        self.a=a

class Dept(Cse):
    def read2(self,b):
        self.b=b

class College(Dept):
    def read3(self,a,b):

        c= a+b
        print(c)

co=College()
co.read3(10,20)
