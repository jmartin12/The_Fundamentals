'''
Jacob Martin 
3/11/2018

system call fork() creates a copy of the process which has called it. copy runs as a child process of the calling process (parent). child process gets
data and code of the parent process. The child has a PID of its own from the O.S. Child process runs as an indepent instance from the parent process.
return value of fork is 0 for child process and > 0 for parent, and <= -1 for error. 

'''

import os #for fork()


def childHandler():
	print('Hello I am a child, my PID is %d', os.getpid())
	os._exit(0) #required because child process would return into the the input statement

def parent():
	while True:
		pid=os.fork()
		if pid == 0:
			childHandler()
		else:
			pids = (os.getpid(), pid)
			print("In parent process, parent PID: %d, child PID: %d\n" %pids)
		reply = input("f for new fork, anything else to quit")
		if reply == 'f':
			continue
		else:
			break



parent()
