# FILTER FUNCTION
l = [1,4,5,6,7,5,3,4,1]

def filter_function(a):
    return a>3

final_l = list(filter(filter_function,l))
print(final_l)