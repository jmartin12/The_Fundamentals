'''
Jacob Martin
3/12/2018

Adjacency List:
	-> Compact way of representing relationships between nodes with only existing edges
	-> Much more efficient than an adjacency matrix in terms of storage of a graph, especially sparse graphs
	-> However, slow lookup time is possible of edges. Worse case can become O(n) if the list is unordered
	-> Stores all neighbors of the a vertex at a current vertex, so neighbor lookup time is trivial  

	adjacent_list= { 1: [2,3],
					2: [4,5],
					3: [5],
					4: [6],
					5: [6],
					6:[7],
					7:[]
					}


Adjacency Matrix:
	-> NxN array, if weighted then filled with the weight of the edge, if not just T/F
	-> Requires O(N^2) space complexity
	-> AccessTime is O(1) to check the distance b/n connected nodes, since you can just look it up in the array.;
	-> This is innefecient when the graph is sparse, meaning there are a lot less edges than n^2 nodes
	-> Neighbor lookup time (O(n)) is higher than adjacency list because you need to check all possible neighbors 

	matrix = [ 	0 0 0 0 0
				1 1 1 1 1
				0 0 0 0 1
				1 0 1 0 1
				0 1 0 0 1   ]

Objects and Pointers:
	->basic datastructures that would be comprised of classes like edges and vertex
	->The edge could have the option of being a directed or undirected and it could contain a weight
	->The vertex could have more data values like an ID, name, and additional properties depending on the situation you are using them in
	->This is in general a more OO approach to graphs 

	in python this would look something like:

	a = vertex(1)
	b = vertex(2)
	ab = edge(a,b,30)


'''