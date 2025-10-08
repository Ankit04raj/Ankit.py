#METHODS :- Methods are function that belogs to objects

#firstly i am creating a class of student
class Student:
    # now add constructor in the class
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    # METHOD :- now using method function which belongs to object
    def welcome(self):
        print("welcome Ankit")
    
    def get_marks(self):  # this will return the marks of student which belongs to object
        return self.marks
    
#creating object(INSTANCE)
s1 = Student("ankit",98)
s1.welcome()
print(s1.get_marks())