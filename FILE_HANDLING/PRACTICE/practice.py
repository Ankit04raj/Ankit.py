#CREATE A NEW FILE "SAMPLE1.TXT" USING PYTHON.ADD THE DATA AS GIVEN
with open("sample1.txt","w") as file:
    file.write("Hi everyone\nwe are learning filei/o\nusing Java\ni like programing in Java")

#WAF THAT REPLACE ALL OCCURRENCE OF "Java" WITH "Python"
with open("sample1.txt","r") as file:
    data = file.read()

    new_data = data.replace("Java","Python")
    print(new_data)
# to show change in file we have to write the file now:-
with open("sample1.txt","w") as file:
    file.write(new_data)

#SEARCH IF THE WORD "LEARNING" EXISTS IN THE FILE OR NOT
def check_for_word():
    word = "learning"
    with open("sample1.txt","r") as file:
        data = file.read()
        if (data.find(word) != -1):
            print("found")
        else:
            print("not found")
check_for_word()


#WAF TO FIND LINE OF THE FFILE DOES THE WORD
# "LEARNING" OCCUR FIRST  PRINTN -1 IF WORD NOT FOUND
def check_for_line():
    word = input("enter the word:-")
    data = True
    line_no = 1
    with open("sample1.txt","r") as file:
        while data:
            data = file.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1
print(check_for_line())


#FORM A FILE CONTAINING NUMBERS SEPARATED BY COMA,
#PRINT THE COUNT OF EVEN NUMBERS.
with open("practice.txt","w") as file:
    file.write("1,23,5,4,54,5,56,")

with open("practice.txt","r") as file:
    data = file.read()
    print(data)

    num = ""
    for i in range (len(data)):
        if(data[i]==","):
            print(int(num))
            num =""
        else:
            num += data[i]


########  0r  SPLIT_METHOD ##########  
count =0
with open("practice.txt","r") as file:
    data = file.read()
    
    nums = data.split(",")
    for val in nums:
        if (int(val) %2 ==0):
            count += 1
print(count)