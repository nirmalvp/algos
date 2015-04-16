from linkedlist import LinkedList

myList= LinkedList()
myList.insertNode(1)
myList.insertNode(2)
myList.insertNode(3)
myList.insertNode(4)
myList.insertNode(5)
myList.insertNode(11)
myList.insertNode(12)
myList.insertNode(13)
myList.insertNode(14)
myList.insertNode(15)

def scramble(self):
	fast=self.first
	slow=self.first

	while(fast!=None):
		fast=fast.next.next
		slow=slow.next

	fast=self.first

	scrambledList=LinkedList()
	while(slow!=None):
		scrambledList.insertNode(fast.data)
		scrambledList.insertNode(slow.data)
		fast = fast.next
		slow = slow.next
	return scrambledList

LinkedList.scramble = scramble

newList = myList.scramble()
newList.display()



