#36) Given matrix, find the sub 2 * 2 array with max sum.

def findMaxTwoCrossTwo(matrix):
	numberOfColums = len(matrix[0])
	maxSum = 0
	for left in range(numberOfColums - 1) :
		sumOfTwoElementsRightOfLeftInRow = [ sum(row[left:left+2]) for row in matrix]
		for index,(element,nextElement) in enumerate(zip(sumOfTwoElementsRightOfLeftInRow,sumOfTwoElementsRightOfLeftInRow[1:])) :
			if element + nextElement > maxSum:
				maxSum = element + nextElement
				leftIndex = left
				topIndex = index
	return topIndex,leftIndex,maxSum
def main():
	numberOfRows,numberOfColums = map(int,raw_input("Enter number of rows and Colums").split())
	if numberOfRows<2 or numberOfColums<2 :
		print "Atleast 2 rows and 2 Colums required"
		return
	matrix = [ [] for _ in range(numberOfRows) ]
	for row in range(numberOfRows):
		while True:
			matrix[row] = map(int,raw_input("Enter the elements of row %s : "%row).split())
			if len(matrix[row]) == numberOfColums :
				break
			else:
				"print number of elements in row not correct"
	topIndex,leftIndex,maxSum = findMaxTwoCrossTwo(matrix)
	print "Max Sum = ",maxSum
	for row in range(topIndex,topIndex+2):
		print matrix[row][leftIndex:leftIndex+2]
main()
				
 

