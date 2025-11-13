class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        toxic=self.name
        sum=0
        for val in self.marks:
            sum+=val
            avg=sum/len(self.marks)
        print("HI", toxic, "your score is:", avg)


s1=student("utpal",[25,26,27])
s1.display()
