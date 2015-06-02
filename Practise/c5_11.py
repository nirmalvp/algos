#11) Given a sorted (increasing order) array, write an algorithm to create a balanced binary search tree
import c5_10
from c5_01 import Node

def createBalancedBST(arrayOfNodeElements,start,end):
	#Recursion : FInd the mid element,make it the root. This creates two sorted arrays on either sides. Repeat the process
	if start > end :
		return None
	middleElement = (start + end) / 2
	node = Node(arrayOfNodeElements[middleElement])
	node.left = createBalancedBST(arrayOfNodeElements,start,middleElement-1)
	node.right = createBalancedBST(arrayOfNodeElements,middleElement + 1, end)
	return node

def main():
	arrayOfNodeElements = map(int, raw_input("Enter the elements of the increasing array").split())
	root = createBalancedBST(arrayOfNodeElements,0,len(arrayOfNodeElements)-1)
	print c5_10.isBalanced(root)
main()

