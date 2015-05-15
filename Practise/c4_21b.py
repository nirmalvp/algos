#For an array whose values first increase and then decrease,
#write an algorithm to determine whether a given value target exists in the array

# https://stackoverflow.com/questions/19372930/given-a-bitonic-array-and-element-x-in-the-array-find-the-index-of-x-in-2logn/21697488#21697488

def binarySearch(array,low,high,item,increasingBinarySearch):
	while low <= high :
		mid = (low + high) >> 1
		print array[mid],item
		if array[mid] == item :
			return mid
		if item < array[mid] :
			if increasingBinarySearch :
				high = mid - 1
			else :
				low = mid + 1
		else :
			if increasingBinarySearch :
				low = mid + 1
			else :
				high = mid - 1

def bitonicBinarySearch(array,low,high,item):
	mid = (low + high) >> 1
	if array[mid] == item :
		return mid
	if low == high: # One element only and if it is not equal to our item, we can return none
		return
	isIncreasingToRight = array[mid+1] - array[mid] > 0  
	if item > array[mid] and isIncreasingToRight : # if item is greater than mid and the array is increasing
	#to right, we can disregard the left portion since it will have only smaller elements
		return bitonicBinarySearch(array,mid+1,high,item)
	if item > array[mid] and not isIncreasingToRight : # elements in array are decreasing to the right, so if 
	#item is already greater than mid, we wont find them in the right subarray
		return bitonicBinarySearch(array, low,mid-1,item)
	if item < array[mid] : #If an item is less than mid, it can either be in the left or right of mid
		leftSearchIndex = binarySearch(array,low,mid-1,item,increasingBinarySearch=True)
		rightSearchIndex = binarySearch(array,mid+1,high,item,increasingBinarySearch=False)
		if leftSearchIndex != None :
			return leftSearchIndex
		if rightSearchIndex != None :
			return rightSearchIndex
def main():
	array = map(int,raw_input("Enter the array : Strictly increasing and then Strictly decreasing").split())
	index = bitonicBinarySearch(array,0,len(array)-1,input("ENter Search ELement"))
	if index != None :
		print "Found at",index
	else :
		print "Sorry"
main() 

