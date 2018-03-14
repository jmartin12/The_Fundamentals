'''
Jacob Martin
3/11/2018



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



LIVELOCK -similar to a deadlock, except that the states of the process involved in the livelock constantly change with regard to one another, but
none progress further into the program. Livelock is a special case of resource starvation. Starvation is when a process is perpetually denied
necessary resources to process its work. An example of this is when two people meet in a narrow corrdor. And each tries to be polite by moving
aside to let the other person pass, but they end up swaying side to side withouth making any progress because they both repeatedly move the 
same way at the same time.

Livelock is a risk with some algorithms that use detection for deadlock handling. If more than one process takes action of trying to fix 
dead lock, then the deadlock detection algorithm can repeatedly be triggered. This can be avoided by putting a priority on who detects the
deadlock algorthm first. 


The main difference between livelock and deadlock is that threads are not going to be blocked, instead they respond to each other continuously,
therefore wasting CPU cycles. 

'''