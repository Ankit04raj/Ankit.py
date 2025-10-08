# OS MODULE TO REMOVE ANY FILE (JUST GIVE THE LOCATION OF FILE)

# import os
# os.remove("sample.txt")

# go to write_append file run the 2nd last program 
# it gives u a sample.txt file ..and come to os module 
# 1st program the above one ..after running it it will delete the sample.txt file




# MAKE A FOLDER OF "data" AND MAKE 10 SUBFOLDER IN DATA USING OS MODULE
import os
if(not os.path.exists("data")):
    os.mkdir("data")

for i in range(0,10):
    os.mkdir(f"data/day{i+1}")

# # RENAME THE FOLDER (SUB_FOLDER)
# import os
# for i in range (0,10):
#     os.rename(f"data/day{i+1}",f"data/tutorial{i+1}")


# # FIND THE NIUMBER OF FOLDERS
# import os
# folders = os.listdir("data")

# print(folders)