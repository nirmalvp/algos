#19) Given a sorted cyclic linked list in ascending order, 
#write code to insert a int into the list and keeping it in ascending order.
from c3_circularlinkedlist import CircularLinkedList,Node
def insertMaintainingOrder(cLinkedList,number):
	node = Node(number)
	currentElement = cLinkedList.first
	if number < cLinkedList.first.data:
		while currentElement.next != cLinkedList.first :
			currentElement = currentElement.next
		temp = currentElement.next 
		currentElement.next = node
		node.next = temp
		cLinkedList.first = node
		return
	while currentElement.next.data < number and currentElement.next != cLinkedList.first :
			currentElement = currentElement.next
	temp = currentElement.next 
	currentElement.next = node
	node.next = temp

def main():
	cLinkedList = CircularLinkedList()
	for number in sorted(map(int,raw_input("Enter the elements of list").split())):
		cLinkedList.insert(number)
	print "List before Insertion = ",
	cLinkedList.show()
	insertMaintainingOrder(cLinkedList,input("Enter the number to insert"))
	cLinkedList.show()
main()
