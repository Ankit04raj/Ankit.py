#WHILE_LOOP:-
i = int(input("enter the number:-"))
print(i)
while (i <= 45):
    i = int(input("enter the number:-"))
    print(i)
print("the loop is completed")

# REVERSE_WHILE_LOOP :-
count = 5
while (count > 0):
    print(count)
    count -= 1
else:
    print("i am inside")


# DO_WHILE_LOOP():-
i = 0
while True:
    print(i)
    i += 1
    if (i % 100 == 0):
        break


# TABLE + BREAK 
N = int(input("enter the table number:-"))
for i in range(15):
    if (i == 10):
        break
    print(N,"x",i +1,"=", N*(i+1))


#CONTINUE:-
N = int(input("enter the table number:-"))
for i in range(12):
    if (i == 10):
        print("skip the itteration")
        continue
    print(N,"x",i +1,"=", N*(i+1))
