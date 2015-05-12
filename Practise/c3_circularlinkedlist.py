class Node(object):
	def __init__(self,data):
		self.data = data
		self.next = None

class CircularLinkedList(object):
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
			node.next = self.first
			return
		temp = self.first
		while temp.next != self.first:
			temp = temp.next
		node.next = self.first
		temp.next = node

	def show(self):
		currentElement = self.first
		while currentElement.next != self.first :
			print "%s "%currentElement.data,
			currentElement = currentElement.next
		print currentElement.data
	


