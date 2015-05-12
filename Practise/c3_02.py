#2) Given two linked lists A and B, return a list C containing the intersection elements of A and B. 
#The nodes of C should appear in the order as in B.
from c3_linkedlist import LinkedList
def findIntersection(listOne,listTwo):
	elementDict = dict()
	intersectionList = LinkedList()
	for element in listOne:
		elementDict[element] = 1
	for element in listTwo:
		if elementDict.get(element) == 1:
			intersectionList.insert(element)
			elementDict[element] = 0 # To avoid repetition
	return intersectionList

def main():
	userInputList = map(int,raw_input("Enter Elements of first list").split())
	listOne = LinkedList()
	for element in userInputList:
		listOne.insert(element)
	userInputList = map(int,raw_input("Enter Elements of second list").split())
	listTwo = LinkedList()
	for element in userInputList:
		listTwo.insert(element)
	intersectionList = findIntersection(listOne,listTwo)
	intersectionList.show()
main()

