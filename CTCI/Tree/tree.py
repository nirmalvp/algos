class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

class Tree :
	
	def __init__(self):
		self.root = None

	def create(self):
		if(self.root == None):
			userInput = int(raw_input("Enter the root element"))
			node=Node(userInput)
			self.root = node
		else:
			userInput = int(raw_input())
			node=Node(userInput)
		
		isLeft = raw_input("Does %s have a left child ? y or y"%userInput)
		if(isLeft=="y"):
			print "Enter the left child of %s"%userInput,
			node.left = self.create()
		
		isRight = raw_input("Does %s have a right child ? Y or N"%userInput)
		if(isRight=="y"):
			print "Enter the right child of %s"%userInput,
			node.right = self.create()
		return node

	def printInorder(self,node=None):
		if(node==None):
			node = self.root
		print "%s\t"%(node.data)
		if(node.left != None):
			print "%s's left child : "%node.data,
			self.printInorder(node.left)
		if(node.right != None):
			print "%s's right child : "%node.data,
			self.printInorder(node.right)

