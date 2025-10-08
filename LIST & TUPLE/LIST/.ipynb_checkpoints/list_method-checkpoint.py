list =  [2,3,1,1]
print(list)
# append():- add element at the end of the list
list.append(4)
print(list)

#sort():- sort the list in ascending order
list.sort()
print(list)
# now sort the list in"descending" order
list.sort(reverse = True)
print(list)

# reverse() :- reverse the list
list.reverse()
print(list)

# insert([idx],ele)  # insert element at index
list.insert(3,6)
print(list)

# remove():- remove first occuerence of elements in the list
list.remove(1)
print(list)

# pop():- remove element at index possistion
list.pop(1)
print(list)
