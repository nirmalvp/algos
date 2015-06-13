#16) You are given a binary tree in which each node contains a value. Design an algorithm
       # to print all paths which sum up to that value. Note that it can be any path in the tree
        #- it does not have to start at the root.
from c5_01 import BinaryTree
def findPathToSum(node,requiredSum) :
	if node is None:
		return
	if node.data == requiredSum :
		yield (node.data, )
	else:
		for path in findPathToSum(node.left, requiredSum - node.data):
			yield (node.data,) + path
		for path in findPathToSum(node.right, requiredSum - node.data):
			yield (node.data,) + path
		for path in findPathToSum(node.left, requiredSum):
			yield path
		for path in findPathToSum(node.right, requiredSum):
			yield path

def main():
	tree= BinaryTree()
	requiredSum = input("Enter the required Sum : ")
	print list(findPathToSum(tree.root, requiredSum))
main()



