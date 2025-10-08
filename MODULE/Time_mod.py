# TIME MODULE:-

#Time.time():-
import time
#FOR WHILE LOOP
def usingWhile():
    i = 0
    while i < 5000:
        i = i + 1
        print(i)

#FOR "FOR_LOOP" 
def usingFor():
    for i in range(5000):
        print(i)

init = time.time()   # init :- initiate "time.time( )"
usingFor()
t1 = time.time() - init
init = time.time()
usingWhile()
t2 = time.time() - init
print(t2)
print(t1)   # the time is count in second for run the program


#TIME.SLEEP():- THIS will sleep the code for given instant of time
# import time    #(u can re import the time )
print(4)
time.sleep(3)
print("this is exectuted after 3 sec")


#TIME.STRFTIME():- it shows local time and month, date,year, sec, hour ,minute

# import time

t = time.localtime()
formatted_time = time.strftime("%y-%m-%d %H:%M:%S",t)
print(formatted_time)