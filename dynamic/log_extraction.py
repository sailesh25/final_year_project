import time
import pandas as pd
import os
import subprocess
from adb.client import Client as AdbClient
import numpy as np

#1. Default is "127.0.0.1" and 5037
client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("emulator-5554")
#end 1


#2 path to the application which is going to be analysed
apk_path = "/home/venkatesh/fyp/Android/Truecaller.apk"
#end 2


#3 extracting package name of APK file and writing to package_name.txt
os.system('./package_name.sh ' + apk_path)
#end 3

#4 extracting package name of APK file from package_name.txt
f = open("package_name.txt", "r")
word = f.read().split()
package_name = word[0]
print("Package Name : " + package_name)
f.close()
#end 4

#random_events_cmd = "adb shell monkey -p "+package_name + " -v 1500"
#print(random_events_cmd)

if(device.is_installed(package_name)):
    print("Already installed")
    #status = device.uninstall(package_name)
    #print("Uninstalled")

    #5 Initializing application 
    random_events_cmd = "adb shell monkey -p "+package_name + " -v 1"
    print("Initialising Command " + random_events_cmd)
    random_events_log = os.popen(random_events_cmd).read()
    #end 5

    #6 Extracting Process ID
    grep_cmd = "adb shell ps | grep " + "'"+ package_name +"'"
    print("Process ID Extraction Command " + grep_cmd)
    proc_id = os.popen(grep_cmd).read()
    print("Returned Process ID " + proc_id)
    proc_id = (proc_id.split(' ')) 
    print("Underprocessing Processing Process ID :")
    print(proc_id)
    proc_id = int(proc_id[4])
    print("Process ID :" + str(proc_id))
    #end 6

    #7 exporting Process to process_ID.txt
    f = open("process_ID.txt", "w")
    f.write(str(proc_id)) 
    f.close()
    #end 7

    #8 generating random events
    random_event_count = 1500
    random_events_cmd = "adb shell monkey -p "+package_name + " -v " + str(random_event_count)
    print("Random Events Command " + random_events_cmd)
    random_events_log = os.popen(random_events_cmd).read()
    #end 8  

    #9 killing application process
    kill_cmd ="adb shell kill -SIGKILL " + str(proc_id)
    os.system(kill_cmd)
    #end 9

    #10 Time to write to file by strace_shell.py 
    time.sleep(1)
    #end 10

    #print(random_events_log)
    
    #11 extracting system calls from log.csv
    log_csv = pd.read_fwf('log.csv')
    log_csv.columns = ["usecs_col","calls_col","errors_col","syscall_col"] 
        #print(log_csv)
    log_csv = log_csv['syscall_col']
    log_csv = log_csv.drop(log_csv.index[0])
    log_csv = log_csv.drop(log_csv.index[0])
    log_csv = log_csv[:-2]
        #print(log_csv)
    #end 11


    #12 Exporting to extracted_syscall.csv  
    log_csv.to_csv("extracted_syscall.csv", sep='\t', index=False)
    #end 12

    

    extracted_syscall_path = "/home/venkatesh/fyp/github/final_year_project/dynamic/"
        
    extracted_syscall_file = "extracted_syscall.csv"

    #converting text extracted_syscall to list
    with open(extracted_syscall_path + extracted_syscall_file) as f:
        extracted_syscall_list = f.read().splitlines()

    #number of extracted_syscall in extracted_syscall list
    extracted_syscall_list_length = len(extracted_syscall_list)

    print(" List : " + str(extracted_syscall_list))
    print("Length of extracted_syscall list : " + str(extracted_syscall_list_length))

    #sorting list to optimise the matching 
    extracted_syscall_list.sort()


    total_syscall_path = "/home/venkatesh/fyp/github/final_year_project/"
        
    total_syscall_file = "list_of_syscalls.txt"

    #converting text extracted_syscall to list
    with open(total_syscall_path + total_syscall_file) as f:
        total_syscall_list = f.read().splitlines()

    #number of extracted_syscall in extracted_syscall list
    total_syscall_list_length = len(total_syscall_list)

    print("Total List : " + str(total_syscall_list))
    print("Length of total_syscall list : " + str(total_syscall_list_length))



    #sorting list to optimise the matching 
    total_syscall_list.sort()

    files_count = 1
    #initialising permission vector
    syscall_vector = np.zeros((total_syscall_list_length,files_count),dtype = int)
    #print(permissions_vector)

    cur_index = 0

    for syscall in extracted_syscall_list:
                    print (syscall)
                    for index,current_syscall in enumerate(total_syscall_list):
                        if(current_syscall == syscall):
                            print(index,current_syscall)
                            syscall_vector[index,cur_index] = 1

    print(syscall_vector)

else:
    #installing apk
    status = device.install(apk_path)
    print(status)
    print("Installed")