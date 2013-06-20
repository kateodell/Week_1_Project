import os
import shutil
import string

# loop through a-z and create 26 directories
# for alpha in range(ord('a'),ord('z')+1):
# 	os.mkdir("./" + chr(alpha))

for alpha in string.ascii_lowercase:
	os.mkdir("./" + alpha)

# get the list of all the file names in original_files
original_files = os.listdir("./original_files/") 

# loop through the list of files, get the first letter of the file 
# and move the file to the right folder
for f in original_files:
	shutil.move("./original_files/"+f,"./"+f[0])
