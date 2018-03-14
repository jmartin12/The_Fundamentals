'''

Concurrency issues come into effect when you have a race conditions. Meaning two or more processes / threads trying to access a shared resource
and the output of the processes / threads is determined by precisely who accesses the shared resource first. There are many strategies to deal
with race condition. These strategies provide mutual exclusion

Locks - Locks can be held by a single thread or no thread at all. If a thread attempts to hold a lock that is already held by another
thread, execution is halted until the thread is released (block state). You have 1 lock object per shared resource to function properly.

EX:
	lock = Lock()

	lock.aquire()
	try:
		use shared resource here
	finally: --Finally is imnportyant to unlock the lock even if something goes wrong in the try statement.
		lock.release()


Semaphores - A slightly more advanced lock mechanism. Semaphores have an internal counter that controls the locking feature. Semaphores will block
access to the shared resource if more than a given number of threads have attempted to hold the semaphore.

EX:

	max_conns = N
	semahpore = threading.BoundedSemaphore(max_conns)  -- Note, if no param is given, then counter is defaulted to 1 

	semaphore.aquire()
		use shared resource here
	semaphore.release()

 	Note -- For python, the bounded semaphore will raise an error to call release() more than youve called aquire() 

Mutexes - They act the same way as locks. They provide mutual exclusion for a given critical section. You should have 1 mutex per 1 shared resource.
In python, there is a mutex module that defines a class to allow mutual exclusion by aquiring and releaseing a lock object
but is depricated in python 3. Should stick to thread.lock for python >= 3


Monitors - this contruct allows threads to have both mutual exclusion and the ability to wait for a certain condition to become true
Monitors also have a mechanism for signalin other threads that their condition has been met. A monitor consists of a mutex object and condition 
variables. A condition variable is basically a container of threads that are waiting for a certain condition. Monitors povide a mechanism
for threads to temporarily give up exclusive access in order to wait for some conidition to be met, before regaining access and resuming their task




DEADLOCK - a conndition when two or more processes are each waiting for another to release a resource. An example of this would be when two people
are drawing a diagram, with only one penil and ruler between them. Person A takes the pencil Person B takes the ruler, they each need a pencil AND ruler
to draw, a deadlock occurs when the person with the pencil needs the ruler and the person with the ruler needs the pencil, before he can give up the ruler.
Neither person's request can be satisfied, so a dead lock occurs

Four conidions necessary for a deadlock to occur:
	1.) Mutual exclusion (resource cannot be used by >1 process at a time
	2.) Hold and wait (process already holding resources may request new resource)
	3.) No preemption (only a process holding a resource may release it)
	4.) Circular wait (2 or more processes form a circular chain where each process waits for a resource that the next process chain holds)

Deadlock can be prevented if 1 of the 4 coniditions that are necessary 

Prevention:
	1.) Remove Mutual Exclusion - meaning no preocess may have exclusive access to a resource 
		(non-blocking synchronization algos)
	2.) Remove Hold and Wait - requiring processes to request all the resources they will need BEFORE starting up. Another way is to require
		processes to release all their resources before requesting all the resources they will need. Both of these are generally impractable.
		(all or none algos)
	3.) Removing No preemption - process has to be able to have a resource for a certain amount of time, The inability to enfore preemption may interfere
		with a priority algorithm. (optomistic Concurrency control algos)
	4.) Removing circular wait - Dijkstras solution

Avoidance - For every resource requestm the system checks if granting request will mean that the system will enter an unsafe state (deadlocks state)
			System only grants requests that lead to a safe state. In order to do this, system must know in advance at any time the # and type of all
			resources in existence, available, and requested. Bankers algorithm uses avoidance. For many systems this is impracrible because it is 
			impossible to know what every process will request. 

Detection - Employs an algorthim that tracks rtesouce allocation and process states, and rolls back and restarts one or more of preocesses in order
			to remove the deadlock. Detection is actually very simple for a system to see since the resources that each processes are using are
			already known to the schedular / OS as a whole.

Do Nothing - Windows does this :( 

'''