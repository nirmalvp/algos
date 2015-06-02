#10) Implement a function to check if a tree is balanced. For the purposes of this question,
#        a balanced tree is defined to be a tree such that no two leaf nodes differ in distance
#        from the root by more than one.

from c5_01 import BinaryTree
def memoize(f):
	memo = dict()
	def wrapper(node):
		if memo.get(node) is None :
			memo[node] = f(node)
		return memo[node]
	return wrapper

@memoize	
def depth(node):
	if node is None:
		return 0
	return max(depth(node.left), depth(node.right)) + 1

@memoize
def isBalanced(node):
	if node is None:
		return True
	if abs(depth(node.left) - depth(node.right)) > 1 :
		print node.data,"error"
		return False
	if not isBalanced(node.left) or not isBalanced(node.right):
		return False
	return True

def main():
	tree = BinaryTree()
	print isBalanced(tree.root)
if __name__ == "__main__":
	main()


