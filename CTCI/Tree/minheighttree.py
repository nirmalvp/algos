from tree import Tree,Node
treeElements = map(int, raw_input("Enter sorted list").split())
tree = Tree()

def createMinTree(low,high):
	if(low>high):
		return
	mid = (low + high)/2
	data = treeElements[mid]
	node = Node(data)
	node.left = createMinTree(low,mid-1)
	node.right = createMinTree(mid+1,high)
	return node

tree.root = createMinTree(0,len(treeElements)-1)
tree.printInorder()

