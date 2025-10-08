#SHOW THE INDEX POSITION (FOR LOOP)
marks = [12,56,54,32,97,87,4,3]
index = 0 
for mark in marks:
    print(mark)
    if (index==3):
        print("Ankit awesome!")
    index += 1

#ENUMERATE_FUNCTION
marks = [12,56,54,32,97,87,4,3]
for index,mark in enumerate(marks):
    print(mark)
    if (index==3):
        print("Ankit awesome!") 