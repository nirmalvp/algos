#65) Given a matrix, number in each row and column greater than the number in previous row and previous column
#write code to find a given integer exist in the matrix or not. [Yang Matrix Searching]

def searchMatrix(matrix,numberOfRows,numberOfColums,element):
	row=0
	column = numberOfColums-1
	seedElement = matrix[row][column] # Start from top right. Elements to its left in same row are lesser than it
	#and elements to its below in the same col are greater than it
	flag = True
	while flag :
		#If flag remains as false after one iteration, it means it has nowhere to move. The element is not
		#present in the matrix
		flag = False 
		while element > seedElement and row != numberOfRows - 1: #If element is greater than seed element,it cant
		#be in the same row as seedElement 
			row+=1
			seedElement = matrix[row][column]
			flag = True
		while element < seedElement and column != 0: #if element is lesser, it has to be to the left of seedElement
			column = column - 1
			seedElement = matrix[row][column]
			flag = True
		if seedElement == element:
			return (row,column)
	return None
def main():
	numberOfRows,numberOfColums = map(int,raw_input("Enter number of rows and Colums").split())
	matrix = [ [] for _ in range(numberOfRows) ]
	for row in range(numberOfRows):
		while True:
			matrix[row] = map(int,raw_input("Enter the elements of row %s : "%row).split())
			if len(matrix[row]) == numberOfColums :
				break
			else:
				"print number of elements in row not correct"
	element = input("Enter element to search : ")
	print searchMatrix(matrix,numberOfRows,numberOfColums,element) or "None"
main()