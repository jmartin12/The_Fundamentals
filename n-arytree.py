'''
Jacob Martin
3/9/2018

N-ary tree is a tree like structure that can have any limit of children at any level 
'''


class Node(object):
	def __init__(self,key):
		self.key=key
		self.child=[]


def printTreeLevelWise(root):
	if root is None:
		return
	queue=[]
	queue.append(root)

	while len(queue)>0:
		n=len(queue)
	#while len(queue) > 0:
		p=queue[0]
		queue.pop(0)
		print(p.key)
		for index, value in enumerate(p.child):
			queue.append(value)
			n-=1
			print("")
	







root = Node(1)
root.child.append(Node(2))
root.child.append(Node(32))
root.child.append(Node(56))
root.child[2].child.append(Node(1))
root.child[2].child.append(Node(45))
root.child[2].child.append(Node(66))
printTreeLevelWise(root)




