class Node:
	def __init__(self,data):
		self.data=data
		self.next = None

class Queue():
	def __init__(self):
		self.first=None
		self.last=None
	def enqueue(self,data):
		node = Node(data)
		if (self.first == None):
			self.first = self.last = node
		else :
			self.last.next = node
			self.last = node

	def dequeue(self):
		if(self.first == None):
			print "Empty Q"
			return
		item = self.first.data
		self.first = self.first.next
		return item
