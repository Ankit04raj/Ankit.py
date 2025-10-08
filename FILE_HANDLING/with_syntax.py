#WITH_SYNTEX ():- it works as a function in any method
#& and there is no need to close the file it will automaticaly close the file
with open("FILE_HANDLING\demo_wi.txt","r") as file:
    data = file.read()
    print(data)

with open ("FILE_HANDLING\demo_wi.txt","w") as file:
    file.write("enter a new data")
    file.write("\nas per your input")


with open("FILE_HANDLING\demo_wi.txt","a") as file:
    file.write("\n this is ankit")