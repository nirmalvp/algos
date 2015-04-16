from linkedlist import LinkedList

myList = LinkedList()
for i in range(1,11):
	myList.insertNode(i)

def kthlast(self,k):
	fast = self.first
	slow = self.first
	for i in range(k-1):
		if(fast.next!=None):
			fast=fast.next
		else :
			print "Not enough elements"
			return
	while(fast.next!=None):
		fast=fast.next
		slow= slow.next
	print "kthlast : ",slow.data

LinkedList.kthlast = kthlast

myList.kthlast(3)


