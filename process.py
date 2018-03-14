'''
Jacob Martin
3/11/2018


Process- an executing instance of a program. Also referred to as task. Process is always stored in the main memory. Several processes may
be associated with a program 

Process Resources:
	1.) virtual address space
	2.) executable code
	3.) open handles to system objects
	4.) security context
	5.) unique process ID
	6.) environment variables
	7.) minumum and maximum working set sizes
	8.) At least one thread of execution, each process start with a single thread. often called the primary thread, but can create additional threads

exec functions execute a new program, replacing the current process. The do not return. 
"l" variants are good if the number of paramaters is fixed
"v" variants are good if the number of paramaters is variable, pass multiple as a list or tuple
'p' variants search the PATH env variable for the file to be executed


'''

import os #for execv
import sys


print("Starting a new process using execl")

#print(os.getcwd())

path = str(os.getcwd) + "\hashTable.py"

os.execl(path,"")

print("Primary Process Finished")
