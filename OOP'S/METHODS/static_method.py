#STATIC METHODS:(@staticmethod):- methods that donot use the self parameter(work at class level)

#**STATIC METHOD** it is a decorator which allows us to wrap anotherfunction in order to 
# extend the behaviour of the wrapped function,without permanently modifying it.
class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
    @staticmethod   #DECORATOR # we dont need to show "self" in this method
    # def hello(self):
    def hello():
        print("hello")

s1 = Student("ankit",69) 
s1.hello()
print(s1.name)
print(s1.marks)