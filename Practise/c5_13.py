

from c3_linkedlist import LinkedList
from c5_bst import BST

def findNodesAtEachDepth(root):
	queue = []
	children = []
	childrenList = LinkedList()
	childrenList.insert(root.data)
	queue.append(root)
	while queue or children : 
		yield childrenList
		childrenList = LinkedList()
		children = list()
		while queue :
			current = queue.pop(0)
			if current.left :
				children.append(current.left)
				childrenList.insert(current.left.data)
			if current.right :
				children.append(current.right)
				childrenList.insert(current.right.data)
		queue = list(children)

def main():
	bst = BST()
	for element in map(int,raw_input("Enter the elements of bst").split()) :
		bst.insert(element)
	for depth,childrenList in enumerate(findNodesAtEachDepth(bst.root)):
		print "Depth %s :"%depth,
		childrenList.show()
main()

