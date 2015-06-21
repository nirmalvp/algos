#1) How would you design a stack which, in addition to push and pop, also has a function
      # min which returns the minimum element? Push, pop and min should all operate in
      # O(1) time.

class Node(object):
	def __init__(self,data,minTillNow):
		self.data = data
		self.next = None
		self.minTillNow = minTillNow

class Stack(object):
	def __init__(self):
		self.top = None
		self._minimumElement = None

	def push(self,data):
		if self._minimumElement is None or data < self._minimumElement :
			self._minimumElement = data
		node = Node(data, self._minimumElement)
		if self.top is None:
			self.top = node
			return
		node.next = self.top
		self.top = node
		
	def pop(self):
		if self.top is None:
			print "Stack UnderFlow"
			return
		temp = self.top
		self.top = self.top.next
		return temp.data
	
	def topElement(self):
		return self.top.data

	def showMinElement(self):
		return self.top.minTillNow

def main():
	stack = Stack()
	stack.push(10)
	stack.push(6)
	stack.push(8)
	stack.push(3)
	stack.push(5)
	stack.push(2)
	print stack.topElement()
	print stack.showMinElement()
	stack.pop()
	print stack.topElement()
	print stack.showMinElement()
main()

