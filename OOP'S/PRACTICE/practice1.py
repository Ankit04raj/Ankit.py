# Q<*>  CREAT STUDENT CLASS THAT TAKES NAME & MARKS OF 3 SUBJECT
#          AS ARGUMENT IN CONSTRUCTOR. THEN CREAT A METHOD TO PRINT THE AVERAGE.

class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi",self.name,"your avg is:",sum/3)

s1 = Student("ankit",[98,92,89])
s1.get_avg()

# we  can change the name by mutable method
s1.name = "Ankit Raj"
s1.get_avg()