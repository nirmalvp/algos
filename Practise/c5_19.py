from c5_01 import BinaryTree
def depth(node):
	if node is None:
		return 0
	return max(depth(node.left), depth(node.right)) + 1


def findDiameter(node):
	if node is None:
		return 0
	leftTreeHeight = depth(node.left)
	rightTreeHeight = depth(node.right)
	return max(leftTreeHeight + rightTreeHeight + 1, findDiameter(node.left), findDiameter(node.right))

def main() :
	tree= BinaryTree()
	print findDiameter(tree.root)

main()


