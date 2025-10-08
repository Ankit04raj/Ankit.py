# # SHUTIL_MODULE :- 
import shutil

#shutil.copy :- it can copy any file or folder
shutil.copy("practice.txt","practice2.txt")

#shutil.copytree   # this will copy whole folder in a split new folder
shutil.copytree("EXERCISE","EXERCISE_C")

# shutil.move  :- it moves the sub file of any folder in different outside of folder as a file
shutil.move("EXERCISE/exercise1.py","exercise_x.py")

# shutil.rmtree : delete any folder(ONLY FOLDER)
shutil.rmtree("EXERCISE_C")