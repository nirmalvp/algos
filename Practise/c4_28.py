#28) Write a algorithm such that if an element in an element in a M*N matrix is 0, it's entire row and column is set to 0.

def setToZero(matrix,numberOfROws,numberOfColumns):
	isRowContainsZero = [False for _ in range(numberOfROws)]
	isColumnContainsZero = [False for _ in range(numberOfColumns)]
	for rowNum in range(numberOfROws) :
		for colNum in range(numberOfColumns) :
			if matrix[rowNum][colNum] == 0 :
				isRowContainsZero[rowNum] = True
				isColumnContainsZero[colNum] = True
	for rowNum in range(numberOfROws) :
		for colNum in range(numberOfColumns) :
			if isRowContainsZero[rowNum] or isColumnContainsZero[colNum] :
				matrix[rowNum][colNum] = 0
def main():
	numberOfROws,numberOfColumns = map(int,raw_input("Enter the number of rows and columns").split())
	matrix = [[] for _ in range(numberOfROws)]
	for row in range(numberOfROws):
		while True:
			matrix[row] = map(int,raw_input("Enter the elements in row %s : "%row).split())
			if len(matrix[row]) == numberOfColumns:
				break
			else:
				print "Wrong number of elements"
	setToZero(matrix,numberOfROws,numberOfColumns)
	for row in matrix:
		print row
main()



