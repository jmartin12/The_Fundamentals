'''
Created by Jacob Martin 
Date 3/7/18

The goal of partitioning is to move items that are on the wrong side with respect to the pivot value while also converging on the split point


Choose a pivot point. simple way to do this is to choose the first slot in the array, or last. 
Randomization could be good for this as the worst case runtime (O(n^2)) is highly unlikely

Increment left index until a value is >= pivot or left > right
Decrement right index until value is <= pivot or right < left
Swap the values once stopped decrementing/incrementing
Repeat until right < left,
once right < left, we have found our split point.
then swap the pivot value with split point.

At this step in the algo, all values on the left of the pivot value are < and right side are >



PROS:
	No additional memory needed
	Implementation is easy
	Most of the time the runtime is O(nlog(n))

CONS:
	Worst case runtime is O(n^2) -- Slow as bubble sort





QUICK VS MERGE:
	Quick is in space, meaning it doesnt need any additional mem. Merge sort is not in space.
	The speed of quick is dependent upon how you choose a pivot point
	When a data set is close to same, all 1's and 2's for example then quick sort will be innefcient, perhaps using mergesort would be better 

	Quicksort prefered fir arrays, merge for LL's. 
	This is because in arrays you can do random access as elements are conitinuous in memory. In LL, you can't do that. you have to traverse every node from the head to the node you want to be at because we dont have continuous blocks of memory in LL. 
	The way quicksort is designed, the overhead is increased when it comes to using it for LL's.
'''


def startQuickSort(myList):
	quickSortUtil(myList,0,len(myList)-1)


def quickSortUtil(myList, first,last):
	if first<last:
		split=partition(myList,first,last)
		quickSortUtil(myList,first,split-1)
		quickSortUtil(myList,split+1,last)

def partition(myList,first,last):
	pivotValue=myList[first]
	left=first+1
	right=last
	done=False

	while not done:
		while left<=right and myList[left] <= pivotValue:
			left+=1
		while myList[right] >= pivotValue and right >=left:
			right-=1
		if right < left:
			done=True
		else:
			temp=myList[left]
			myList[left]=myList[right]
			myList[right]=temp

	temp=myList[first]
	myList[first]=myList[right]
	myList[right]=temp

	return right

_list = [100,1,2,3,70,40,21,34,50,6,377,30,20]
print(_list)
startQuickSort(_list)
print(_list)