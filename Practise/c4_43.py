#43) Given an int array, write code to find the numbers, for which all the numbers left to it are smaller than the number
#and all the numbers to its right are greater than the number

def findMidNumbers(array):
	length = len(array)
	
	leftMax = list()
	rightMin= [None]*length
	#For a number to be in the mid, it has to be greater than the maximum number to its left and
	# lesser than the smallest number to its right
	
	maxTillnow = array[0]
	for number in array:
		leftMax.append(maxTillnow)
		if number > maxTillnow:
			maxTillnow = number
	
	minTillNow = array[length-1]
	for index in reversed(xrange(length)):
		element = array[index]
		rightMin[index] = minTillNow
		if element < minTillNow:
			minTillNow = element
	
	for index,element in enumerate(array):
		if leftMax[index] < element < rightMin[index] :
			yield element

def main():
	array = map(int,raw_input("Enter the array").split())
	for midElements in findMidNumbers(array):
		print midElements

main()
