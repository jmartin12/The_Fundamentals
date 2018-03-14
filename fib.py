'''
Jacob Martin
3/12/2018

Calculates n'th iteration of fib sequence. User input for n

'''

from math import sqrt


def slower_F(n): # O(2^n) 
	if n==0: return 0
	elif n==1: return 1
	else: return slower_F(n-1) + slower_F(n-2)


def faster_F(n):
	return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))


def main():
	try:
		iterations=int(input("Enter how many iterations of the fib sequence\n"))
		print(slower_F(iterations))
		print(faster_F(iterations))
	except ValueError:
		print("Not an integer")







if __name__=='__main__':
	main()