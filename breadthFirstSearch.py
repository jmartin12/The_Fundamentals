import collections #this is done because if we use a standard queue structure in python  and try to pop(0) the time complexity rises to O(n)
					#Hoever, the collections module contains a deque object which has a popleft(), but time complexity is O(1)

'''
Jacob Martin
Created 3/9/2018

Algorithm used for traversing graph data structures. 

Usually used for AI problem solving, or shortest path problems

BFS starts from a node, then checks all the nodes at distance one from starting node, then checks all nodes at distance two, so on so forth.
Distance is defined as number of edges between two vertices

To remember which nodes have been visted, BFS uses a queue. The case where this would come in handy as far as performance goes is when there are 
one or more cycles in the graph

BFS is a complete algorithm. meaning it will always return a solution if there is one 

Uses:  Shortest Path, discover all nodes reachable from a vertex, find neightbor nodes in PTP networks, find people at a given distance from 
social networks

Psuedo for algorithm:

1.) check starting node and add its neighbors to queue
2.) get first node from queue then dequeue
3.) go thru neighbors of the node
4.) add neighbor nodes to the a new path list
5.) check to see if the new path ended up at our goal, if so return it
6.) mark node as explored
7.) loop 2 - 7 until empty queue




'''

#undirected, unweighted graph. 
# 7 nodes, 7 edges 

graph = { 'A': ['B','C','E'], 
		  'B':['A','D','E'],
		  'C':['A','F','G'],
		  'D':['B','E'],
		  'E':['A','B','D'],
		  'F':['C'],
		  'G':['C']}


def bfs_shortest_path(graph,start,goal):
	explored=[] #nodes checked
	queue = collections.deque([start]) #nodes to be checked
	#queue = [[start]]
	if start == goal:
		return "Found! Start = Goal"

	while queue:
		path = queue.popleft() #pop shallowest node from queue
		#path = queue.pop(0) 
		node = path[-1] #get last node from path
		if node not in explored:
			neighbors=graph[node] #get its neighbors from the graph
			for neighbor in neighbors:
				new_path = list(path)
				new_path.append(neighbor)
				queue.append(new_path) #add its neighbors into the queue to check
				if neighbor==goal:
					return new_path
			explored.append(node) #add it to the checked nodes
	return "Connecting Path DNE"


print(bfs_shortest_path(graph,'G', 'D'))