#17) Write a method to transfer a BinarySearchTree to a sorted LinkedList without using extra space.
from c3_linkedlist import LinkedList
from c5_bst import BST

def bstToLinkedList(node,linkedlist):
	if node.left :
		bstToLinkedList(node.left,linkedlist)
	linkedlist.insert(node.data)
	if node.right :
		bstToLinkedList(node.right,linkedlist)

def main():
	bst = BST()
	for element in map(int,raw_input("Enter elements of the bst").split()):
		bst.insert(element)
	linkedlist = LinkedList()
	bstToLinkedList(bst.root,linkedlist)
	linkedlist.show()

main()

