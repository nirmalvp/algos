#32) Given a int array, write a code to find a pair integers which sum is a specific number K
def findPairs(array, requiredSum):
	visitedElements = set()
	for element in array:
		otherElement = requiredSum - element
		if otherElement in visitedElements :
			yield (element,otherElement)
		else :
			visitedElements.add(element)
def main():
	array = map(int,raw_input("Enter the array").split())
	requiredSum = input("Enter the required Sum")
	print list(findPairs(array,requiredSum))
main()