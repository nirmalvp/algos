#4) How do you find out the fifth maximum element in an Binary Search Tree in efficient manner. in BinarySearchTree.select()
      # Note: You should not use use any extra space. 
#i.e sorting Binary Search Tree and storing the results in an array and listing out the fifth element

from c5_01 import BinaryTree
def findKthElement(node,k):
	stack = list()
	count = 0
	stack.append(node)
	while node.right:
		node = node.right
		stack.append(node)
	while stack:
		node = stack.pop()
		count +=1
		if count == k :
			return node.data
		if node.left:
			node = node.left
			stack.append(node)
			while node.right:
				node = node.right
				stack.append(node)

def main():
	tree = BinaryTree()
	print findKthElement(tree.root,4)
main()
