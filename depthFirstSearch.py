'''
Jacob Martin
Created 3/9/2018

Depth First Search

Pseudo:
1.) Start by putting any one of the graph vertices on top the stack
2.) Take the top item of the stack and add it to visited
3.) Create a list of vertex's adjacent nodes, add the opnes which arent visted to top of stack
4.) Repeat 2-3 until stack empty


'''

adjacent_matrix = { 1: [2,3],
					2: [4,5],
					3: [5],
					4: [6],
					5: [6],
					6:[7],
					7:[]
					}


def dfs_recursion(graph,vertex,path=[]):
	path += [vertex]
	for neighbor in graph[vertex]:
		if neighbor not in path: #linear runttime not constant
			path=dfs_recursion(graph,neighbor,path)
	return path	


def dfs_iterative(graph,start):
	stack,path=[start],[]
	while stack:
		vertex=stack.pop()
		if vertex in path:
			continue
		path.append(vertex)
		for neighbor in graph[vertex]:
			stack.append(neighbor)
	return path


print("Recursive -----", dfs_recursion(adjacent_matrix,1))
print("Iterative -----", dfs_iterative(adjacent_matrix,1))
