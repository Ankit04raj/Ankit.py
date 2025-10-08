#  SEEK  AND TELL FUNCTION
# MAKE A SAMPLE .TXT FILE
with open("sample2.txt","w") as file:
    file.write("123456789@Ankit")

with open("sample2.txt","r") as file:
    print(type(file))
    #MOVE TO THE 10 TH BYTE IN THE FILE
    file.seek(10)

    # check the location where i exist know
    print(file.tell()) 

    #READ THE NEXT 5 BYTES
    data = file.read(5)
    print(data)


# TRUNCATE THE FILE
with open("sample.txt","w") as file:
    file.write("hello world!")
    file.truncate(5)

with open("sample.txt","r") as file:
    print(file.read())