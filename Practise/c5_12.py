
from c5_bst import BST 
def findNodeContainingData(bst,data):
	current = bst.root
	while current:
		if data == current.data :
			return current
		if data < current.data :
			current = current.left
		else:
			current = current.right

def inorderSuccessor(bst,data):
	node = findNodeContainingData(bst,data)
	if not node:
		print "Element not found in the BST"
		return
	current = node
	if current.right :
		current = current.right
		while current.left:
			current = current.left
		return current.data
	else : 
		parent = current.parent
		if parent and current == parent.left : # If it is a left child, parent is the inorder succ
			return parent.data
		while parent and current == parent.right: # If it is right child, go up the tree,
		#till we find a parent that has left child, parent is the inorder succ
			current = parent
			parent = parent.parent
		return parent.data if parent else None

def main():
	bst = BST()
	for element in map(int,raw_input("Enter the elements of bst").split()) :
		bst.insert(element)
	searchElem = input(" Input the element to find in-order successor : ")
	successor = inorderSuccessor(bst,searchElem)
	if successor is not None:
		print successor
	else :
		print "No successor" 
main()
