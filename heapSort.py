'''
Heap property: every child node is <= to its parent, also satisfies C.B.T property.
Complete Binary Tree property: binary tree where every level, except possibly the last, is completely filled and all nodes are as far left as possible
Binary Tree: Trr in which every internal node has at most 2 children
Tree: asyclic connected graph


Heap is good for array based implementation because the left and right child can be calculated by 2*I+1 and 2*I+2, repectively (assuming index starts at 0)


Heap Sort Algo:
1.) Build max heap from input
2.) Since largest item is root from max heaping the input, replace it with the last item of the heap followed by reducing the size of heap by 1, then heapify the root. 
3.) Repeat while size of heap is > 1



'''




def heapify(myList,n,i):
	largest=i
	l=2*i+1
	r=2*i+2


	if l<n and myList[i] <myList[l]:
		largest=l

	if r<n and myList[largest]<myList[r]:
		largest=r

	if largest != i:
		myList[i],myList[largest]=myList[largest],myList[i]
		heapify(myList,n,largest)




def heapSort(myList):
	n= len(myList)

	#build maxheap
	for i in range(n,-1,-1):
		heapify(myList,n,i)

	#One by one extraction
	for i in range(n-1,0,-1):
		myList[i],myList[0]=myList[0],myList[i]
		heapify(myList,i,0)


_list = [100,1,2,3,70,40,21,34,50,6,377,30,20]
print(_list)
heapSort(_list)
print(_list)