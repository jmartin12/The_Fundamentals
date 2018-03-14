'''
Jacob Martin


BIG - O:
	-> Relative representation of the complexity of an algorithm
	-> Upper Bound ( Worst Case Scenario )
	-> Relative : Big o comparisons should only be kept within their respective types. So sorting with sorting algos, swapping with swapping, 
					counting with counting, etc.. 
	-> Representation: Big -O reduces the comparison between algorithms to a single variable. Variable is chosen off of observations or assumptions.
	-> Complexity: If it takes one second to sort 1000 elements how long will it takes to sort 10000. Complexity in this example is a relative measure
				to something else.

	Another good example of this is adding numbers. Assume that adding is the most expensive operation in an adding algorithm. I.E. 11456+21092


	Linear complexity O(n)  -- If we add two 5 digit numbers,we have to do 5 additions. If we add two numbers with 100000 digits,
	 we take 100000 additions.


	Quadratic complexity O(n^2) -- multiplication is not Linear. You have to take the first digit in the bottom number, and multiply it against
	each digit in the top number and so on through each bottom digit, then add the resulting numbers up if needed. So now, compared to addition,
	the most expensive part of the operation changes, its not addition anymore its multiplication. This results in O(n^2 + 2n) 

	Important to note, we only care about the most significant portion of the complexity because the lesser complex portions  have an impact
	on runtime nearly as much as the most complex


	Logarithmic Complexity O(log(n)) -- Suppose you are asked to search for the phone # of john doe in a phone book. We can implement a binary search
	for this, split the book in half, compare the name in the middle and see if its < or > to the name of john doe, and then search the half you
	are closer to. Obviously you need to check if the names match in the algorithm. 

	For a phone book of 3, it takes at MOST 2 comparisons.
	For 7 is takes at most 3.
	for 15 it takes most 4.
	...
	for 1,000,000 it takes 20. 

	Plotted on a graph, this follows the log(n) function. This complexity is actually pretty good for computers.

	Factorial Complexit (O(n!)) -- Traveling Salesmen
	
	Consider 3 towns and 3 roads. Each town is linked to another town with a road inbetween them. What is the shortest path that visits every
	town? 

	3 towns - 3 possibilites
	4 towns - 12 possibilites	 
	5 towns - 60 possibilites
	6 towns - 360 possibilites

	By the time you get to 200 towns there isnt enough time left in the universe to solve the problem with traditional computers.


	Constant complexity O(1) -- N the runtime is the same.

'''