#78) Given an unsorted array of integers, find the length of the longest consecutive elements sequence. [LeetCode]
#        Your algorithm should run in O(n) complexity.
#       For example, Given [100, 4, 101, 1, 3,99, 2], The longest consecutive elements sequence is [1, 2, 3, 4]. 
#Return its length: 4.

def findLongestConsecutive(array):
	yetToProcess  = set(array)
	maxIntervalLength = 0
	for element in array :
		if not yetToProcess: # Stop when all the elements have been processed
			break
		if element not in yetToProcess:
			continue
		rangeLength = 0
		i = 0
		while element + i in yetToProcess:
			yetToProcess.remove(element + i)
			rangeLength += 1
			i += 1
		i = 1
		while element - i in yetToProcess:
			yetToProcess.remove(element - i)
			rangeLength +=1
			i += 1
		if rangeLength > maxIntervalLength :
			maxIntervalLength = rangeLength
	return maxIntervalLength
def main():
	array = map(int,raw_input("Enter the array").split())
	print findLongestConsecutive(array)
main()





	