#8) Given the pre-order and in-order traverse list, write code to find the post-order
#http://www.geeksforgeeks.org/print-postorder-from-given-inorder-and-preorder-traversals/
def search(rootElement,inorder):
	for index,element in enumerate(inorder):
		if element == rootElement:
			return index
	return -1

def printPostOrder(inorder,preorder,length):
	rootElement = preorder[0]
	rootIndexInInorder = search(rootElement,inorder)
	if rootIndexInInorder != 0 :
		printPostOrder(inorder[:rootIndexInInorder],preorder[1:],rootIndexInInorder)
	if rootIndexInInorder!=length-1 :
		printPostOrder(inorder[rootIndexInInorder+1:],preorder[rootIndexInInorder+1:],length - rootIndexInInorder - 1)
	print rootElement,

def main():
	inorder = [4, 2, 5, 1, 3, 6]
	preorder = [1, 2, 4, 5, 3, 6]
	printPostOrder(inorder,preorder,len(preorder))
main()
