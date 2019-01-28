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

random_events_cmd = "adb shell monkey -p "+package_name + " -v 5000"
print(random_events_cmd)

if(device.is_installed(package_name)):
    print("Already installed")
    #status = device.uninstall(package_name)
    #print("Uninstalled")
    
    
    proc_id = os.popen("adb shell ps | grep 'truecaller'").read()
    print(proc_id)
    proc_id = (proc_id.split('  ')) 
    proc_id = int(proc_id[2])
    print("Process Id :" + str(proc_id))
    
    f = open("process_ID.txt", "w")
    f.write(str(proc_id)) 
    f.close()
    random_events_log = os.popen(random_events_cmd).read()
    kill_cmd ="adb shell kill -SIGKILL " + str(proc_id)
    os.system(kill_cmd)
    #print(random_events_log)


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
    


