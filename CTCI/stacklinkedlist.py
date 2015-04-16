class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class Stack:
	def __init__(self):
		self.top = None

	def push(self,data):
		node = Node(data)
		if(self.top==None):
			self.top = node
		else :
			node.next = self.top
			self.top = node

	def pop(self):
		if(self.top == None):
			print "Nothing to pop "
			return
		item = self.top.data
		self.top = self.top.next
		return item

