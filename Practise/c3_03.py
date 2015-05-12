#3) Given a single list, find the "Mth to the last" element.
from c3_linkedlist import LinkedList
def findNthToLastElement(linkedList,n):
	fastPointer = linkedList.first
	for i in xrange(n):
		fastPointer = fastPointer.next
	slowPointer = linkedList.first
	while fastPointer:
		fastPointer = fastPointer.next
		slowPointer = slowPointer.next
	return slowPointer.data

def main():
	userInput = map(int,raw_input("Enter the element of the list").split())
	n = input("Enter n in nth to last")
	if len(userInput) < n :
		print "Insufficient number of element"
		return
	linkedList = LinkedList()
	for element in userInput:
		linkedList.insert(element)
	print findNthToLastElement(linkedList,n)
main()
