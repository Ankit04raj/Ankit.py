# WAF  to print the length of a list (list is the parameter)
cities = ["delhi","mumbai","noida","gurgaon","pune"]
heroes = ["spiderman","ironman","captain","thor","loki"]

def print_len(list):
    print(len(list))

print_len(heroes)
print_len(cities)
# WAF TO PRINT THE ELEMENT OF A LIST IN A SINGLE LINE
cities = ["delhi","mumbai","noida","gurgaon","pune"]
heroes = ["spiderman","ironman","captain","thor","loki"]

print(heroes[0], end = "\n")
print(heroes[1], end ="\n")

def print_list(list):
    for item in list:
        print(item, end =" ")

print_list(heroes)
print(end="\n")
print_list(cities)
print(end="\n")
#WAF TO FIND THE FACTORIAL OF N( N IS THE PARAMETER)
n = int(input("enter a  number:"))
def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)
cal_fact(n)

# WAF TO CONVERT USD TO INR
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val,"USD=", inr_val,"INR")

converter(76)

# WAF WHICH RETURN A STRING "OOD" OR "EVEN" IF THE NUMBER IS ODD OR EVEN RESPECTIVELY
N = int(input ("enter a number even or odd: "))
def nature_checker(N):
    if N % 2==0:
        print("EVEN")
    else:
        print("ODD")
nature_checker(N)