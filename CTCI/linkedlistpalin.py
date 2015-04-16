from linkedlist import LinkedList

palin = raw_input("Enter palin Strng : ")
myList = LinkedList()
for ch in palin:
	myList.insertNode(ch)


def checkPalindrom(self):
	myStack =[]
	slow = myList.first
	fast = myList.first
	myStack.append(slow.data)

	while(fast!=None and fast.next!=None):
		slow=slow.next
		fast=fast.next.next
		if(fast !=None):
			myStack.append(slow.data)
	
	while (slow != None):
		if(slow.data != myStack.pop()):
			print "Not palin"
			return
		slow=slow.next
	print "Palindrome"

LinkedList.checkPalindrom = checkPalindrom
myList.checkPalindrom()






