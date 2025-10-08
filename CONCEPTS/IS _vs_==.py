#IS  "VS" == .KEY_WORD
# IS :-  check  the exact location in memory
#== :-  check the value 
a = 4
b = "4"
print(a is b)   # check  the exact location in memory
print(a == b)   # check the value 

a = [1,45,67]
b = [1,45,67]
print(a is b)   # false
print(a == b)   # true

a = "ankit"
b = "ankit"
print(a is b)   # true
print(a == b)   # true