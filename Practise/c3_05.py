#Reverse every k node in a linked list
from c3_linkedlist import LinkedList
def reverseEveryNth(node,n):
	if node == None:
		return
	firstElement = node
	previousElement = None
	currentElement = node
	count = 0
	while count < n-1 and currentElement.next:
		nextElement = currentElement.next
		currentElement.next = previousElement
		previousElement = currentElement
		currentElement = nextElement
		count += 1
	firstOfNextNnodes = currentElement.next
	currentElement.next = previousElement
	firstElement.next = reverseEveryNth(firstOfNextNnodes,n)
	return currentElement
	
def main():
	userInput = map(int,raw_input("Enter the element of the list").split())
	linkedList = LinkedList()
	for element in userInput:
		linkedList.insert(element)
	n = input("Enter n where n is the number of element to be reversed")
	linkedList.first = reverseEveryNth(linkedList.first,n)
	linkedList.show()

main()
