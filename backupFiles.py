import os
import shutil

source=input("Enter source folder name: ")
destination=input("Enter destination folder name: ")

source=source+'/'
destination=destination+'/'

listOfFiles=os.listdir(source)
for file in listOfFiles: 
    shutil.copy((source+file),destination)

#output
#Enter source folder name: C:\WhiteHatJr\Python\Class99\Myfolder
#Enter destination folder name: C:\WhiteHatJr\Python\Class99\backup