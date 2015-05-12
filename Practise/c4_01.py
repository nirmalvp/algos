#https://stackoverflow.com/questions/726756/print-two-dimensional-array-in-spiral-order
#https://stackoverflow.com/questions/6667201/how-to-define-two-dimensional-array-in-python
#1) Given an image represented by an N\*N matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
#    1A)Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#       For example, Given n = 3, You should return the following matrix:
#        [ 1, 2, 3 ],
#        [ 8, 9, 4 ],
#        [ 7, 6, 5 ]
def createLeftTop(matrix,topRow,bottomRow,leftCol,rightCol,element):
	for colIndex in reversed(range(leftCol,rightCol+1)):
		matrix[bottomRow][colIndex] = element
		element += 1
	for rowIndex in reversed(range(topRow,bottomRow)):
		matrix[rowIndex][leftCol] = element
		element += 1
	if rightCol!=leftCol:
		createRightBottom(matrix,topRow,bottomRow-1,leftCol+1,rightCol,element)
def createRightBottom(matrix,topRow,bottomRow,leftCol,rightCol,element):
	for colIndex in range(leftCol,rightCol+1):
		matrix[topRow][colIndex] = element
		element += 1
	for rowIndex in range(topRow+1,bottomRow+1):
		matrix[rowIndex][rightCol] = element
		element += 1
	if rightCol!=leftCol:
		createLeftTop(matrix,topRow+1,bottomRow,leftCol,rightCol-1,element)

def main():
	n = input("Size of square array")
	matrix = [[None for _ in range(n)] for _ in range(n)]
	createRightBottom(matrix,0,n-1,0,n-1,1)
	for row in matrix:
		print row
main()