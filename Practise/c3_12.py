#12) Implement a function to check if a linked list is a palindrome.
from c3_linkedlist import LinkedList
def isPalindrome(linkedList):
	slowPointer = linkedList.first
	fastPointer = linkedList.first
	stack = list()
	stack.append(slowPointer.data)
	while fastPointer.next and fastPointer.next.next :
		fastPointer = fastPointer.next.next
		slowPointer = slowPointer.next
		if fastPointer.next != None : # if Even Number of elemets. consider the middle element, otherwise ignore it
			stack.append(slowPointer.data)
	slowPointer = slowPointer.next
	while slowPointer:
		if slowPointer.data != stack.pop():
			return False
		slowPointer = slowPointer.next
	return True

def main():
	linkedList = LinkedList()
	for element in raw_input("enter the element of the list ").split():
		linkedList.insert(int(element))
	print isPalindrome(linkedList)
main()
