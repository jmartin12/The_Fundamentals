'''
Jacob Martin
Created 3/9/2018

Queue data structure -- First in First Out
'''

class Queue:
	def __init__(self):
		self.items =  []

	def isEmpty(self):
		return self.items==[]
	def enqueue(self,item):
		self.items.insert(0,item)
	def dequeue(self):
		self.items.pop()
	def size(self):
		return len(self.items)


myQ = Queue()
print(myQ.isEmpty())
myQ.enqueue(1)
myQ.enqueue(2)
print(myQ.size())
myQ.dequeue()
print(myQ.size())
print(myQ.isEmpty())