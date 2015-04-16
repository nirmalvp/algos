from stacklinkedlist import Stack 

def peek(self):
	return self.top.data

Stack.peek = peek

stack=Stack()
stack.push(2)
stack.push(4)
stack.push(8)
stack.push(1)
stack.push(7)


temp =Stack()

temp.push(stack.pop())

while(stack.top != None):
	tmp = stack.pop()
	while (temp.top !=None and tmp < temp.peek() ):
		stack.push(temp.pop())
	temp.push(tmp)
while (temp.top!=None):
	print temp.pop()











