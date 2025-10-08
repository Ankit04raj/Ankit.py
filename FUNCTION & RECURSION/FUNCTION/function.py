# ADDITION BY FUNCTION METHOD
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
def calculate_sum(a,b):
    sum = a + b
    print(sum)
    return sum
calculate_sum(a,b)
calculate_sum(3,9)
calculate_sum(4,7)

# PRINT_HELLO
def print_hello():  # undefined function
    print("hello")
print_hello()
print_hello()
print_hello()

# IF ANY FUNCTION HAS NO VALUE AND WE PRINT AS A
#  RESULT THEN ITS RETURN "NONE" VALUE
def print_hello():
    print("hello")
result = print_hello()
print(result)  # NONE

# average of 3 numbers 
def calc_avg(a,b,c):
    # if (a == 0)
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg
calc_avg(56,45,98)

#ARGUMENT(DEFAULT PARAMETER)
def calc_product(a=9,b=6):
    print(a*b)
    return a*b
calc_product(9,6)
# we can change the value of (a,b)
calc_product(7)   #  a=7  b = 6
calc_product(2,4)  # a = 2 b = 4


#GREATEST OF 2
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))

def is_greater(a,b):
    if(a>b):
        print("the first number is greater.")
    else:
        print("the second number is greater or equal")
def is_lesser(a,b):
    pass  # pass contunue the program 

is_greater(a,b)