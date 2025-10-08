# FIND THE NIUMBER OF FOLDERS
import os
folders = os.listdir("data")

print(folders)

# find the subfolder of tutorial
for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))
