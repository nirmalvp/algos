#70) Given an array of integers, write a method to find indices m and n such that if you sorted elements m through n, the entire array would be sorted.
#        Minimize n - m (that is find the smallest such sequence).
#        Example: 1,2,4,7,10,11,7,12,11,6,7,16,18,19, return (3,9)

def findSmallestRangeToSort(array):
	for index,(element,nextElement) in enumerate(zip(array,array[1:])):
		if element > nextElement : # Find the point where array ceases to be in sorted order
			startingPoint = index
			break
	for index,element in enumerate(array[startingPoint+1:],startingPoint+1):
		if element <= array[startingPoint]: # Any element that is lesser than the the element at which 
		#the sort order ceased to be, is not sorted. We need to include them in the sort range
			endPoint = index
	for index,element in enumerate(array[:startingPoint]):
		if element >= array[endPoint]: # Conside [1 3 11 8 2] . Ending point is element 2 ,but now we have to
		# add element 3(first num bigger than 2) in our sort or else the order cant be maintained
			startingPoint = index
			break
	return startingPoint,endPoint
def main():
	array = map(int,raw_input("Enter the elements").split())
	print findSmallestRangeToSort(array)
main()

