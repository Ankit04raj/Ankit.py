# GETTERS AND SETTERS :-
#@PROPERTY:-
class Student:
    def __init__(self,phy,che,math):
        self.phy = phy
        self.che = che
        self.math = math

    #PROPERTY is used as "getter"
    @property  # DECORATOR
    def percentage(self):
        return str((self.phy + self.che +self.math) /3) + "%"

    # # for "SETTER"
    # @percentage.setter
    # def percentage(self,final_percentage):
    #     self._percentage = final_percentage
    #     return str((self.phy + self.che +self.math) /3) + "%"
#  *********setter is not clear properly************ #  CONCEPT"ERROR"
stu1 = Student(98,97,99)
print(stu1.percentage)
stu1.phy = 86
print(stu1.phy)
print(stu1.percentage)



# OTHER EXAMPLE:-
class Myclass:
    def __init__(self,value):
        self._value = value
    
    def show(self):
        print(f"value is {self._value}")

    #PROPERTY is used as "getter"
    @property
    def ten_value(self):
        return 10* self._value
    
        # # for "SETTER"
    @ten_value.setter
    def ten_value(self,new_value):
        self._value = new_value/10

obj = Myclass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()