import os
from androguard.core.bytecodes.apk import APK
# detect the current working directory
benignware_path = "/home/venkatesh/fyp/github/final_year_project/Benignware/"

# read the entries
with os.scandir(benignware_path) as listOfEntries:  
    for entry in listOfEntries:
        # print all entries that are files
        if entry.is_file():
            print(entry.name)
            a = APK( benignware_path + entry.name)
            print (a.get_permissions())

            