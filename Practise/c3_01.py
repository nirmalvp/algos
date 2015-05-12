#1) Merge two sorted lists
from c3_linkedlist import LinkedList
def merge(linkedListOne,linkedListTwo):
	mergedLinkedList = LinkedList()
	currentElementOne = linkedListOne.first
	currentElementTwo = linkedListTwo.first
	while currentElementOne and currentElementTwo:
		if currentElementOne.data < currentElementTwo.data:
			mergedLinkedList.insert(currentElementOne.data)
			currentElementOne = currentElementOne.next
		else:
			mergedLinkedList.insert(currentElementTwo.data)
			currentElementTwo = currentElementTwo.next
	while currentElementOne:
		mergedLinkedList.insert(currentElementOne.data)
		currentElementOne = currentElementOne.next
	while currentElementTwo:
		mergedLinkedList.insert(currentElementTwo.data)
		currentElementTwo = currentElementTwo.next
	return mergedLinkedList


	
def main():
	linkedListOne = LinkedList()
	linkedListTwo = LinkedList()
	list1 = map(int,raw_input("Enter First sorted list").split())
	for element in list1:
		linkedListOne.insert(element)
	list2 = map(int,raw_input("Enter 2nd sorted list").split())
	for element in list2:
		linkedListTwo.insert(element)
	mergedLinkedList = merge(linkedListOne,linkedListTwo)
	mergedLinkedList.show()
main()