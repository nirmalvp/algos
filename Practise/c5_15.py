#15) You have two very large binary trees: T1, with millions of nodes, and T2, with hundreds
        # of nodes. Create an algorithm to decide if T2 is a subtree of T1.

#Alternate method. Find the node containing the root of subtree in supertree. Traverse both the list together and check if the 
#elements are the same
from c5_01 import BinaryTree
def storeInorder(root,traversalStorage):
	if root.left :
		storeInorder(root.left,traversalStorage)
	traversalStorage.append(str(root.data))
	if root.right:
		storeInorder(root.right,traversalStorage)

def storePreorder(root,traversalStorage):
	traversalStorage.append(str(root.data))
	if root.left :
		storePreorder(root.left, traversalStorage)
	if root.right:
		storePreorder(root.right, traversalStorage)

def isSubset(treeSuper, treeSub):
	treeSubInorderTraversal = list()
	treeSuperInorderTraversal = list()
	storeInorder(treeSub.root,treeSubInorderTraversal) #treeSubInorderTraversal contains inorder traversal of subtree
	storeInorder(treeSuper.root,treeSuperInorderTraversal) #treeSuperInorderTraversal contains inorder traversal of supertree
	convertListToString = lambda aList : " ".join(aList) 
	#If both inorder and preorder traversals of supertree contains inorder and preorder trav of subtree,then they are subsetfb
	if convertListToString(treeSubInorderTraversal) in convertListToString(treeSuperInorderTraversal) :
		treeSubPreorderTraversal = list()
		treeSuperPreorderTraversal = list()
		storePreorder(treeSub.root,treeSubPreorderTraversal)
		storePreorder(treeSuper.root,treeSuperPreorderTraversal)
		return convertListToString(treeSubPreorderTraversal) in convertListToString(treeSuperPreorderTraversal) 
	return False

def main():
	treeSuper = BinaryTree()
	treeSub = BinaryTree()
	print isSubset(treeSuper,treeSub)

main()


