# Find the only number that appears exactly twice , in a list of unsorted list of length n+1 made
#from number in range 1-n

def findDuplicateNum(array):
	originalSum = sum(array)
	n = len(array) - 1
	expectedSum = (n * (n+1)) / 2
	return originalSum - expectedSum
def main():
	array = map(int,raw_input("enter the array : ").split())
	print "Duplicate element = " , findDuplicateNum(array)

main()

