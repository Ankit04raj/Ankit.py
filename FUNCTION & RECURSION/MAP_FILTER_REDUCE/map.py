# cube USING FUNCTION
def cube(x):
    return x * x * x
print(cube(2))
# cube is define above
l = [1,3,4,5,3,2,3,4]
newl = []
for item in l:
    newl.append(cube(item))
print(newl)

# cube  USING MAP FUNCTION
def cube(x):
    return x * x* x
l = [1,4,5,6,7,5,3,4,1]
newl = list(map(cube,l)) 
# here we hve to define the map function as a list

# IN PLACE OF CUBE WE CAN USE "lambd x: x*x*x" then we dont have to define cube
#def function IS SIMPLY IGNORED:- LIKE 
# newl = list(map(lambda x: x*x*x,l)) 
print(newl)