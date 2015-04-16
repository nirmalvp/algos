import re
myArray = map( int, re.split( r"\s|,", raw_input("Enter rotated sorted array :") ) )

def findMin(low,high):
	mid = (low+high)/2
	if(myArray[mid] > myArray[high] and myArray[mid+1] < myArray[mid]):
		return myArray[mid+1]
	if(myArray[mid] < myArray[low] and myArray[mid-1] > myArray[mid] ):
		return myArray[mid]

	if(myArray[mid] > myArray [high]):
			return findMin(mid+1,high)
	else:
		return findMin(low,mid-1)

print findMin(0,len(myArray)-1)