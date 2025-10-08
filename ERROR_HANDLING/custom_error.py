##Raising Exceptions: You can also manually raise exceptions using the raise keyword.
#rise error stop the program forther after any type of error
#EXAMPLE 1>:-
a  = int(input("enter the value between 5 and 9:-"))

if (a<5 or a>9):
    raise ValueError("value should be in between 5 and 9.")

#EXAMPLE 2>:-
def divide(a, b):
    if b == 0:
        raise ValueError("The denominator cannot be zero!")
    return a / b

try:
    print(divide(10, 0))
except ValueError as e:
    print(e)