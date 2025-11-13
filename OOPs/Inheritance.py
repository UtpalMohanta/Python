#Single Inheritance

class utpal:
    name="I love python"

class Mohanta(utpal):
    def __init__(self,age):
        self.age=age

s1=Mohanta(24)
print(s1.age)
print(s1.name)

#Multi- Level Inheritance

class utpal:
    name="I love python"

class Mohanta(utpal):
    def __init__(self,age):
        self.age=age

    @staticmethod
    def display():
        print("I am a kutta")


class Mohanta1(Mohanta):
    def __init__(self, roll, age):
        super().__init__(age)
        self.roll = roll
        #self.age=age

s1=Mohanta1(24,25)
print(s1.age)
print(s1.roll)
print(s1.name)
print(s1.display())

#Multiple Inheritance

class utpal:
    name="I love python"

class Mohanta:
    def __init__(self,age):
        self.age=age

class Mohanta1(utpal,Mohanta):
    def __init__(self,Id,age):
        self.Id=Id
        super().__init__(age)


s1=Mohanta1(24,25)
print(s1.age)
print(s1.Id)
print(s1.name)
