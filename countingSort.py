'''
Jacob Martin
3/12/2018

Counting Sort: 

Counts the number of objects having distinct key values, creates a bucket for each value, then increments the counter (hence counting sort) for each
value in the bucket. Because the algorithm creates buckets for the range of values to be inputted, there is one restriction: the max k value must
be known beforehand

For our purposes, we will sort characters in the alphabet


RUNTIME: BEST, AVERAGE, AND WORSE: O(n+k). Where n= size of input and k = range of values from 0 to k

'''





def countingSort(myArr):
	output = [0 for i in range(256)] #This will be our final sorted array

	#Create a count array to store count of individual characters and initialize all counts to 0
	count = [0 for i in range(256)]

	#Storing resulting answer since the string is immutable
	ans = ["" for _ in myArr]

	for i in myArr:
		count[ord(i)]+=1 #ord returns the unicode character, so 'a' == 97 

	#Change count[i] so that count[i] now contains the actual position of this character in the output array
	for i in range(256):
		count[i]+=count[i-1]

	#Build the output character array
	for i in range(len(myArr)):
		output[count[ord(myArr[i])]-1]=myArr[i]
		count[ord(myArr[i])] -=1

	#Copy output array to answer array. So that we contain the sorted characters.
	for i in range(len(myArr)):
		ans[i] = output[i]
	return ans



def countingSort2(myArr,k):
	counter = [0] * (k+1) #Create K+1 buckets
	for i in myArr:
		counter[i]+=1 #increment counter for each time a vlue appears

	index=0
	for i in range(len(counter)): #For the length of the counter
		while 0 < counter[i]: #while that counter is >0 
			myArr[index]=i #Enter the sorted value into the array
			index+=1 #Move the index to the next
			counter[i]-=1 #Decrease counter amount for that bucket
	return myArr




#arrayToSort="xmnajkdasdfjhkjahdfxqpqifh"
arrayToSort2=[4,3,2,1,4,3,2,4,3,4]
print("Before Sort: ", arrayToSort2)
print("After sort: ", countingSort2(arrayToSort2,4))
