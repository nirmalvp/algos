#5) Imagine a (literal) stack of plates. If the stack gets too high, it might topple. There-
       #fore, in real life, we would likely start a new stack when the previous stack exceeds
       #some threshold. Implement a data structure SetOfStacks that mimics this. SetOf-
       #Stacks should be composed of several stacks, and should create a new stack once
       #the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should
       #behave identically to a single stack (that is, pop() should return the same values as it
       #would if there were just a single stack).
class Stack(object):
	MAX_SIZE = 3
	def __init__(self):
		self.data = list()
		self.next = None
	def isFull(self):
		return len(self.data) == Stack.MAX_SIZE
	def isEmpty(self):
		return False if self.data else True
	def push(self,data):
		self.data.append(data)
	def pop(self):
		return self.data.pop()

class SetOfStacks():
	def __init__(self):
		self.top = None
	def push(self, data):
		if self.top is None:
			self.top = Stack()
			self.top.push(data)
			return
		if self.top.isFull():
			stack = Stack()
			stack.next = self.top
			self.top = stack
		self.top.push(data)
	def pop(self):
		if self.top and self.top.isEmpty():
			self.top = self.top.next
		if self.top is None:
			print "Stack Underflow"
			return
		return self.top.pop()
def main():
	setofstacks = SetOfStacks()
	for i in range(8):
		setofstacks.push(i)
	for i in range(10):
		print setofstacks.pop()
main()

