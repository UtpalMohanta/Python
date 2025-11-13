class student:

    @staticmethod
    def display(name,marks):

        sum=0
        for val in marks:
            sum+=val
            avg=sum/len(marks)
        print("HI", name, "your score is:", avg)


s1=student()
s1.display("utpal",[25,26,27])
