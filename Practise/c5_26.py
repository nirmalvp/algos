#26) Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).  [LeetCode]       
#        For example, this binary tree is symmetric:        
#            1
#           / \
#          2   2
#         / \ / \
#        3  4 4  3
#        But the following is not:
#            1
#           / \
#          2   2
#           \   \
#           3    3
from c5_01 import BinaryTree
def isMirrorEqual(leftSubtree,rightSubtree):
    if leftSubtree is None or rightSubtree is None:
        return leftSubtree is None and rightSubtree is None
    # If they are both None, they are mirrors, but if one is None and the other is not, they are not equal
    if leftSubtree.data != rightSubtree.data :
        return False
    return isMirrorEqual(leftSubtree.left, rightSubtree.right) and isMirrorEqual(leftSubtree.right, rightSubtree.left)

def main():
    tree = BinaryTree()
    print isMirrorEqual(tree.root.left, tree.root.right)

main()
