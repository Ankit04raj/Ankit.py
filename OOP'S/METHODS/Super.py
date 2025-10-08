# it is generaly used in "INHERITANCE"
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