#READ("r") open for reading file (Default)
#file.read() :- read whole the file
file = open("FILE_HANDLING\demo_R.txt","r")
data = file.read()   # read full file
print(data)
print(type(data))
file.close()

# file.readline():-print(line_x) # read only the given line
file = open("FILE_HANDLING\demo_R.txt","r")
line1 = file.readline() 
print(line1)

line2 = file.readline() 
print(line2)
print(type(line2))
file.close()

#file.read(i) ,{i = index} :- read till the index position of file
file = open("FILE_HANDLING\demo_R.txt","r")
data = file.read(5) 
print(data)
print(type(data))
file.close()

#"r+"  read  + overwrite  (pointer   start) :- notruncate
#"w+"  read  + overwrite  (pointer   start) :-   truncate
#"a+"  read  + append      (pointer   end)  :- notruncate