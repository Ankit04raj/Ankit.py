#RECURSION
n  = int(input("enter a number:"))
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
    print("end")
show(n)

# FACTORIAL OF N
n  = int(input("enter a number:"))
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return fact(n-1)*n
print(fact(n))

# SUM OF "N" NATURAL NUMBER
n  = int(input("enter a number:"))
def calc_sum(n):
    if(n==0):
        return 0
    else:
        return calc_sum(n-1)+n
sum = calc_sum(n)
print(sum)

#WARF TO PRINT ALL ELEMENT IN A LIST
cities = ["delhi","mumbai","noida","gurgaon","pune"]
def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

print_list(cities)