#37) Given a unsorted array of containing only all the numbers in the range 1-M,
# write code to find the shortest sub array which  contains all 1-M numbers.
# ex : [1 2 3 2 4 1 4 2 6 2 1 3 5 4] for m=6

def findSmallestWindow(array,m):
	found = {key:0 for key in array}
	count = 0
	windowBeginIndex = 0
	minWindowLength = len(array)+1 # Unattainable value
	for index,element in enumerate(array):
		found[element] += 1
		if found[element] == 1 : # ONly count the distinct elements found
			count +=1
		if count >= m : #All elements have been found atleast once
			firstElementInWindow = array[windowBeginIndex]
			while found[firstElementInWindow] > 1 :
				found[firstElementInWindow] -= 1
				windowBeginIndex += 1
				firstElementInWindow = array[windowBeginIndex]
			windowLength = index - windowBeginIndex + 1
			if windowLength < minWindowLength:
				minWindowLength = windowLength
				minWindowBeginIndex = windowBeginIndex
				minWindowEndIndex = index
	if minWindowLength == len(array) + 1 :
		return None
	return minWindowBeginIndex,minWindowEndIndex
def main():
	array = map(int,raw_input("Enter the array").split())
	m = input("Enter M in [1..M] : ")
	result= findSmallestWindow(array,m)
	if result:
		minWindowBeginIndex,minWindowEndIndex =result
		print array[minWindowBeginIndex:minWindowEndIndex+1]
main()





