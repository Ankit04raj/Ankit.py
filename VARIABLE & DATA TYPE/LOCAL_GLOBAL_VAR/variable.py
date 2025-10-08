# LOCAL VS GLOBAL VARIABLR
x = 4
print(x)  # 1st output

def hello():
    x =5
    print(f"the local x is {x}")    # 2nd output
    print("hello ankit")     # 4th output
print(f"the global x is {x}")   # 2nd  output
hello()
x = 5   #  this is able to change the global x
print(f"the global x is {x}")   # 5th output


#  OTHER EXAMPLE:-
X = 10    # global variable

def my_function():
    global X   # it change the previous global value in a function of any type of value global or local
    x = 4
    y = 5   # local variable
    print(y)

my_function()
print(x)
#print(y)  #  this will cause an error because y is a
#local variable and is not accessible of the function