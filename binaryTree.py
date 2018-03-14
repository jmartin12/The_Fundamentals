'''
Created by Jacob Martin 
Date 3/8/18

BST Property says: every internal node has at most 2 children and the keys are less than the parent in the left subree, and greater than the parent in the right subtree
A well balanced BST is O(log(n)) for searching, inserting,deletion, and accessing

Insertion: First check if the tree has a root, if it doesnt, then create new node and initialize it as root.
If the tree has a root, search BST based off of the new key to be inputed. Find its spot on the tree, then insert the new node with its corresponding data values

For getting a value: Searches the tree just like inserting, if there is a match with the key then the payload (value) of the node is returned. If nothing is found, None is returned

For deletion, 3 cases to consider for the node to be deleted:
1.)Node has no children
	->delete node, remove parent reference
2.)Node has one child
  	6 cases to consider:
	  	If the curr node to be deleted has a left child:
	  		1.) if node to be deleted is left child, update left child parent reference, then update parent left child reference
			2.) if node to be deleted is right child, update left child parent reference, then update right child parent refereence 
			3.) if node has no parent, it is root. Replace all root data with the child that is moving to be the new root
		The cases for the right child are asymetrical to the above 3. 
3.)Node has two children
	Need to find a successor -- next-largest key in the tree. 3 cases to consider
		1.) node has right child, successor is smallest key in subtree
		2.) node has no and right child and is left child of its parent, then parent is successor
		3.) node is right child of parent, and node has no rightchild, then the successor of node is successor of its parent, excluding the curr node

		Note - when removing, we chose to spliceout because it will handle every case of deleting and replacing a node without searching for the correct spot on the tree. If we call delete() recursively we can achieve the same goal, but with the added time of searching the tree. 


Preorder - Visit root node first, then recursively do a preorder traversal of the left subtree, followed by a recursive preorder traversal of the right subtree
Inorder - recursive do a inorder traversal of the left subtree, visit root, then recursive inorder traversal of right subtree
PostOrder - recursive PostOrder traversal of left subtree, then recursive PostOrder traversal of right subtree, followed by visit to the root


'''

class BinarySearchTree:
	def __init__(self):
		self.root = None
		self.size = 0

	def Preorder(self,node):
		if node is None:
			return
		print(node.key)
		if node.leftChild is not None:
			self.Preorder(node.leftChild)
		if node.rightChild is not None:
			self.Preorder(node.rightChild)

	def Inorder(self,node):
		if node is None:
			return
		if node.leftChild is not None:
			self.Inorder(node.leftChild)
		print(node.key)
		if node.rightChild is not None:
			self.Inorder(node.rightChild)


	def Postorder(self,node):
		if node is None:
			return
		if node.leftChild is not None:
			self.Postorder(node.leftChild)
		if node.rightChild is not None:
			self.Postorder(node.rightChild)
		print(node.key)



	def length(self):
		return self.size

	def __len__(self):
		return self.size

	def __iter__(self):
		return self.root.__iter__()

	def insert(self,key,value):
		if self.root:
			self._insert(key,value,self.root)
		else:
			self.root = TreeNode(key,value)
		self.size +=1

	def _insert(self,key,value,currNode):
		if key < currNode.key:
			if currNode.hasLeftChild():
				self._insert(key,value,currNode.leftChild)
			else:
				currNode.leftChild=TreeNode(key,value,parent=currNode)
		else:
			if currNode.hasRightChild():
				self._insert(key,value,currNode.rightChild)
			else:
				currNode.rightChild=TreeNode(key,value,parent=currNode)

	def __setitem__(self,k,v): #This overloads the [] operator to allow us to acces nodes within the tree like a pythonic dictionary
		self.insert(k,v)

	def getRoot(self):
		return self.root

	def get(self,key):
		if self.root:
			res=self._get(key,self.root)
			if res:
				return res.payload
			else:
				return None
		else:
			return None

	def _get(self,key,currNode):
		if not currNode:
			return None
		elif currNode.key == key:
			return currNode
		elif key < currNode.key:
			return self._get(key,currNode.leftChild)
		else:
			return self._get(key,currNode.rightChild)

	def __getitem__(self,key): #overloads the [] operator to allow us to acces nodes within the tree in a pythonic dictionary way
		return self.get(key)

	def __contains__(self,key): #overloads the in operator so we can use in
		if self._get(key,self.root):
			return True
		else:
			return False

	def delete(self,key):
		if self.size >1:
			nodeToRemove = self._get(key,self.root)
			if nodeToRemove:
				self.remove(nodeToRemove)
				self.size-=1
			else:
				raise KeyError('Error when removing, key not found in tree')
		elif self.size ==1 and self.root.key==key:
			self.root=None
			self.size = self.size-1
		else:
			raise KeyError('Error when removing, key not found in tree')

	def __delitem__(self,key): #overloads the [] operator to allow us to delete nodes using the python dictionary way
		self.delete(key)

	def remove(self, currNode):
		if currNode.isLeaf():
			if currNode == currNode.parent.leftChild:
				currNode.parent.leftChild=None
			else:
				currNode.parent.rightChild=None
		elif currNode.hasBothChildren():
			succ=currNode.findSuccessor()
			succ.spliceOut()
			currNode.key=succ.key
			currNode.payload=succ.payload
		else: #node has one child
			if currNode.hasLeftChild():
				if currNode.isLeftChild():
					currNode.leftChild.parent=currNode.parent
					currNode.parent.leftChild=currNode.leftChild
				elif currNode.isRighChild():
					currNode.leftChild.parent=currNode.parent
					currNode.parent.rightChild=currNode.leftChild
				else:
					currNode.replaceNodeData(currNode.leftChild.key,currNode.leftChild.payload,currNode.leftChild.leftChild,currNode.leftChild.rightChild)
			else:
				if currNode.isLeftChild():
					currNode.rightChild.parent=currNode.parent
					currNode.parent.leftChild=currNode.rightChild
				elif currNode.isRighChild():
					currNode.rightChild.parent=currNode.parent
					currNode.parent.rightChild=currNode.rightChild
				else:
					currNode.replaceNodeData(currNode.rightChild.key,currNode.rightChild.payload,currNode.rightChild.left,currNode.rightChild.rightChild)






class TreeNode:
	def __init__(self,key,value,left=None,right=None,parent=None):
		self.key = key
		self.payload = value
		self.leftChild = left
		self.rightChild = right
		self.parent = parent

	def hasLeftChild(self):
		return self.leftChild

	def hasRightChild(self):
		return self.rightChild

	def isLeftChild(self):
		return self.parent and self.parent.leftChild == self

	def isRighChild(self):
		return self.parent and self.parent.rightChild == self

	def isRoot(self):
		return not self.parent

	def isLeaf(self):
		return not (self.rightChild or self.leftChild)

	def hasAnyChildren(self):
		return self.rightChild or self.leftChild

	def hasBothChildren(self):
		return self.rightChild and self.leftChild

	def replaceNodeData(self,key,value,lc,rc):
		self.key=key
		self.leftChild=lc
		self.rightChild=rc
		self.payload=value
		if self.hasLeftChild():
			self.leftChild.parent = self
		if self.hasRightChild():
			self.rightChild.parent=self

	def findSuccessor(self):
		succ=None
		if self.hasRightChild():
			succ = self.rightChild.findMin()
		else:
			if self.parent:
				if self.isLeftChild():
					succ=self.parent
				else:
					self.parent.rightChild=None
					succ = self.parent.findSuccessor()
					self.parent.rightChild=self
		return succ

	def findMin(self):
		current=self
		while current.hasLeftChild():
			current=current.leftChild
		return current

	def spliceOut(self):
		if self.isLeaf():
			if self.isLeftChild():
				self.parent.leftChild=None
			else:
				self.parent.rightChild=None
		elif self.hasAnyChildren():
			if self.hasLeftChild():
				if self.isLeftChild():
					self.parent.leftChild=self.leftChild
				else:
					self.parent.rightChild=self.leftChild
				self.leftChild.parent=self.parent
			else:
				if self.isLeftChild():
					self.parent.leftChild=self.rightChild
				else:
					self.parent.rightChild=self.rightChild
				self.rightChild.parent=self.parent

	def __iter__(self): #This overloads the 'for x in' , so we can traverse our tree inorder 
		if self:
			if self.hasLeftChild():
				for element in self.leftChild:
					yield element
			yield self.key
			if self.hasRightChild():
				for element in self.rightChild:
					yield element


myTree = BinarySearchTree()
myTree[15]="to"
myTree[3]="f12"
myTree[7]="press"
myTree[16]="help"
myTree[20]="ninetynine"
myTree[9]="airplane"
myTree[14]="timing"
myTree[22]="yes"
myTree[12]="no"
myTree[1]="maybe"
myTree[90]="match"

print("<------PRE------>")
myTree.Preorder(myTree.getRoot())
print("<------IN------>")
myTree.Inorder(myTree.getRoot())
print("<------POST------>")
myTree.Postorder(myTree.getRoot())
