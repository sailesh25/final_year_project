import os
import numpy as np
from androguard.core.bytecodes.apk import APK
# detect the current working directory
benignware_path  = "/home/venkatesh/fyp/github/final_year_project/Benignware/"
permissions_path = "/home/venkatesh/fyp/github/final_year_project/"
permissions_file = "list_of_permissions1.txt"
#converting text permission to list
with open(permissions_path + permissions_file) as f:
    permissions_list = f.read().splitlines()

permissions_list_length = len(permissions_list)
print("Permission List : " + str(permissions_list))
print("Length of permission list : " + str(permissions_list_length))


# read the entries
with os.scandir(benignware_path) as listOfEntries:  
    for entry in listOfEntries:
        # print all entries that are files
        if entry.is_file():
            print(entry.name)
            current_apk = APK( benignware_path + entry.name)
            print (current_apk.get_permissions())
