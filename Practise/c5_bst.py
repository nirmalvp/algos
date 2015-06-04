class Node(object) :
	def __init__(self, data):
		self.data = data
		self.parent = None
		self.left = None
		self.right = None


class BST(object):
	def __init__(self):
		self.root = None

	def insert(self, data):
		node = Node(data)
		if self.root is None :
			self.root = node
			return
		current = self.root
		while current:
			parent = current
			if data < current.data:
				current = current.left
			else :
				current = current.right
		if data < parent.data :
			parent.left = node
		else:
			parent.right = node
		node.parent = parent
