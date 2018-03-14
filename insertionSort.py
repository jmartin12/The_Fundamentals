'''
Created by Jacob Martin 
Date 3/7/18

Assume a list of 1 is a sorted list

Start outerloop i =1 -> len(myList), i++ , then inner loop at i-1 , go to 0, decrementing j--. In innerloop, check if the value at j+1 is less than j, if it is, then swap, if not, found its place

PROS:
	easy to implement
	works well with small data sets

CONS:
	if you have a long list and a tiny number at the end, overhead of swapping can be costly 
	O(n^2)
	Nested loops -- not that fast
'''


def insertion_sort(myList):
	for i in range(1,len(myList)):
		for j in range(i-1,-1,-1):
			if myList[j] > myList[j+1]:
				myList[j],myList[j+1]=myList[j+1],myList[j]
			else:
				break



_list = [100,1,2,3,70,40,21,34,50,6,377,30,20]
print(_list)
insertion_sort(_list)
print(_list)