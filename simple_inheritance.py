class Neha:
    def hi(self):
        print("It's me Sneha")
n=Neha()


class Sneha(Neha):
    def hello(self):
        print("Sur name is Walande")
s= Sneha()
s.hi()         # Calling another class method using recent class object