class Node:
	def __init__(self,data):
		self.data = data
		self.minSoFar = None
		self.next =None

class Stack:
	def __init__(self):
		self.top = None

	def push(self,data):
		node =Node(data)
		if(self.top==None):
			node.minSoFar = node.data
			self.top = node
		else :
			node.minSoFar = node.data if node.data < self.top.minSoFar else self.top.minSoFar
			node.next = self.top
			self.top = node

	def pop(self):
		if(self.top==None):
			return 
		item = self.top.data
		self.top = self.top.next
		return item

	def minElement(self):
		if (self.top ==None):
			return
		return self.top.minSoFar

s= Stack()
s.push(5)
print s.minElement()
s.push(7)
print s.minElement()
s.push(6)
print s.minElement()
s.push(3)
print s.minElement()
s.push(9)
print s.minElement()
