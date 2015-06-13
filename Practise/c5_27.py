#27)Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.
#       For example, Given n = 3, your program should return all 5 unique BST's shown below.
#       
#          1         3     3      2      1                      3               3
#           \       /     /      / \      \                    /  \
#            3     2     1      1   3      2                  2    5
#           /     /       \                 \                /    /
#          2     1         2                 3              1    4
from c5_01 import Node
def preorder(node, parent, dir):
	print "%s %s of %s"%(node.data,dir,parent)
	if node.left:
		preorder(node.left,node.data,"left")
	if node.right:
		preorder(node.right, node.data,"right")

def createBSTWithElementsInRange(low,high):
	if low > high :
		yield None
		#Empty Subtree
	else:
		for number in xrange(low, high + 1):
			for leftTree in createBSTWithElementsInRange(low, number-1): 
				# Leftree can only have numbers less than the current node
				for rightTree in createBSTWithElementsInRange(number+1, high):
					#Right tree can only have numbers greater than the current node
					node = Node(number)
					node.left = leftTree
					node.right = rightTree
					yield node
def main():
	n = input("Enter n , the max num in bst : ")
	for tree in createBSTWithElementsInRange(1,n):
		preorder(tree,None, "root")
		print "*" * 25
main()


