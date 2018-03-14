'''
Jacob Martin
3/13/2018


3 Parts to a Scheduler:

Long-Term scheduler - Selects a process from the pool of jobs and loads into memory for execution

Short torm - Selects a process from the ready queue and allocates the CPU

Memory Scheduler - Schedule which process is in the memory and in the disk

When to make a scheduling decision????
	1.) When process goes from running -> block state
	2.) When process switches from running -> ready state
	3.) When process terminates
	4.) When process switches from blocked -> ready state


NonPreemtive - Once a process given CPU, cannot take away CPU from that process
Preemtive -> Once a process given CPU, can take away CPU for another process

General Algos:
	Shortest Job First:
		->Provides minimum average waiting
		->Drawback is to know the length of a CPU request
		->Can be used for a long-term scheduler in a batch system since CPU batch jobs can be estimated
		->Short term scheduler not effective, very hard to estimated


	Shortest Remaining Time:  
		->Preemptive SJF Algo
		-> If a new process arrives in ready queue while prev process executing and is shorter than the current job switch to it 

	Priority Queue Scheduling:
		-> Determine a way to make a process more important than another, whether it's by an external factor (importance) or an internal factor (resources req)
		-> Starvation could be an issue, so we introduce aging. Aging is the technique of gradually increasing the priority of a processs that waits for a long Time


	Guarenteed Schedulin:
		->Scheduling algo that guarantess fairness by monitoring the amount of CPU time spent by each user and allocating the CPU accordingly
		->To create fairness, system must keep track of how much CPU time each process has had since its creation
		-> Ex: n processes, each process will receive 1/n of CPU power
		-> Since the amount of CPU time each process has is known, its fairly easy to compute the ratio of actual CPU time consumed
		->Based on the ratio value, CPU selects which process will run 
'''


