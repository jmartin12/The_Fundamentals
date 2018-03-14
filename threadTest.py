'''
Jacob Martin
3/11/2018

Thread - an entity within a process that can be scheduled for execution. All threads of a process share its virtual address space and system resources
Each thread maintains exeption handlers, a scheduling priority, thread local storage, a unique thread ID, and a set of structures the system will 
use to save the thread context until it is scheduled. 

Thread Context Includes:
	1.) thread's set of machine regiesters
	2.) Kernel stack
	3.) thread environment blockj
	4.) a user stack in the address space of the thread's process 


To use the threading module in python, first override the __init__ function with whatever variables you want to be passed in from the parent of the thread
Then define a run() function for what you actually want the thread to do when you run a thread.
When you call thread.start(), it will eventually end up in the run() of the class you defined.

'''


import threading
import time

exitFlag=0


class myThread(threading.Thread):
	def __init__(self,threadID,name,counter):
		threading.Thread.__init__(self)
		self.threadID=threadID
		self.name=name
		self.counter=counter
	def run(self):
		print("Starting " + self.name)
		print_time(self.name,5,self.counter)
		print("Exiting " + self.name)


def print_time(threadName,counter,delay):
	while counter:
		if exitFlag:
			threadName.exit()
		time.sleep(delay)
		print("%s: %s" % (threadName,time.ctime(time.time())))
		counter -=1

thread1 = myThread(1,"Thread-1",1)
thread2 = myThread(2, "Thread-2",2)

thread1.start()
thread2.start()