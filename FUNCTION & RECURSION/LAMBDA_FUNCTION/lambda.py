# LAMBDA FUNCTION
n = int(input("enter 1st number:"))
m = int(input("enter 2nd number:"))

# lambda function can pass "function of function"
def apply(fx,value):
    return 6 + fx(value)

double = lambda x: x*2
cube = lambda x: x*x*x
avg = lambda n,m: (n +m)/2
# print each one respectively (BE_CAREFULL)
print(apply(cube , n))
print(double(n))
print(cube(n))
print(avg(n,m))