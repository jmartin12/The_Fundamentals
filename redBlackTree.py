'''
Jacob Martin
3/10/2018

insert, delete,search, all O(log(n))

Red Black Tree - a binary search tree with one extra bit of storage per node -- color. Either red or black. The tree is guarenteed to be balanced.
			   - Each node contains the fields: color,key,left,right,and parent. If the child or parent DNE for a node, the corresponding pointer
			   points to a container value called the NilNode. Nilnode is always colored black. Nils always have black heighth of 0.

Properties:
	1.)Every Node is either red or Black
	2.)Every leaf (NIL) is Black
	3.)If a node is red, then both its children must be black
	4.)Every simple path from a node to a descendant leaf contains the same number of black nodes


<---------------Insertion-------------------->
In General, when we insert we may violate a RBT property. The main property that is violated is two consectutive reds, since new 
nodes ares red.
So we have to fix this by either A: recoloring, B: rotation, C: both

Consider x, a new node to be inserted.
	1.) Perform the normal BST Insertion with the exception that the color is red of the new node
	2.) if x = root, change color to black
	3.) If x != root or x.parent != black
		a.) if x.uncle  = red
			-> change color of parent and uncle as black
			-> change color of grandparent to red
			-> x=x.grandparent, repeat x 2-3 for every new x
		b.) if x.uncle = black
			i) uncle is black and x =left left (from grandparent)
			    -> Right Rotate on grandparent 
			    -> Swap colors of grandparent and parent
			ii) uncle black and x = left right (from grandparent)
				-> left rotate on parent
				->Apply case b.i 
			iii) uncle black and x = right right (from grandparent)
				-> left rotate on grandparent
				->swap colors of grandparent and parent
			iv) uncle black and x = right left (from grandparent)
				->right rotate on parent
				->apply case b.iii

	Finally, don't forget to recolor the root black (After the loop)



<------------DELETION--------------->
In delettion, the main property that is violated is the change of black hieghth in the tree. To check violations, we check the sibling.

Consider x node to be deleted, and y, x's replacement, and w, the sibling of x

	1.) Perform the normal BST delete. For this, we alwyas delete a leaf node (not the nil node, but an actual node with a key value). Because of
 	    this, we only need to handle cases where either a node is a leaf, or a node has one child. 
 	2.) If either x =red or y = red
		-> Mark replaced child as black.
	3.) If x = black and y= black , do the following while y != root and y = black
		i.) if w.child = red (any of them)
			->recolor w and w.child
			->rotate w
			->reassign w
		ii.) if w.color = black and w.children.color =black (both)
			->recolor w
			->y=y.parent
		iii.) w.color = black and w is left right or right left (from grandparent)
			->recolor w and w's child
			->rotate w
			->reassign w
		iiii.)w.color = black and w is left left or right right (from grandparent)
			->w.color= y.parent.color
			->recolor w's child, y.parent
			->rotate y.parent
			->x=root
	Finally, y.color = black  (After the loop)
'''


class Node:
	RED = True
	BLACK = False

	def __init__(self, key, color = RED):
		if not type(color) == bool:
			raise TypeError("Please enter a boolean for color. Red = True, Black = False")
		self.color = color
		self.key=key
		self.left = self.right=self.parent=NilNode.instance()


	def __str__(self, level=0,indent="   "):
		s = level*indent+str(self.key)
		if self.left:
			s=s+"\n"+self.left.__str__(level+1,indent)
		if self.right:
			s=s+"\n"+self.right.__str__(level+1,indent)
		return s

	def __nonzero__(self):
		return True

	def __bool__(self):
		return True

class NilNode(Node): #inherits node
	__instance__=None

	@classmethod
	def instance(self):
		if self.__instance__ is None:
			self.__instance__=NilNode()
		return self.__instance__

	def __init__(self):
		self.color=Node.BLACK
		self.key=None
		self.left=self.right=self.parent=None

	def __nonzero__(self):
		return False

	def __bool__(self):
		return False


class RedBlackTree:
	def __init__(self):
		self.root = NilNode.instance()
		self.size=0

	def __str__(self):
		return("(root.size = %d)\n" % self.size) + str(self.root)

	def add(self,key):
		self.insert(Node(key))

	def insert(self,x):
		self.__insert_helper(x)

		x.color=Node.RED
		while x!=self.root and x.parent.color == Node.RED:
			if x.parent == x.parent.parent.left:
				y=x.parent.parent.right #uncle
				if y and y.color == Node.RED: 
					x.parent.color = Node.BLACK
					y.color = Node.BLACK
					x.parent.parent.color = Node.RED
					x = x.parent.parent
				else:
					if x==x.parent.right: 
						x=x.parent
						self.__left_rotate(x)
					x.parent.color=Node.BLACK
					x.parent.parent.color=Node.RED
					self.__right_rotate(x.parent.parent)
			else:
				y=x.parent.parent.left #uncle
				if y and y.color==Node.RED: 
					x.parent.color = Node.BLACK
					y.color=Node.BLACK
					x.parent.parent.color=Node.RED
					x=x.parent.parent
				else:
					if x==x.parent.left:
						x=x.parent
						self.__right_rotate(x)
					x.parent.color=Node.BLACK
					x.parent.parent.color=Node.RED
					self.__left_rotate(x.parent.parent)
		self.root.color=Node.BLACK


	def __insert_helper(self,z):
		y=NilNode.instance()
		x=self.root
		while x:
			y=x
			if z.key<x.key:
				x=x.left
			else:
				x=x.right

		z.parent=y
		if not y:
			self.root=z
		else:
			if z.key<y.key:
				y.left=z
			else:
				y.right=z
		self.size+=1

	def __left_rotate(self,x):
		if not x.right:
			raise "x.right is nil"
		y=x.right
		x.right=y.left
		if y.left:
			y.left.parent=x
		y.parent=x.parent
		if not x.parent:
			self.root=y
		else:
			if x==x.parent.left:
				x.parent.left=y
			else:
				x.parent.right=y
		y.left =x
		x.parent=y

	def __right_rotate(self,x):
		if not x.left:
			raise "x.left is nil"
		y=x.left
		x.left=y.right
		if y.right:
			y.right.parent=x
		y.parent=x.parent
		if not x.parent:
			self.root=y
		else:
			if x==x.parent.left:
				x.parent.left=y
			else:
				x.parent.right=y
		y.right=x
		x.parent=y

	def successor(self,x):
		if x.right:
			return self.minimum(x.right)
		y=x.parent
		while y and x==y.right:
			x=y
			y=y.parent
		return y

	def minimum(self,x=None):
		if x is None:
			x=self.root
		while x.left:
			x=x.left
		return x

	def search(self,key,x=None):
		if x is None:
			x= self.root
		while x and x.key != key:
			if key<x.key:
				x=x.left
			else:
				x=x.right
		return x



	def delete(self,z):
		if not z.left or not z.right:
			y=z
		else:
			y=self.successor(z)
		if not y.left:
			x=y.right
		else:
			x=y.left
		x.parent=y.parent

		if not y.parent:
			self.root=x
		else:
			if y==y.parent.left:
				y.parent.left=x
			else:
				y.parent.right=x

		if y!=z:
			z.key=y.key

		if y.color ==Node.BLACK:
			self.__delete_fixup(x)

		self.size-=1
		return y

	def __delete_fixup(self,x):
		while x!= self.root and x.color == Node.BLACK:
			if x==x.parent.left:
				w=x.parent.right #sibling
				if w.color == Node.RED:
					w.color=Node.BLACK
					x.parent.color=Node.RED
					self.__left_rotate(x.parent)
					w=x.parent.right
				if w.left.color==Node.BLACK and w.right.color==Node.BLACK:
					w.color=Node.RED
					x=x.parent
				else:
					if w.right.color==Node.BLACK:
						w.left.color=Node.BLACK
						w.color = Node.RED
						self.__right_rotate(w)
						w=x.parent.right
					w.color = x.parent.color
					x.parent.color=Node.BLACK
					w.right.color=Node.BLACK
					self.__left_rotate(x.parent)
					x=self.root
			else:
				w=x.parent.left #sibling
				if w.color==Node.RED:
					w.color=Node.BLACK
					x.parent.color=Node.RED
					self.__right_rotate(x.parent)
					w=x.parent.left
				if w.right.color==Node.BLACK and w.left.color ==Node.BLACK:
					w.color=Node.RED
					x=x.parent
				else:
					if w.left.color==Node.BLACK:
						w.right.color=Node.BLACK
						w.color=Node.RED
						self.__left_rotate(w)
						w=x.parent.left
					w.color=x.parent.color
					x.parent.color=Node.BLACK
					w.left.color=Node.BLACK
					self.__right_rotate(x.parent)
					x=self.root
		x.color=Node.BLACK






def main():
	rbt = RedBlackTree()
	rbt.add(10)
	rbt.add(3)
	rbt.add(7)
	rbt.add(4)
	rbt.add(20)
	rbt.add(15)
	rbt.add(100)
	rbt.add(1)
	print(rbt)

	#rbt.delete(rbt.search(7))
	rbt.delete(rbt.search(10))
	#rbt.delete(rbt.search(3))
	rbt.delete(rbt.search(4))
	rbt.delete(rbt.search(20))
	#rbt.delete(rbt.search(15))
	rbt.delete(rbt.search(100))
	#rbt.delete(rbt.search(1))
	print(rbt)

if __name__=="__main__":
	main()


