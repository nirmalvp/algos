class Node(object):
	def __init__(self,data):
		self.data = data
		self.next = None

class Stack(object):
	def __init__(self):
		self.top = None
		
	def push(self,data):
		node = Node(data)
		if self.top is None:
			self.top = node
			return
		node.next = self.top
		self.top = node
		
	def pop(self):
		if self.top is None:
			print "Stack UnderFlow"
			return
		temp = self.top
		self.top = self.top.next
		return temp.data