from linkedlist import LinkedList
from random import randint

myList = LinkedList()

for i in range(10):
	myList.insertNode(randint(0,9))

def partition(self):
	pivot = self.first.data
	start = self.first
	temp = self.first
	while(temp.next!=None):
		if(temp.next.data < pivot):
			nextElement = temp.next.next
			temp.next.next = start
			start = temp.next
			temp.next=nextElement
		else:
			temp = temp.next
	self.first = start

LinkedList.partition = partition
myList.display()
myList.partition()
myList.display()


			






