# ARITHMETIC OPERATION 
a = float(input("enter the first number:"))
b = float(input("enter the second number:"))
# a =4 
# b =2
print(a+b)  # sum
print(a-b)  # substract
print(a*b)  # multiply
print(a/b)  # division
print(a//b)  # take only intiger value
print(a % b) #remainder
print(a**b)  # a  power b


#RELATIONAL/COMPARISION OPERATOR
x = 45
y =20
print(x==y)
print(x != y)
print(x >= y)
print(x > b)
print(x<=y)
print(x<y)


# ASSIGNMENT OPERATOR

# IF WE TAKE EVERY TIME NUM FOR EVERY OPERATION then 
#we got the another one output
num = 10
num += 10
print("num",num)
num = 10
num -= 10
print("num",num)
num =10
num **= 10
print("num",num)

# for only one num is taken first operation output acts
#like second operation num and its continue forther...
num = 10
num += 10
print("num",num)
num -= 10
print("num",num)
num **= 10
print("num",num)


# LOGICAL OPERATOR

#a> Not operator:- # it reverse the real output
print(not False)
print(not True)
a = 50
b = 56
print(not (a<b))

# b> And operator:- # if both are treue then its return true
val1 = True
val2 = True
print("and operator", val1 and val2)

val1 = True
val2 = False
print("And operator", val1 and val2)

#c> or operator :- it return true any of one input is true
val1 = True
val2 = True
print("and operator", val1 or val2)


val1 = True
val2 = False
print("and operator", val1 or val2)


# TYPE CONVERSION:-
# its add simply addition
a = 2
b= 5.98
sum = a + b
print(sum)
# #  both code gives error due pyhon 
# cannot add string or int value
# a = "2"
# b= 5.98
# sum = a + b
# print(sum)

#TYPE CASTING :- convert the class of any type
a = int("2") # convert string to int
b = 4.26
sum = a + b
print(sum)


# BASIC INPUT EXAMPLE
name = input("enter your name")
age = int(input("enter your age"))
marks = float(input("enter your marks"))

print("welcome",name)
print("age= ", age)
print("marks=",marks)
print(type(name))
print(type(age))
print(type(marks))