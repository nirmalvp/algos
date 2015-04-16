from linkedlist import LinkedList, Node
num1 = map(int,raw_input("enter number 1 : "))
num2 = map(int,raw_input("enter number 2 : "))

firstNum = LinkedList()
for x in num1:
	firstNum.insertNode(x)

secondNum = LinkedList()
for x in num2:
	secondNum.insertNode(x)


temp = firstNum.first
firstStack=[]

while(temp!=None):
	firstStack.append(temp.data)
	temp = temp.next

temp = secondNum.first
secondStack=[]

while(temp!=None):
	secondStack.append(temp.data)
	temp = temp.next

def insertFirst(theList,data):
	node = Node(data)
	node.next = theList.first
	theList.first = node

carry =0
result = LinkedList()

while (firstStack or secondStack):
	num1 = firstStack.pop() if firstStack else 0
	num2 = secondStack.pop() if secondStack else 0
	sum = num1 + num2 + carry
	carry = sum / 10
	sum = sum % 10
	insertFirst(result,sum)
	if( (not firstStack and not secondStack) and carry!=0):
		insertFirst(result,carry)

result.display()
	




