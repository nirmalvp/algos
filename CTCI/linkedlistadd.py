from linkedlist import LinkedList
num = map(int,raw_input("Enter the first number"))

firstNum = LinkedList()
for x in reversed(num):
	firstNum.insertNode(x)
num = map(int,raw_input("Enter the second number"))
secondNum = LinkedList()
for x in reversed(num):
	secondNum.insertNode(x)

temp1 = firstNum.first
temp2 = secondNum.first
carry = 0
result = LinkedList()
while(temp1!=None and temp2!=None):
	sum = temp1.data + temp2.data + carry
	carry = sum / 10
	sum = sum % 10
	result.insertNode(sum)
	if(temp1.next== None and temp2.next==None and carry !=0 ):
			result.insertNode(carry)
	temp1 = temp1.next
	temp2 = temp2.next

while(temp1 != None):
	sum = temp1.data + carry
	carry = sum /10
	sum = sum % 10
	result.insertNode(sum)
	if(temp1.next== None and carry !=0 ):
			result.insertNode(carry)
	temp1 = temp1.next

while(temp2 != None):
	sum = temp2.data + carry
	carry = sum /10
	sum = sum % 10
	result.insertNode(sum)
	if(temp2.next== None and carry !=0 ):
			result.insertNode(carry)
	temp2 = temp2.next


result.display()