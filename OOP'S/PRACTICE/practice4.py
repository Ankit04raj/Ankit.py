#4q>define a employee class with attributes role,department & salary.this 
#class also a showdetails()method
#     create an Engineer class that inherities from empolyee & has
# additional attributes : name & age

class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =",self.role)
        print("dept =",self.dept)
        print("salary =",self.salary)

#2nd part creating an engineer class
class Engineer(Employee):
    def __init__(self,name , age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","80,000")

# e1 = Employee("accountant","finance","60,000")
# e1.showDetails()

engg1 = Engineer("ankit",21)
engg1.showDetails()