#10) Write code to partition a linked list around a value x, such that all nodes less then x come to before,
# all nodes greater than or equal to x.
from c3_linkedlist import LinkedList
def arrangeAroundPivot(linkedlist,num):
	lessThanPivotPointer = linkedlist.first
	greaterThanPointer = linkedlist.first
	current =linkedlist.first
	while current:
		nextItem = current.next
		if current.data < num :
			current.next = lessThanPivotPointer
			lessThanPivotPointer = current
		else :
			greaterThanPointer.next = current
			greaterThanPointer = current
		current = nextItem
	linkedlist.first = lessThanPivotPointer

def main():
	userInput = map(int,raw_input("Enter the element of the list").split())
	linkedList = LinkedList()
	for element in userInput:
		linkedList.insert(element)
	arrangeAroundPivot(linkedList,input("Enter Pivot element"))
	linkedList.show()
main()