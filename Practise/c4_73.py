#Given an array A of integers, find the maximum of j-i subjected to the constraint of A[i] < A[j]
def findGreatestRange(array):
	#If there is a element to the left lesser than the current element, we would always choose the left one.
	#Therefore the candidates of starting point are elements which has no lesser elements to its left.
	#candidatesForStartingElement stores indices of qualifying elements
	candidatesForStartingElement = list()
	candidatesForStartingElement.append(0)
	for index,element in enumerate(array[1:],1):
		if element < array[candidatesForStartingElement[-1]] :
			candidatesForStartingElement.append(index)
	#candidatesForStartingElement[-1] contains the index of the smallest element which qualify as a starting point
	#we start from the end of the list 
	#and find an element that is greater than the element stored at array[candidatesForStartingElement[-1]]
	#Elements lesser than array[candidatesForStartingElement[-1]] are lesser than all other 
	#array[candidatesForStartingElement[..]] and can be ignored further 
	j = len(array) - 1
	maxDist = -1
	for i in reversed(candidatesForStartingElement) :
		while j >=0 and array[j] < array[i]:
			j = j-1
		if j < 0:
			break
		if array[i] == array[j]: #We want to preserve the value of j for the next iteration of i, but it 
		#it shouldnt be used in the maxdist calculation of current iteration
			continue
		maxDist = max(maxDist, j - i + 1 )
	return maxDist
def main():
	array = map(int,raw_input("Enter the array").split())
	print findGreatestRange(array)
main()
