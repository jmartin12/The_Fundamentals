'''
Created by Jacob Martin 
Date 3/7/18

ASSUME (len(list) == 1, therefore sorted)

Works by getting mid index of the list, then slice the list in two, a left and right, recursively until the base case is met for all values in list.

Then we merge the lists, combining two lists at a time with the smallest number inserted first into the original list.

Merge is a stable sort -- meaning the input data that has keys with the same value are in the same order as the output array

RUntime: 

We can divide a list in half log n times where n is the length of the list.
Then the merge, a list size n will require n operations. so 


PROS: 
	O(nlog(n))
	Simple To Understand
	parrelilizeable
	Works well in large data sets of extremely unorganized data
CONS: 
	Not as fast as quicksort
	Requires as much memory aS 	the original array

'''


def mergeSort(myList):

	print("Splitting ", myList)
	if len(myList) > 1:
		mid = len(myList)/2
		left = myList[:int(mid)]
		right = myList[int(mid):]
		mergeSort(left)
		mergeSort(right)


		i = 0
		j = 0
		k = 0

		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				myList[k] = left[i]
				i +=1
			else:
				myList[k] = right[j]
				j+=1
			k+=1

		while i<len(left): #repeatedly taking the smallest item from the sorted lists.
			myList[k]=left[i]
			i+=1
			k+=1

		while j < len(right): #repeatedly taking the smallest item from the sorted lists.
			myList[k]=right[j]
			j+=1
			k+=1
	print("Merging", myList)



_list = [100,1,2,3,70,40,21,34,50,6,377,30,20]
mergeSort(_list)
print(_list)