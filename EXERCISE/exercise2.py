# DEFINE TIME 
import time
timestamps = time.strftime("%H : %M : %S")
print(timestamps)
timestamps = time.strftime("%H")
print(timestamps)
timestamps = time.strftime("%M")
print(timestamps)
timestamps = time.strftime("%S")
print(timestamps)

# print day time according to the clock
import time
timestamps = time.strftime("%H:%M:%S")
print(timestamps)
timestamps = int(time.strftime("%H"))
print(timestamps)
if (6<timestamps<12):
    print("good morning")
elif(12<timestamps<17):
    print("good afternoon")
elif(17<timestamps<21):
    print("good evening")
else:
    print("good night")