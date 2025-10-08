# REDUCE FUNCTION USING LAMBDA FUNCTION
from functools import reduce
#list of numbers
numbers = [1,4,5,6,7,5,3,4,1]

#calc the sum of the numbers using the reduce function
sum = reduce(lambda x,y : x+y,numbers)
print(sum)


#  usinf def function 
from functools import reduce
#list of numbers
numbers = [1,4,5,6,7,5,3,4,1]
#calc the sum of the numbers using the reduce function
def mysum(x,y):
    return x+y
sum = reduce(mysum,numbers)
print(sum)