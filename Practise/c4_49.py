#49) Given an matrix M * N, write code to clock-wisely print the matrix 
def printBotomRightToTopLeft(matrix,top,left,bottom,right):
	for cellIndex in reversed(xrange(left,right+1)):
		print matrix[bottom][cellIndex],
	for rowIndex in reversed(xrange(top,bottom)):
		print matrix[rowIndex][left],
	if left != right:
		printTopLeftToBottomRight(matrix,top,left+1,bottom-1,right)

def printTopLeftToBottomRight(matrix,top,left,bottom,right):
	for cellIndex in xrange(left,right+1):
		print matrix[top][cellIndex],
	for rowIndex in range(top+1,bottom+1):
		print matrix[rowIndex][right],
	if left != right:
		printBotomRightToTopLeft(matrix,top+1,left,bottom,right-1)

def main():
	numOfrows,numOfColums = map(int,raw_input("Input number of rows and column").split())
	matrix = [ [] for _ in range(numOfrows) ]
	for row in range(numOfrows):
		while True:
			matrix[row] = map(int,raw_input("Enter the elements in row number %s : "%row).split())
			if len(matrix[row]) == numOfColums :
				break
			print "Invalid number of elements in the row"
	printTopLeftToBottomRight(matrix,0,0,numOfrows-1,numOfColums-1)
main()
