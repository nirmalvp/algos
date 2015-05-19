#67) Given an array whose values first decrease and then increase,
# write an algorithm to determine whether a given value target exists in the array
def binarySearch(array,low,high,element,isAscendingOrder):
	while low <= high:
		mid = (low + high) >>1
		if array[mid] == element :
			return mid
		if element < array[mid]:
			if isAscendingOrder:
				high = mid -1
			else :
				low = mid + 1
		else :
			if isAscendingOrder:
				low = mid + 1
			else :
				high = mid - 1

def butonicSearch(array,low,high,element):
	if low > high :
		return 
	mid = (low + high) >> 1
	if array[mid] == element :
		return mid
	if mid == high :
		return
	isAscending = array[mid+1] > array[mid]
	if element > array[mid] and isAscending :
		return butonicSearch(array,mid+1,high,element)
	if element > array[mid] and not isAscending :
		return butonicSearch(array,low,mid-1,element)
	if element < array[mid]:
		leftAscendingSearch = binarySearch(array,low,mid-1,element,isAscendingOrder = True)
		if leftAscendingSearch is not None :
			return leftAscendingSearch
		else : 
			return binarySearch(array,mid+1,high,element,isAscendingOrder = False)
def main():
	array = map(int,raw_input("Enter the butonic array : ").split())
	#array = [10,20,30,40,50,45,35,25,15,5]
	element = input("Enter search element : ")
	foundIndex = butonicSearch(array,0,len(array)-1,element)
	if foundIndex is not None:
		print "%s found at %s"%(element,foundIndex)
	else :
		print "%s not found"%element
main()



