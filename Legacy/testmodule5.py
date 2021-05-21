# Import Module
import os
  
# Folder Path
path = r"C:\Users\matth\Documents\workspace\Testfolder"
  
# Change the directory
os.chdir(path)
  
# Read text File
  
newarr = []

def read_text_file(file_path):
    with open(file_path, 'r') as f:
        newvar = f.read()
        newarr.append(newvar)

  
# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith("success.txt"):
        file_path = f"{path}\{file}"
  
        # call read text file function
        read_text_file(file_path)

f=open("NewUnNumbers2.txt","w+")
for line in newarr:
  f.write(line)
f.close()