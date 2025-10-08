# "list_slicing" is simmilar to "strinng_slicing"
# list are "MUTABLE" BUT "STRINGS" are "immutable"
#LIST_NAME[starting[index : ending[index]]]   # but inding index is not included in the list

marks = [87.9, 79.5, 65.7,85.0,64.9]        # 87.9 ,  79.5,  65.7, 85.0, 64.9
                                            #  0       1      2     3      4      #(positivee_slicing)
                                            #  -5     -4     -3     -2    -1     # (negative_slicing)
print(marks[0:4])   # last index is not include 9ignore 4 th index in output
print(marks[0:])     # print till 0 to total list

# negative_slicing
print(marks[-5:-1])
print(marks[-5:])
print(marks[0:-3])  # last index is ignored