'''
Created by Jacob Martin 
Date 3/6/18

Hash Table - Chaining
	
Upon insertion, Table accepts a key value that is sent through a hashing function. (there are many, a common and simple one is  k mod n where k = key and n = size of table)
Then the table inserts the key value within the table based upon it's hash value.

*Be sure to check if the value you are inserting is not a duplicate value. 
*If there is a collision, meaning there are different key values mapped to the same hash value, then we need to handle this. Chaining, Linear probing, and open addressing are the three ways to deal with this. 


Deletion, given a key to deltete compute its hash value, then remove from the list.


Goal of hash table is to get constant lookup time.

A hash function is any mathematical function with converts a large zied amount of data into a singular value.

Prime numbers for size of tables reduce the # of collisions compared to non-prime

'''


def get_value(key): 
	return hash(key)%11 #hash function

def inList(ourList, key): #returns true if duplicate
	for i in range(len(ourList)):
		if(ourList[i] == key):
			return True
	return False

class HashTableChaining(object):
	table = [None] * 11

	def insert(self,key):
		val = get_value(key)
		if self.table[val] == None:
			self.table[val] = [key]
		else:
			#if(not inList(self.table[val],key)):
			if(not self.lookup(key)):
				self.table[val].append(key)
			else:
				print("Did not add, multiset hash table not allowed")

	def delete(self,key):
		val = get_value(key)
		if self.table[val]!=None:
			try:
				i=self.table[val].index(key) #if we try to delete a value thats not in the list a value error will happen here 
				self.table[val].remove(self.table[val][i])
			except ValueError:
				print("Can not delete, not in list")
		else:
			print("Error, can not delete, list is empty")

	def lookup(self, key):
		found = False
		val = get_value(key)
		found = key in self.table[val]
		return found

	def printTable(self):
		for i in range(len(self.table)):
			print(self.table[i])



	

def main():
	table = HashTableChaining()
	table.insert(1)
	table.insert(111)
	table.printTable()

if __name__ == "__main__":
	main()