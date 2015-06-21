#2) Implement a Queue with Stacks.
from c7_stack import Stack
class Queue(object):
	def __init__(self):
		self.pushstack = Stack()
		self.popstack = Stack()
	def enqueue(self,data):
		self.pushstack.push(data)
	def dequeue(self):
		if self.popstack.top is None:
			while self.pushstack.top:
				self.popstack.push(self.pushstack.pop())
		return self.popstack.pop()

def main():
	q= Queue()
	q.enqueue(1)
	q.enqueue(2)
	print q.dequeue()
	q.enqueue(3)
	print q.dequeue()
	print q.dequeue()
main()