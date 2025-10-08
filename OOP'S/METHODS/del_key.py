#DEL_KEYWORD :- used to delete object properties or object itself
class Student:
    def __init__(self,name):
        self.name = name
s1 = Student("Ankit")
print(s1.name)
# its print the name before deletation
#& after deletation
del s1.name
print(s1.name) # it shows error