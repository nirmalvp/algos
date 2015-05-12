from c3_linkedlist import LinkedList
def getMiddleElement(firstnode):
	fastRunner = firstnode
	slowRunner = firstnode
	while fastRunner.next and fastRunner.next.next :
		fastRunner = fastRunner.next.next
		slowRunner = slowRunner.next
	return slowRunner 
def merge(firstnode, secondHalfFirstNode):
	mergedList = LinkedList()
	while firstnode and secondHalfFirstNode:
		if firstnode.data < secondHalfFirstNode.data:
			mergedList.insert(firstnode.data)
			firstnode = firstnode.next
		else :
			mergedList.insert(secondHalfFirstNode.data)
			secondHalfFirstNode = secondHalfFirstNode.next
	while firstnode:
		mergedList.insert(firstnode.data)
		firstnode = firstnode.next
	while secondHalfFirstNode:
		mergedList.insert(secondHalfFirstNode.data)
		secondHalfFirstNode = secondHalfFirstNode.next
	return mergedList.first
		

def mergeSort(firstnode):
	if firstnode.next == None :
		return firstnode
	middleElement = getMiddleElement(firstnode)
	secondHalfFirstNode = middleElement.next
	middleElement.next = None
	firstNode = merge(mergeSort(firstnode), mergeSort(secondHalfFirstNode))
	return firstNode

def main():
	linkedList = LinkedList()
	for number in raw_input	("Enter the elements of the list").split() : 
		linkedList.insert(int(number))
	linkedList.first = mergeSort(linkedList.first)
	linkedList.show()
main()