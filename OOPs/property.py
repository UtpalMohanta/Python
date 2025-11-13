class utpal:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math

    @property
    def display(self):
        return str((self.math+self.phy+self.chem)/3) +"%"

s1=utpal(96,97,98)
print(s1.display)

s1.chem=99
print(s1.display)