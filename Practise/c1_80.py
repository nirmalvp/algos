#80) Given an array of non-negative integers, you are initially positioned at the first index of the array.   [LeetCode]
#    Each element in the array represents your maximum jump length at that position.
#        Determine if you are able to reach the last index.
#        For example:    A = [2,3,1,1,4], return true. A = [3,2,1,0,4], return false.

def isPathExisting(array,index,zeroIndex):
	jumpLength = array[index]
	for  length in range(1,jumpLength+1):
		if index + length > zeroIndex :
			return True
		if index+length < len(array) :
			if isPathExisting(array,index+length,zeroIndex):
				return True
	return False
def findIndexOfLastZero(array):
	index =-1
	for pos,number in enumerate(array):
		if number == 0:
			index = pos
	return index
def main():
	array = map(int, raw_input("Enter the array").split())
	zeroIndex = findIndexOfLastZero(array)
	if zeroIndex == -1:
		print True
	else:
		print isPathExisting(array,0,zeroIndex)
main()