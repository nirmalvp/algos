#29) A int array contains positive and negative number, find the max sum of all continuous sub arrays
def maximumSumSubsequence(array):
	containsPositive = False
	for index,element in enumerate(array):
		if element > 0 :
			containsPositive = True
			startIndex = index
			maximumStartIndex = index
			maximumEndIndex = index
			currentSumStreak = element
			maximumSum = element
			break
	if not containsPositive:
		return None
	for index,element in enumerate(array[maximumStartIndex+1:],maximumStartIndex+1):
		if currentSumStreak + element < element :
			startIndex = index
			currentSumStreak = element
		else :
			currentSumStreak += element
			if currentSumStreak > maximumSum :
				maximumSum = currentSumStreak
				maximumStartIndex = startIndex
				maximumEndIndex = index
	return maximumStartIndex,maximumEndIndex,maximumSum

def main():
	array = map(int,raw_input("Enter the array"),split())
	result = maximumSumSubsequence(array)
	if result:
		startIndex,endIndex,maximumSum = maximumSumSubsequence(array)
		print array[startIndex:endIndex+1], maximumSum
	else :
		print "ALl numbers are negative"
		
main()
