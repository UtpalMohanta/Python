class utpal:
    name="Mohanta"

    #defult constructor
    def __init__(self):
        print("Very easy language python.")
s1=utpal()
print(s1.name)


class utpal:

    #parameterized constructor
    def __init__(self,fullname):
        self.name=fullname
        print("Very easy language python.")
s1=utpal("jaton")
print(s1.name)

s1=utpal("Bithi")
print(s1.name)


class utpal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Very easy language python.")
s1=utpal("jaton",97)
print(s1.name,s1.age)

s1=utpal("Bithi",98)
print(s1.name,s1.age)


#AK sathe
class utpal:

    #defult constructor
    def __init__(self):
        print("Very easy language python.")

    #parameterized constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Very easy language python.")
s1=utpal("jaton",97)
print(s1.name,s1.age)

s1=utpal("Bithi",98)
print(s1.name,s1.age)