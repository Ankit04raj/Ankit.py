#CLASS_METHOD:- (@classmethod) : a class method is bound to the class & 
#            receives the class as an implicit first argument

# NOTE* :- @staticmethod canot access or modify class state & generaly for utility
class Person:
    name = "anonymous"

    # def changeName(self,name):
    #     self.name = name
    #     # Person.name = name  # it directly change and print the new given name in object class "OR"
    #     self.__class__.name = "ankit raj"

    @classmethod  #DECORATOR # it directly change(modify) the "person class"
    def changeName(cls,name):
        cls.name = name

p1 = Person()
p1.changeName("Ankit raj")
print(p1.name) 
print(Person.name)


#CLASS METHOD AS ALTERNATIVE CONSTRUCTORS:-
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])
    
e1 = Employee("Ankit",120000)
print(e1.name)
print(e1.salary)

string = "Harry -1200000"
e2 = Employee.fromstr(string)
print(e2.name)
print(e2.salary)