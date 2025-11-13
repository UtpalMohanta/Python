class utpal:
    name="I love python"

class Mohanta(utpal):
    def __init__(self,age):
        self.age=age

class Mohanta1(Mohanta):
    def __init__(self, roll, age):
        super().__init__(age)
        self.roll = roll
        #self.age=age

s1=Mohanta1(24,25)
print(s1.age)
print(s1.roll)
print(s1.name)