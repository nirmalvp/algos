#32A)Given a int array, write a code to find three integers which sum is a specific number K.
def findTwoPair(array,lowPointer,requiredSum):
	highPointer = len(array) - 1
	while lowPointer<highPointer:
		if array[lowPointer] + array[highPointer] == requiredSum:
			yield(array[lowPointer],array[highPointer])
			lowPointer += 1
			highPointer -= 1
		elif  array[lowPointer] + array[highPointer] < requiredSum :
			lowPointer+=1
		else :
			highPointer -=1

def findTriplets(array,requiredSum):
	array.sort()
	for index,element in enumerate(array):
		for twoPair in findTwoPair(array,index+1,requiredSum - element):
			yield (element,) + twoPair

def main():
	array = map(int,raw_input("ENter the array").split())
	requiredSum = input("Enter the sum the triplet should add up to : ")
	print list(findTriplets(array,requiredSum))
main()