#Find the Kth small element in an array
def KthSmallest(array,k):
	if k >= len(array):
		return None
	pivot = array[0]
	lesserThanPivot = [element for element in array if element < pivot ]
	greaterThanPivot = [element for element in array if element > pivot ]
	lengthOfLesserArray = len(lesserThanPivot)
	if lengthOfLesserArray == k-1 : # k-1 elements lesser than pivot + 1 element(pivot itself) makes pivot kth smallest
		return pivot
	if  lengthOfLesserArray < k-1 : # pivot is too small, real kth smallest so exist in greater Array
		return KthSmallest(greaterThanPivot, k - (lengthOfLesserArray+1) )
	else :
		return KthSmallest(lesserThanPivot,k)
def main():
	array = map(int, raw_input("enter the array").split())
	k = input("Enter K : Will return Kth smallest")
	print "%s smallest = %s "%(k,KthSmallest(array,k))
main()