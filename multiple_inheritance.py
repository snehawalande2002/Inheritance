class Father:
    def father(self):
        print("I am her Father")

class Mother:
    def mother(self):
        print("i am her Mother")

class Child(Father,Mother):
    def child(self):
        print("I am Sneha..")

c = Child()
c.child()
c.father()
c.mother()
