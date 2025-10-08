# STRINGS ARE IMMUTABLE
#upper():-
str1 = "AbVbDFbkdbbbf"
print(str1.upper()) 
#lower():-
print(str1.lower())

#count():- # count the spacific char in the string 
print(str1.count("b"))

# strip() :- remove white space before and after the string
str2 = " silver spoon "
print(str2.strip())

# split() :-  rsplit the string in diff str 
print(str2.split())

# replace():- replace any string or charecter of the string
print(str2.replace("sp","m"))

#Rstrip():-  # remove any trailing charecter
str3 = "Hello!!!"
print(str3.rstrip("!"))

# Capitalize():- only the first char of the strinfg convert in upper case
# and others at=re in lower case
# if 1 st char is  already in upper case then no change occurance
print(str3.capitalize())

# center():- align the string to the center as per the parameter given by user
str4 = "welcome To the console!!"
print(str4.center(50,"."))

# endswith():- check the staement of the string
print(str4.endswith("!!"))
print(str4.endswith("to",4,10))

# startwith():-
print(str4.startswith("wel"))

#find():- find index position of the char in string
# find is similar to index method :- the diff is 
# index rise an exception if value is absent where find() doesnot rise an exception
print(str4.find("to"))
# index():- 
print(str4.index("console"))

#Isalnum():-return true only if entire string only consist of a-z ,A-Z, 0-9.if any other cherecter are present then gives ERROR
print(str4.isalnum())    #  in str4  "!" is present with lower case   so   return "False"

# Isalpha():- return true only if the entire string only consist of A-Z, a-z, 0-9 any other char or puncctuations or number(0-9)
# are present  then return "False"
print(str1.isalpha())

#Isupper :- return true if all the char in the str are in uppercase
print(str1.isupper())

#Islower():- return true if all the char in the str are in lower case
print(str4.islower())

# Isprintable():return true if all the values with the given str are printable if not then return False
print(str4.isprintable())

#Isspace():- return true only and only if the str contains with space else: return Falsw(spacebar/tab bar)
str ="      "
print(str.isspace())

#Istitle():-return true only if first word of each word ofthe string are in uppercase else: false
str5 = "Ankit Is An Freelancer"
print(str5.istitle())

# swapcase():- it change the uppercase to lowercase and vice versa
print(str4.swapcase())

# title():- caitalize each first letter of the word within the string
print(str4.title())