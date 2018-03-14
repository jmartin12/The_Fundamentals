'''
Jacob Martin
3/12/2018

Factorial - creates a factorial based off user inputs

'''
from math import factorial as fct

def factorial(n):
	num =1 
	while n>=1:
		num*=n
		n-=1
	return num

try:
	iterations = int(input("Enter in the # of iterations for factorial\n"))
	print(factorial(iterations)) 
	#or
	print(fct(iterations))
except ValueError:
	print('Not an int')



