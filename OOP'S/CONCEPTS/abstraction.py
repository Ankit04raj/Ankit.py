#ABSTRACTION:- hidding the implimentation detail of a class
#             and only showing the essential features to the user.

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")

car1 = Car()
car1.start()

# the whole working process under the class will hide 
# and the final argument is passed which is true then the 
# car started .
#  the all hidden argument are hidden by the "ABSTRACTOR"
# AS  like this # abstractor # works 