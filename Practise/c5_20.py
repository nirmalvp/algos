 #20) Write code to create a mirroring of a binary tree
from c5_01 import BinaryTree
def mirrorTree(node):
	if node is None:
		return
	leftSubtreeMirror = mirrorTree(node.left)
	rightSubtreeMirror = mirrorTree(node.right)
	node.left = rightSubtreeMirror
	node.right = leftSubtreeMirror
	return node

def main():
	tree = BinaryTree()
	tree.visitPreorder()
 	tree.root=mirrorTree(tree.root)
 	tree.visitPreorder()
main()
