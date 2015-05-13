# 4) Given an array whose elements are sorted, return the index of a the first occurrence of a specific integer. 
#Do this in sub-linear time.

def modifiedBinarySearch(array,low,high,element):
	while low <= high:
		mid = (low + high) >> 1
		if array[mid] == element and ( array[mid-1] != element or mid == 0 ) :
			return mid
		if element <= array[mid] :
			high = mid - 1
		else:
			low = mid + 1
	return None

def main():
	array = map(int,raw_input("Enter the array").split())
	element = input("Enter the search element")
	index = modifiedBinarySearch(array,0,len(array)-1,element)
	if index != None:
		print "First Occurence at %s"%index
	else:
		print "element not found"
main()

