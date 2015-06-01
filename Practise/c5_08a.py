#8) Given the pre-order and in-order traverse list, write code to find the original tree
class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None


def printPostOrder(root):
	if root.left :
		printPostOrder(root.left)
	if root.right :
		printPostOrder(root.right)
	print root.data
		
	

def search(currentRoot, inOrder,subtreeStart) :
	for index, element in enumerate(inOrder,subtreeStart):
		if element == currentRoot :
			return index
	return -1

def buildTree(subtreeStart,subtreeEnd,inOrder,preOrder):
	if subtreeStart > subtreeEnd :
		return None
	global nextPreOrderIndex
	currentRoot = preOrder[nextPreOrderIndex]
	node = Node(currentRoot)
	nextPreOrderIndex += 1
	if subtreeStart == subtreeEnd:
		return node
	indexOfRootInorder = search(currentRoot,inOrder[subtreeStart:subtreeEnd + 1], subtreeStart)
	node.left = buildTree(subtreeStart, indexOfRootInorder-1, inOrder, preOrder)
	node.right = buildTree(indexOfRootInorder + 1, subtreeEnd, inOrder, preOrder)
	return node

nextPreOrderIndex = 0
def main():
	preOrder = [10,5,2,4,3,7,6,8,15,13,18,20]
	inOrder = [2,3,4,5,6,7,8,10,13,15,18,20]
	root = buildTree(0, len(preOrder)-1, inOrder, preOrder)
	printPostOrder(root)
main()


