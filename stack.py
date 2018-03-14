'''
Jacob Martin
Created 3/9/2018

Stack data structure -- First in Last Out
Note - top is at the beginning, instead of the end so we can use list methods append and pop
'''


class Stack:
	def __init__(self):
		self.items=[]

	def isEmpty(self):
		return self.items == []

	def push(self,item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)


myStack = Stack()
print(myStack.isEmpty())
myStack.push(1)
print(myStack.isEmpty())
myStack.push(2)
print(myStack.peek())
myStack.push('yes')
print(myStack.peek())
print(myStack.size())
myStack.pop()
print(myStack.size())
