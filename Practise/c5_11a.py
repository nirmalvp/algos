#11A)Given a sorted (increasing order) linkedlist, write an algorithm to create a balanced binary search tree.
from c3_linkedlist import LinkedList
from c5_01 import Node
import c5_10
first = None

def createBalancedBST(start,end):
	#Bottom-up recursion : Find the middle of the linkedlist. That is the parent index.
	#From every parent, first build the left subtree. This ensures that we can use the elements in
	#sequential order from the linked list. After the left subtree, next elem from linkedlist is the parent itself
	#and then use the elements to the right to build the right subtree
	global first
	if start > end :
		return None
	middle = (start + end) / 2
	leftChild = createBalancedBST(start,middle-1)
	parent = Node(first.data)
	first = first.next
	rightChild = createBalancedBST(middle+1,end)
	parent.left = leftChild
	parent.right = rightChild
	return parent

def main():
	linkedlist = LinkedList()
	length = 0
	for element in map(int,raw_input("Enter the elements of the increasing array").split()) :
		linkedlist.insert(element)
		length +=1
	global first
	first = linkedlist.first
	root = createBalancedBST(0,length-1)
	print c5_10.isBalanced(root)
main()


	
