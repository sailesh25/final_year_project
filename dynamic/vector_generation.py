import numpy as np


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