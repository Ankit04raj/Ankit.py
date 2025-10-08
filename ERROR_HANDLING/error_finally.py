#ERROR_HANDILING:-
a = (input("enter a number:"))
print(f"Multiplication table of {a} is:")

try:
    for i in range(1,11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except:
    print("invalid input")

print("some imp line of code")
print("end of the program")

#CONCEPTS:-
# 1. try block:
# Code that may raise an exception is placed inside the try block.

# 2. except block:
# If an exception occurs in the try block, the control moves to the except block, where you can specify what to do in case of a specific exception.

# 3. else block:
# The else block is executed if no exception occurs in the try block.

# 4. finally block:
# The finally block is always executed, regardless of whether an exception was raised or not. It is useful for cleanup actions (like closing files or network connections).


# Example 1: Handling a division by zero error
try:
    a =10
    b = 0
    result = a/b
except ZeroDivisionError as e:
    print(f"error {e}")
else:
    print(f"result: {result}")
finally:
    print("exception completed.")

# Example with Multiple Exceptions:
n= (input("enter a number:"))
try:
    result = 10/int(n)
except ZeroDivisionError:
    print("cannot divided by zero.")
except ValueError:
    print("invalid input!")
    print("please enter a valid number.")
else:
    print(f"the result is {result}")
finally:
    print("exception completed.")

## UNDERSTANDING OF FINALLY KEYWORD:-(day 37 :- code with harry)
# The finally block is always executed, regardless of whether an exception was raised or not. It is useful for cleanup actions (like closing files or network connections).
def func1():
    try:
        l = [1,3,5,6]
        i = int(input("enter the index:"))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0
    finally:
        print("i am always executed.")

x = func1()
print(x)