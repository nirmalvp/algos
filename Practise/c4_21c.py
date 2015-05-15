#Search element in a sorted and rotated array : For eg [2,3,4,5,7,8,9] -> [7,8,9,2,3,4,5]

def searchSortRotate(array,low,high,item):
	if low > high:
		return
	mid = (low+high) >> 1
	if array[mid] == item :
		return mid
	# If we divide a sorted and rotated array into two, one half will always be sorted
	if array[low] <= array[mid] : #Check if the first half is the sorted half
		if array[low]<= item <= array[mid] : # If sorted half, we can check if element exist in this range,
		#by comparing it with the first and last elements
			return searchSortRotate(array,low,mid-1,item)
		else : # element is not present in this range
			return searchSortRotate(array,mid+1,high,item)
	else : # if second half is the sorted half
		if array[mid+1]<= item <= array[high] : # If sorted half, we can check if element exist in this range,
		#by comparing it with the first and last elements
			return searchSortRotate(array,mid+1,high,item)
		else : # element is not present the second half
			return searchSortRotate(array,low,mid-1,item)
def main():
	array = map(int, raw_input("ENter the elements").split())
	index = searchSortRotate(array,0,len(array)-1,input("Enter Search element"))
	if index != None :
		print "Found at ",index
	else:
		print "Not Found"
main()