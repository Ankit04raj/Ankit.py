# WRITE FILE ("OVERWRITE") IT WILL DELETE THE WHOLE FILE DATA
# & AND INPUT THE REWRITE DATA
file = open("FILE_HANDLING\demo_W.txt","w")
file.write("i am learing video editing")
file.close()

#APPEND :- OPEN FOR WRITING APPENDING TO THE END OF THE FILE IF IT EXISTS
file = open("FILE_HANDLING\demo_W.txt","a")
file.write("\non the davinci resolve")
file.close()

# WE CAN BUILD A FILE BY SIMPLY OPEN 7 CLOSE("WRITE "OR "APPEND")METHOD
file = open("sample.txt","w")
# file = open("sample.txt","a")
file.close()


#"r+" it will over write the file from begning
file =open("FILE_HANDLING\demo_W.txt","r+")
file.write("hey u ")
print(file.read())
file.close() 


#"r+"  read  + overwrite  (pointer   start) :- notruncate
#"w+"  read  + overwrite  (pointer   start) :-   truncate
#"a+"  read  + append      (pointer   end)  :- notruncate