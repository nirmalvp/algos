#13) Suppose you have an NxM matrix of positive and negative integers. Write some code that finds the sub-matrix with the maximum sum of its elements.
#https://www.youtube.com/watch?v=yCQN096CwWM&list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr&index=31
def findMaximumIncreasingSubSequence(array):
	for index,element in enumerate(array):
		if element >= 0 : #Start from first positive number
			currentSumStreak = element
			bestSumSoFar = element
			bestStartIndex = index
			bestEndIndex = index
			break
	for index,element in enumerate(array[bestStartIndex+1:],bestStartIndex+1):
		if element + currentSumStreak >= element :
			currentSumStreak += element
			if currentSumStreak > bestSumSoFar :
				bestSumSoFar = currentSumStreak
				bestEndIndex = index
		else :
			currentSumStreak = element
			bestStartIndex = index
	return bestSumSoFar,bestStartIndex,bestEndIndex


def findMaxSumSubMatrix(matrix,numOfrows,numOfColums):
	subMatrixLeft = 0
	subMatrixRight = 0
	subMatrixTop = 0
	subMatrixBottom = 0
	bestMatrixSum = 0
	for left in range(numOfColums):
		sumOfElementsBetweenLAndR = [0 for _ in range(numOfrows)]
		for right in range(left,numOfColums):
			for row in range(numOfrows):
				sumOfElementsBetweenLAndR[row] += matrix[row][right]
			matrixSum,startRow,endRow = findMaximumIncreasingSubSequence(sumOfElementsBetweenLAndR)
			if matrixSum > bestMatrixSum:
				bestMatrixSum = matrixSum
				subMatrixLeft = left
				subMatrixRight = right
				subMatrixTop = startRow
				subMatrixBottom = endRow
	return subMatrixLeft,subMatrixRight,subMatrixTop,subMatrixBottom

def main():
	numOfrows,numOfColums = map(int,raw_input("Input number of rows and column").split())
	matrix = [ [] for _ in range(numOfrows) ]
	for row in range(numOfrows):
		while True:
			matrix[row] = map(int,raw_input("Enter the elements in row number %s : "%row).split())
			if len(matrix[row]) == numOfColums :
				break
			print "Invalid number of elements in the row"
	subMatrixLeft,subMatrixRight,subMatrixTop,subMatrixBottom = findMaxSumSubMatrix(matrix,numOfrows,numOfColums)
	for row in range(subMatrixTop,subMatrixBottom+1):
		print matrix[row][subMatrixLeft:subMatrixRight+1]
main()
