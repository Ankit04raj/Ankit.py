#INHERITANCE:-
            # WHEN one class(child/derived) derives the properties & method of another class(parent/base)
# there are 3 types of inheritance
#1> single inheritance:-
class Car:
    color = "orange"
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class toyotacar(Car):  # this is a child class 
    #& after giving it(Car)"parent class" the perant class behaviour is present in child_class
    def __init__(self,name):
        self.name = name

#creating object class
car1 =toyotacar("fortuner")
car2 = toyotacar("prius")

print(car1.name)
print(car1.stop())
print(car1.color)

#2> multi- level inheritance:-
class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stopped.")

class toyoyacar(Car):  # this is a child class 
    #& after giving it(Car)"parent class" the perant class behaviour is present in child_class
    def __init__(self,brand):
        self.brand = brand

class Fortuner(toyoyacar): # this toyata function property cintains car property to which now contain in fortuner this is caled multi_level
    def __init__(self, type):
        self.type = type

car3 = Fortuner("diesel")
car1.start()


#3>Multiple inheritance:-
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA) 


#********SUPER_METHOD:-************
#super-method:- super()method is used to access methods of the parent class
class Car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("car started!..")
    @staticmethod
    def stop():
        print("car stop...")

class Toyotacar(Car):
    def __init__(self, name,type):
        super().__init__(type)
        super().start()
        self.name = name

car1 = Toyotacar("prius","electric")
print(car1.type)