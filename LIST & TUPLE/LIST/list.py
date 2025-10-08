# "LIST" ARE "MUTABLE" .IT IS A DATA TYPE THAT STORES SET 
# OF VALUE .IT CAN STORE ELE OF DIFF TYPE(STR,INT,BOOLIAN,FLOAT ETC...)
marks = [87.9, 79.5, 65.7,85.0,64.9]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[4])
# possible inndex are 4 inn the upper list(0-4)
# if we print index[5] the "error" found
# print(marks[5])  # 5 index not exist we got error

# MUTING THE LIST
student = ["ankit",9.26,94,"kolkata"]
print(student[0])
print(student[3])
# now immute the index[0]
student[0] = "rishi"
print(student)