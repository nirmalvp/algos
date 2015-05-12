class Node(object):
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList(object):
	def __init__(self):
		self.first = None
	def __iter__(self):
		currentElement = self.first
		while currentElement:
			yield currentElement.data
			currentElement = currentElement.next
	
	def insert(self,data):
		node = Node(data)
		if self.first == None:
			self.first = node
			return
		temp = self.first
		while temp.next:
			temp = temp.next
		temp.next = node
	def show(self):
		currentElement = self.first
		while currentElement:
			print "%s "%currentElement.data,
			currentElement = currentElement.next
		print
	


