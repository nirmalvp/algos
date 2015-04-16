from tree import Tree
from linkedlist import LinkedList
tree = Tree()
tree.create()

def createDepthLinkedList():
	nodesAtDepth = LinkedList()
	nodesAtDepth.insertNode(tree.root.data)
	q=[]
	q.append(tree.root)
	
	depthLinkedList =[nodesAtDepth]
	condition = True
	while condition:
		children = []
		while (q):
			node= q.pop(0)
			if(node.left != None):
				children.append(node.left)
			if(node.right != None):
				children.append(node.right)
		condition = True if children else False
		if(condition):
			nodesAtDepth = LinkedList()
			for node in children:
				nodesAtDepth.insertNode(node.data)
			depthLinkedList.append(nodesAtDepth)
			q.extend(children)
	for linkedlist in depthLinkedList:
		 linkedlist.display()

createDepthLinkedList()




