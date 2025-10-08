#CONSTRUCTOR  OR "__init__" FUNCTION
# all classes havee a function called __init__(), which 
# is always executed when the class/object is begin initiated

#CREATING A CLASS:
class Student:
    # CREATING A CONSTRUCTOR: 
    def __init__(self,name):
        self.name = name
        # print(self)
        print("adding new student in database.")

# CREATING OBJECT(instance)
s1 = Student("Ankit")
print(s1.name)   
# CONSTRUCTOR CALLED EACH TIME WITH NEW OBJECT INSERTION
s2  = Student("rishi")
print(s2.name)

# IF THERE Is ONLY ONE INPUT "__init__(self)" then
# this  is called default constructors

# we can add multiple value 
#which is known as parameterized constructors:-
class Student:
    # CREATING A CONSTRUCTOR: 
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        # print(self)
        print("adding new student info in database.")

# CREATING OBJECT(instance)
s1 = Student("Ankit",97)
print(s1.name,s1.marks)   
# CONSTRUCTOR CALLED EACH TIME WITH NEW OBJECT INSERTION
s2  = Student("rishi",89)
print(s2.name,s2.marks)
