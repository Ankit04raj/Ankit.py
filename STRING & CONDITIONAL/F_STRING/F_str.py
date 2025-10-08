# F_STRING():-
country = "India"
name = "Ankit"
print(f"my mname is {name} and i am from {country}")

# the : .2fstring():- the dot 2f(:.2f) function print 2 digit after the decimal path
price = 49.08757
print(f"for only {price:.2f} dollars!")
print(type(f"{2*30}"))

# X .FORMAT(A,B) METHOD:-
letter = "hey! my name is {} and i am from {}"
country = "India"
name = "Ankit"
print(letter.format(name,country))