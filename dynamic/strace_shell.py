import subprocess
from subprocess import STDOUT, check_output
import os
import psutil


def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()

#proc = subprocess.call("adb shell  ps | grep 'com.truecaller'",timeout=10,shell=True)

#random_events_log = os.popen(random_events_cmd).read()
f = open("process_ID.txt", "r")
word = f.read().split()
print(word)
proc_id = word[0]
logger_cmd = "adb shell strace -p "+  str(proc_id) +" -c  > sample.csv"
proc = subprocess.call(logger_cmd,timeout=10,shell=True)
#proc = subprocess.Popen("adb shell strace -p 5045 -c",shell=True)

#seconds = 10
#output = check_output("adb shell strace -p 4633 -c", stderr=STDOUT, timeout=seconds,shell=True)
print(proc)