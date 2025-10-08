my_dict = {
    "name" : "Ankit Raj",
    "cgpa" : 9.4,
    "marks" : [76,89,98,79,87]
}
print(my_dict)
#  .KEYS()  :- RETURN ALL KEYS OF THE DICTIONARY
keys= my_dict.keys()
print(keys)

# .VALUES() :- RETURN ALL THE VALUES OF THE STRING
value = my_dict.values()
print(value)

# .items() :- RETURN ALL ("KEY": VALUE) PAIRS AS TUPLES
item = my_dict.items()
print(item)

# .get() :- RETURN THE KEY ACCORDING TO VALUE
GET = my_dict.get("cgpa")
print(GET)

#  .UPDATE() :- INSERT THE SPECIFIED ITEMS TO THE DICTIONARY
new_data = {'b': 3, 'c': 4}
my_dict.update(new_data)
print(my_dict)

# # .CLEAR():- RETURN A EMPTY dictionary
# my_dict.clear()
# print(my_dict)

# .POP() :- DISAPEAR ELEMENT FROM THE DICTIONARY
pop = my_dict.pop("marks")
print(pop)
print(my_dict)
