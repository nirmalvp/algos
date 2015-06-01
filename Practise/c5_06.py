#6) Given two binary trees, write a compare function to check if they are equal or not.
#       Being equal means that they have the same value and same structure.
from c5_01 import BinaryTree
def isTreesEqual(rootOne,rootTwo):
	if rootOne is None and rootTwo is None:
		return True
	elif rootOne is None : # Only one tree is none
		return False
	elif rootTwo is None:
		return False
	if rootOne.data != rootTwo.data : # If data unequal, the trees are not same
		return False
	#If Both the left and right trees of both the trees are equal, the trees are equal
	return isTreesEqual(rootOne.left,rootTwo.left) and isTreesEqual(rootOne.right,rootTwo.right)

def main():
	print "Input the Elements of the first tree"
	treeOne = BinaryTree()
	print "Input the Elements of the second tree"
	treeTwo = BinaryTree()
	if isTreesEqual(treeOne.root, treeTwo.root):
		print "The two trees are equal"
	else :
		print "The two trees are unequal"
main()