class utpal:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def display(self):
        print(self.__age)
s1=utpal("utpal",24)
print(s1.name)
#print(s1.__age)#not run this code
print(s1.display())


class utpal:

    def __display(self):
        print("I am utpal")

    def display1(self):
        print(self.__display())
        
s1=utpal( )
print(s1.display1())



