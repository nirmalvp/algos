#60) Given an array which is partial sorted, write code to find a specified item in it.
#partial sorted = [sortedsection1,sortedsection2] eg : [7,8,16,20,10,15,18]
def binarySearch(array,low,high,element):
	while low <= high :
		mid =(low+high) >> 1
		#print "binary",low,mid,high
		if array[mid] == element:
			return mid
		if element < array[mid]:
			high = mid-1
		else:
			low = mid + 1

def searchPartialSortedArray(array,low,high,element):
	if low > high :
		return
	mid = (low + high) >> 1
	#print "fn",low,mid,high
	if array[mid] == element :
		return mid
	elif array[mid+1] < array[high]: #Find the sorted half. If sorted half
		if array[mid+1] <= element <= array[high]: # Check if element in the sorted half
			rightBinarySearchResult = binarySearch(array,mid+1,high,element) 
			if rightBinarySearchResult is not None:
				return rightBinarySearchResult
		return searchPartialSortedArray(array,low,mid-1,element) #if element not in the sorted half
	else : #If sorted half
		if array[low] <= element <= array[mid-1]:
			leftBinarySearchResult = binarySearch(array,low,mid-1,element) 
			if leftBinarySearchResult is not None:
				return leftBinarySearchResult
		return searchPartialSortedArray(array,mid+1,high,element)
def main():
	array = map(int,raw_input("Enter the array : ").split())
	element = input("Enter the element to search for : ")
	print "%s found at %s"%(element,searchPartialSortedArray(array,0,len(array)-1,element))
main()

