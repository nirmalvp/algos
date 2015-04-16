class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
class Stack():
	def __init__(self):
		self.top = None
	def push(self,data):
		node = Node(data)
		if(self.top == None):
			self.top = node
		else:
			node.next = self.top
			self.top = node
	def pop(self):
		if (self.top == None):
			return
		item = self.top.data
		self.top = self.top.next
		return item

class Queue:
	def __init__(self):
		self.insertStack =Stack()
		self.retreiveStack = Stack()
	def enqueue(self,data):
		self.insertStack.push(data)

	def dequeue(self):
		if(self.retreiveStack.top == None):
			while(self.insertStack.top != None):
				self.retreiveStack.push(self.insertStack.pop())
		return self.retreiveStack.pop() 

q =Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print q.dequeue()
print q.dequeue()
q.enqueue(4)
q.enqueue(5)
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
