my_set = {1, 2, 3, 4}
set2 = { 2,4,3,5,6,7,}
print(my_set)
print(set2)

# add():-  add element in the set
my_set.add(5) 
print(my_set)

#remove():- remove ele from the set
my_set.add(5)
print(my_set)

# discard():-  Removes element  if exists, otherwise does nothing
my_set.discard(6)
print(my_set)
my_set.discard(5)
print(my_set)

#pop():- remove a random element
my_set.pop()
print(my_set)

#union():- combine both set value and return new set
set = my_set.union(set2)
print(set)

#intersection():- combines common values and return new
set= my_set.intersection(set2)
print(set)