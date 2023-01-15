import os
cwd=os.getcwd()
print(cwd)
#get the current working directory
#output
#C:\WhiteHatJr\Python\Class99
#-------------------------------
#os.chdir('../')
print(os.getcwd())
#output
#C:\WhiteHatJr\Python
#------------------------------------
#create directory
#os.mkdir("Ashmita")
#------------------------------------
directory="Myfolder1"
parent_dir="C:/WhiteHatJr/Python/Class99"

path=os.path.join(parent_dir,directory)
#os.mkdir(path)
#----------------------------------------
dir_list=os.listdir("C:/WhiteHatJr/Python/Class99")
print(dir_list)
#lists all files and folder
#-----------------------------------------
#os.rmdir("Myfolder1")
#removes the directory
os.remove("C:/WhiteHatJr/Python/Class99/backup/file3.txt")