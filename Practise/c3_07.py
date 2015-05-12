#7) We have a linked list as a1,a2,a3...an,b1,b2,b3...bn, we need a rearrange method to rearrange the linked list into
#a1,b1,a2,b2...an,bn
from c3_linkedlist import LinkedList
def rearrange(linkedList,length):
	rearrangedLinkedList = LinkedList()
	fastPointer = linkedList.first
	for i in xrange(length/2):
		fastPointer = fastPointer.next
	slowPointer = linkedList.first
	while fastPointer:
		rearrangedLinkedList.insert(slowPointer.data)
		rearrangedLinkedList.insert(fastPointer.data)
		slowPointer = slowPointer.next
		fastPointer = fastPointer.next
	return rearrangedLinkedList

def main():
	userInput = map(int,raw_input("Enter the element of the list").split())
	length = len(userInput)
	if length % 2 != 0 :
		print "LinkedList needs even number of elements"
		return
	linkedList = LinkedList()
	for element in userInput:
		linkedList.insert(element)
	rearrangedLinkedList = rearrange(linkedList,length)
	rearrangedLinkedList.show()

main()