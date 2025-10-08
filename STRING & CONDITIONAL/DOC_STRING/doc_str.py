# PYTHON COMMENTS VS DOCSTRINGS:-
# comment :-            
            # comment are description that help programmers better understand the intel and
                # functionality of the program they are completly ignored by the python inter pretor

#DOC_STRING:-    
            # python  docstring are the string litral that appear right after
                # of a function "method" class on module
        #python docstrings are strings  used right after the defination of a function,
            # ,method , class  or module (like in example below)..they used to document our code

n = int(input("enter the numbers:"))
def square(n):
    '''take in a number n, return the square of n'''
    print(n**2)  # square  of n
square(n)
print(square.__doc__)

#PEP-8 :- 
        # it is a document that provides guidelines and best practices on how 
            # to write python code the primary focus of PEP-8 is to improve the 
                #radability and consistency of python code
#PEP(PYTHON ENHANCEMENT PROPOSAL) is a document that describes new features proposed for python and 
    # that describes new features proposed for python and documents aspects of python 
        # like design and style for the community