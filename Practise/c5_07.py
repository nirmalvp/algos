 #7) Given a BinarySearchTree and value K, find all value pairs whose sum is K in O(n).
from c5_01 import BinaryTree
def getNextSmallerNum(node, greaterToSmaller):
	if node.left :
		node = node.left
		greaterToSmaller.append(node)
		while node.right:
			node = node.right
			greaterToSmaller.append(node)
	return greaterToSmaller.pop()

def getNextBiggerNum(node, smallerToGreater):
	if node.right :
		node = node.right
		smallerToGreater.append(node)
	while node.left:
		node = node.left
		smallerToGreater.append(node)
	return smallerToGreater.pop()


def findSumPairs(root,requiredSum):
 	smallerToGreater = list()
 	greaterToSmaller = list()
 	smallerToGreater.append(root)
 	greaterToSmaller.append(root)
 	node = root
 	while node.left:
 		node=node.left
 		smallerToGreater.append(node)
 	node = root
 	while node.right:
 		node = node.right
 		greaterToSmaller.append(node)
 	smallElement = smallerToGreater.pop()
 	bigElement = greaterToSmaller.pop()
 	while smallElement.data < bigElement.data :
 		if smallElement.data + bigElement.data == requiredSum :
 			yield (smallElement.data, bigElement.data)
 			bigElement = getNextSmallerNum(bigElement,greaterToSmaller)
 			smallElement = getNextBiggerNum(smallElement,smallerToGreater)
 		if smallElement.data + bigElement.data > requiredSum :
 			bigElement = getNextSmallerNum(bigElement,greaterToSmaller) 
 		if smallElement.data + bigElement.data < requiredSum :
 			smallElement = getNextBiggerNum(smallElement,smallerToGreater)
def main():
	tree = BinaryTree()
	print list(findSumPairs(tree.root,10))

main()

