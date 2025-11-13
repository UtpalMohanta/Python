class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("I am a krishna devotee")

    def display(self):
        return self.name

    def display1(self):
        return self.age


s1=student("utpal",25)        #function===Method
print(s1.display())
print(s1.display1())