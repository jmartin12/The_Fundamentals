'''
Created by Jacob Martin 
Date 3/7/18

Based on the idea that finding a min or max element in an unsorted array and then putting in its correct pos in a sorted array.


PROS:
	one of the simplest sorting algorithms out there
	works well if you have small data sets


CONS:
 O(n^2)
 ineficient with large data sets
'''


def selectionSort(myList):
	for fillslot in range(len(myList)-1,0,-1):
		positionMax=0
		for location in range(1,fillslot+1):
			if myList[location]>myList[positionMax]:
				positionMax=location

		temp = myList[fillslot]
		myList[fillslot]=myList[positionMax]
		myList[positionMax]=temp


_list = [100,1,2,3,70,40,21,34,50,6,377,30,20]
print(_list)
selectionSort(_list)
print(_list)



