from c5_01 import BinaryTree
#5) Given a binary tree, programmatically you need to prove it is a binary search tree

#For a binary search tree, if we perform inorder traversal, it will be a ascending order sorted array
def checkTreeIfBST(node):
	stack = list()
	stack.append(node)
	lastElementVisited = None
	while node.left:
		node = node.left
		stack.append(node)
	while stack:
		node = stack.pop()
		if lastElementVisited is not None and lastElementVisited > node.data :
			#If not in ascending order,it is not a BST
			return False
		lastElementVisited = node.data
		if node.right:
			node = node.right
			stack.append(node)
			while node.left:
				node = node.left
				stack.append(node)
	return True

def main():
	tree = BinaryTree()
	print checkTreeIfBST(tree.root)
main()

