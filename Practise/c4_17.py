#17) There is an array A[N] of N numbers. You have to compose an array Output[N] 
#such that Output[i] will be equal to multiplication of all the elements of A[N] except A[i].
#        For example Output[0] will be multiplication of A[1] to A[N-1] and 
#Output[1] will be multiplication of A[0] and from A[2] to A[N-1]. Solve it without division operator and in O(n)

#https://stackoverflow.com/questions/2680548/given-an-array-of-numbers-return-array-of-products-of-all-other-numbers-no-div?lq=1
def createOutput(array):
	length = len(array)
	productofElementsLeftToIndex = [None]*length
	productofElementsRightToIndex = [None]*length
	output = list()
	p = 1
	for index in range(length) :
		productofElementsLeftToIndex[index] = p
		p = p * array[index]
	
	p = 1
	for index in reversed(range(length)) :
		productofElementsRightToIndex[index] = p
		p = p * array[index]
	
	for productLeft, productRight in zip(productofElementsLeftToIndex,productofElementsRightToIndex) : 
		output.append(productLeft*productRight)
	return output

def main():
	array = map(int,raw_input("Enter the array").split())
	print createOutput(array)
main()