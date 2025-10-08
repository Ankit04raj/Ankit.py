#POLYMORPHISM :- OPERATOR OVERLOADING
#when the same operator is allowed to have different meaning according to the context

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def shownumber(self):
        print(self.real,"i +",self.img,"j")

    # NOW we want to add both complex number
    def __add__(self, num2):   # __add__(dunder function)
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

    # NOW we want to sub both complex number
    def __sub__(self, num2):   # __add__(dunder function)
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)

num1 = Complex(1, 3)
num1.shownumber() 

num2 = Complex(4, 6)
num2.shownumber() 

# num3 = num1.add(num2)
# num3.shownumber() 

num3 = num1 + num2  #  its work due to dunder function(line13)
num3.shownumber() 

num3 = num1 - num2 
num3.shownumber() 


# OPERATOR OVERLAPING (of vector)
class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,x):
        return Vector(self.i + x.i,self.j+x.j,self.k +x.k)
    

v1 = Vector(3,5,6)
print(v1)

v2 = Vector(1,2,4)
print(v2)

print(v1+v2)
print(type(v1+v2))