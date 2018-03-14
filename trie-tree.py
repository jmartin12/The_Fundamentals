
'''
Created by Jacob Martin 
Date: 3/9/2018

Trie is a tree like structure where each node represent a single character of a given key, search time is O(M) where m = maximum key length.
The tree structure is primarily used for retrieval of keys 
Unlike BST, A node may have more than two children.
While Searching time is relatively good, the drawback is storage for your tree.


'''

class TrieNode(object):
	def __init__(self):
		self.children=[None]*26 #made for alphabet 
		self.word_finished=False
		

class Trie(object):
	def __init__(self):
		self.root = self.getNode()

	def getNode(self): #makes a new node
		return TrieNode()

	def _charToIndex(self,ch): #converts ket current character to index using only a - z , lowercase 
		return ord(ch)-ord('a') 

	def insert(self,key):
		traveler = self.root
		length= len(key)
		for level in range(length):
			index = self._charToIndex(key[level])
			if not traveler.children[index]: #if not in tree, insert
				traveler.children[index]=self.getNode()
			traveler=traveler.children[index]
		traveler.word_finished=True #mark leaf node


	def search(self,key):
		traveler=self.root
		length= len(key)
		for level in range(length):
			index = self._charToIndex(key[level])
			if not traveler.children[index]:
				return False
			traveler=traveler.children[index]
		return traveler!=None and traveler.word_finished




def main():
	keys = ["hello","world","yes","no","hippo","zebra","Test"]
	output = ['not in tree','in tree']
	myTree=Trie()
	for key in keys:
		myTree.insert(key)
	print("{} ---- {}".format("the",output[myTree.search("the")]))
	print("{} ---- {}".format("hello",output[myTree.search("hello")]))
	print("{} ---- {}".format("yes",output[myTree.search("yes")]))
	print("{} ---- {}".format("Test",output[myTree.search("Test")]))
	print("{} ---- {}".format("zebra",output[myTree.search("zebra")]))
	print("{} ---- {}".format("yo",output[myTree.search("yo")]))

if __name__=='__main__':
	main()