class utpal:
    name="matha_kharap"

    @classmethod
    def changeName(cls,name):
        cls.name=name

p1=utpal()
p1.changeName("utpal mohanta")
print(p1.name)
print(utpal.name)