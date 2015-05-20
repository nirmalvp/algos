#69) Given a stream of integer,
# design and implement a data structure tracking the rank of integers.
#It have 2 methods: track(int n) is called when generate a new integer n,
# and rank(int n) return how many integers in the stream is smaller than n.

class Node(object):
	def __init__(self,item):
		self.item = item
		self.left = None
		self.right = None
		self.repetition = 1 # Number of times the same item exist in the list
		self.lesserCount = 0

class ModifiedBST(object):
	def __init__(self):
		self.root = None
	def track(self,number):
		node = Node(number)
		if not self.root:
			self.root = node
			return
		temp = self.root
		while temp :
			if number == temp.item :
				temp.repetition += 1 #If number already present in the bst, increment the repetition count
				return
			parent = temp
			if number < temp.item :
				temp.lesserCount += 1 # If the new number is less than the node, increment the count of elements
				#lesser than the node
				temp = temp.left
			else :
				temp = temp.right
		if number < parent.item :
			parent.left = node
		else :
			parent.right = node
	
	def getRank(self,number):
		temp = self.root
		rank = 0
		while number != temp.item :
			if number > temp.item: # When we go to the right subtree of a node, all the elements lesser than the node
			# and the node itself, is lesser than the number we are quering for 
				rank += (temp.lesserCount + temp.repetition)
				temp = temp.right
			else :
				temp = temp.left
		#When the number is found, all elements in its left subtree are lesser than it.
		rank += temp.lesserCount
		return rank
def main():
	bst = ModifiedBST()
	array = map(int,raw_input("Enter the elements").split())
	for element in array:
		bst.track(element)
	for element in array:
		print "Element = %s , Rank = %s"%(element, bst.getRank(element))
main()











