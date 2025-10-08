#WALRUS_OPERATOR (:=)  
#new to python
#which assignment expression aka walrus operator
#assigns values to variables as part of a larger expression

# eg1>
a = True
print(a:= False)

# eg>
numbers = [1,2,3,4,5]
while (n:= len(numbers)) > 0:
    print(numbers.pop())

# eg3>(NORMAL LOOP METHOD)
foods = list()
while True:
    food = input("what food do you like? ")
    if food == "quit":
        break
    foods.append(food)

#WALRUS METHOD:-
foods = list()
while(food:= input("what food do you like? -")) != "quit":
    foods.append(food)