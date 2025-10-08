#PRIVATE(LIKE) ATTRIBUTES & METHODS:-
# private attributes & methods are ment to be used only
#withinn the class and are not accessible from outside of the class

#firstlt creating a "account" class
class Account:
    # now define a constructor
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        # but  we have to "private " our account _pass atrbitues
        # so we use (self.__acc_pass) in class to private it
        #& then print it in objecct class ,we found "error" the "acc_pass" will hide
        self.__acc_pass = acc_pass

        #but if we want to unhide it in class then we have to print
        #the acc_pass in class function :- like:-
    def reset_pass(self):
        print(self.__acc_pass)

# now creating an object class of account
acc1 = Account("123578","abcde")

print(acc1.acc_no)
print(acc1.reset_pass()) # it print the acc_pass from class(2nd function)
# print(acc1.__acc_pass)   # it gives an error due to it is hide in class(from 1st function)



#ANOTHER CLASS:-
#if we private any thing in class then it is only accesible by another class function & not from out side the class
class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello person!")
    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome())
# here 2nd"welcome" function of class is accesible & 
# after that 2nd function call the 1st function and then gives 
# # the final output .
