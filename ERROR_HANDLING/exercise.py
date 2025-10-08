# ENETER AN INTIGER BETWEEN 5 TO 9 WHICH SHOWS "quit" AS OUTPUT
# OTHER WAISE AT ANY TYPES OF INPUT IT RISE VALUE ERROR:-

a = int(input("enter a number between 5 to 9:-"))
if (a>5 or a<9):
    print("quit")
else:
    raise ValueError("value shound be in intiger form between 5 to 91")
