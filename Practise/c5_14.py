# 14) Design an algorithm and write code to find the first common ancestor of two nodes
#        in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
#        necessarily a binary search tree

from c5_01 import BinaryTree

def findLCA(root,node1Data,node2Data):
	if root is None:
		return None
	if root.data == node1Data or root.data == node2Data : #If either of the nodedata is the root elem,return root
		return root 
	nodeIfPresentInLeftSubtree = findLCA(root.left,node1Data, node2Data) # IS either nodeData present in left subtree
	nodeIfPresentInRighttSubtree = findLCA(root.right,node1Data, node2Data) #IS either nodeData present in right subtree
	if nodeIfPresentInLeftSubtree and nodeIfPresentInRighttSubtree : # If the node data are in different subtress,their root is
	#the LCA
		return root
	#If both elements are in the same subtree,return the subtree which contains both the nodes	
	return nodeIfPresentInLeftSubtree if nodeIfPresentInLeftSubtree else nodeIfPresentInRighttSubtree

def main():
	bst = BinaryTree()
	commonAncestor = findLCA(bst.root,input("Enter node1 "),input("enter node 2"))
	print commonAncestor.data
main()










