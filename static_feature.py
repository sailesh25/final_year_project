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
#print("Permission List : " + str(permissions_list))
print("Length of permission list : " + str(permissions_list_length))

permissions_list.sort()
files_count = len(os.listdir(benignware_path))
print ("Total no. of files : " + str(files_count))

print("Permission List : " + str(permissions_list))
permissions_vector = np.zeros((permissions_list_length,files_count),dtype = int)
#print(permissions_vector)

# read the entries
with os.scandir(benignware_path) as listOfEntries:  
    for count,entry in enumerate(listOfEntries):
        # print all entries that are files
        print (count)
        if entry.is_file():
            print(entry.name)
            current_apk = APK( benignware_path + entry.name)
            current_apk_permissions = current_apk.get_permissions()
            print (current_apk_permissions)
            
            for permission in current_apk_permissions:
                print (permission)
                for index,current_permission in enumerate(permissions_list):
                    if(current_permission == permission):
                        print(index,current_permission)
                        permissions_vector[index,count] = 1

print (permissions_vector)