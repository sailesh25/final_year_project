import time
import pandas as pd
import os
import subprocess
from adb.client import Client as AdbClient
# Default is "127.0.0.1" and 5037
client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("emulator-5554")

apk_path = "/home/venkatesh/fyp/Android/Truecaller.apk"

os.system('./package_name.sh ' + apk_path)


f = open("package_name.txt", "r")
word = f.read().split()
print('/')
package_name = word[0]
print(package_name)
print('/')

#random_events_cmd = "adb shell monkey -p "+package_name + " -v 1500"
#print(random_events_cmd)

if(device.is_installed(package_name)):
    print("Already installed")
    #status = device.uninstall(package_name)
    #print("Uninstalled")

    random_events_cmd = "adb shell monkey -p "+package_name + " -v 1"
    print(random_events_cmd)

    random_events_log = os.popen(random_events_cmd).read()

    grep_cmd = "adb shell ps | grep " + "'"+ package_name +"'"
    print(grep_cmd)
    proc_id = os.popen(grep_cmd).read()
    print(proc_id)
    proc_id = (proc_id.split(' ')) 
    print(proc_id)
    proc_id = int(proc_id[4])
    print("Process Id :" + str(proc_id))
    
    f = open("process_ID.txt", "w")
    f.write(str(proc_id)) 
    f.close()
    random_events_cmd = "adb shell monkey -p "+package_name + " -v 1500"
    print(random_events_cmd)
    random_events_log = os.popen(random_events_cmd).read()
    kill_cmd ="adb shell kill -SIGKILL " + str(proc_id)
    os.system(kill_cmd)
    time.sleep(1)
    #print(random_events_log)
    log_csv = pd.read_fwf('sample.csv')
    #log_csv.columns = ["usecs_col","calls_col","errors_col","syscall_col"] 
    print(log_csv)
    #print(log_csv['syscall_col'])
else:
    #installing apk
    status = device.install(apk_path)
    print(status)
    print("Installed")
    n = os.fork()
    if n > 0: 
        print("Parent process and id is : ", os.getpid()) 
  
    # n equals to 0 means child process 
    else: 
        print("Child process and id is : ", os.getpid()) 
        #os.system(random_events_cmd)
    


