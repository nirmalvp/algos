#1) Create a binary-tree datastructure, having pre-order, in-order, and post-order traverse.
class Node(object):
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

class BinaryTree(object):
	def __init__(self):
		self.root = self.createSubtree()
	
	def createSubtree(self,parent=None,childPosition=None):
		if parent is not None:
			data = input("Enter the %s child of %s"%(childPosition,parent))
		else:
			data = input("Enter the root element")
		node = Node(data)
		if raw_input("Does %s has a left child : Y or N"%data).upper() == "Y":
			node.left = self.createSubtree(data,"left")
		if raw_input("Does %s has a right child : Y or N"%data).upper() == "Y":
			node.right = self.createSubtree(data,"right")
		return node

	def visitPreorder(self,node=None):
		if not self.root :
			print "Empty Tree"
			return
		if not node:
			node = self.root
		print "%s ---> "%node.data,
		if node.left: 
			self.visitPreorder(node.left)
		if node.right:
			self.visitPreorder(node.right)
		if node == self.root:
			print #Leaving a blank after the entire preorder is over

	def visitInorder(self,node=None):
		if not self.root :
			print "Empty Tree"
			return
		if not node:
			node = self.root
		if node.left :
			self.visitInorder(node.left)
		print "%s ---> "%node.data,
		if node.right:
			self.visitInorder(node.right)
		if node == self.root:
			print 

	def visitPostorder(self,node=None):
		if not self.root :
			print "Empty Tree"
			return
		if not node:
			node = self.root
		if node.left :
			self.visitPostorder(node.left)
		if node.right:
			self.visitPostorder(node.right)
		print "%s ---> "%node.data,
		if node == self.root:
			print 

def main():
	tree = BinaryTree()
	print "in-order"
	tree.visitInorder()
	print "pre-order"
	tree.visitPreorder()
	print "post-order"
	tree.visitPostorder()
if __name__ == "__main__":
	main()


	








