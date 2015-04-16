class Stack:
	def __init__(self,limit):
		self.stackContent = [None]*limit
		self.top = -1
		self.next =None
		
	def push(self,data):
		self.top += 1
		self.stackContent[self.top] = data

	def pop(self):
		item = self.stackContent[self.top]
		self.top -= 1
		return item

class SetOfStacks:
	def __init__(self,limit):
		self.top = None
		self.limit = limit

	def push(self,data):
		if(self.top == None):
			stack=Stack(self.limit)
			stack.push(data)
			self.top = stack 
		else :
			if( (self.top.top)+1 == self.limit):
				stack = Stack(self.limit)
				stack.next = self.top
				self.top = stack
				stack.push(data)
			else :
				self.top.push(data)
	def pop(self):
		if(self.top.top == -1):
			if(self.top.next==None):
				return
			self.top = self.top.next
		return self.top.pop()

s= SetOfStacks(3)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()
print s.pop()



		
