class Girlfriend:
    def gf1(self):
        print("But Sakshi want to proposed by Aryan")

    def gf2(self):
        print("But that girl wants to propsed by sarthak")

class Boyfriend1(Girlfriend):
    def bf1(self):
        print("Sarthak want to propose sakshi")

class Boyfriend2(Girlfriend):
    def bf2(self):
        print("Aryan want to propose some another girl")

b1=Boyfriend1()
b1.bf1()
b1.gf1()
b2=Boyfriend2()
b2.bf2()
b2.gf2()


