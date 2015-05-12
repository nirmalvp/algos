#21) Reverse a linked list from position m to n. Do it in-place and in one-pass.
#        For example:    Given 1->2->3->4->5->NULL, m = 2 and n = 4, return 1->4->3->2->5->NULL.
from c3_linkedlist import LinkedList
def reverse(firstNode,count):
	currentElement = firstNode
	previousElement = None
	while count > 0 and currentElement.next :
		nextItem = currentElement.next
		currentElement.next = previousElement
		previousElement = currentElement
		currentElement = nextItem
		count -= 1
	firstNode.next = currentElement.next
	currentElement.next = previousElement
	return currentElement


def reverseInRange(linkedlist,m,n):
	if m == 1 :
		linkedlist.first = reverse(linkedlist.first, n-m)
		return
	currentElement = linkedlist.first
	count = 1
	while count < m-1 :
		currentElement = currentElement.next
		count+=1
	currentElement.next = reverse(currentElement.next, n-m)

def main():
	linkedList = LinkedList()
	for number in raw_input	("Enter the elements of the list").split() : 
		linkedList.insert(int(number))
	m = input("enter index of starting element")
	n = input("enter index of ending element")
	reverseInRange(linkedList,m,n)
	linkedList.show()
main()
