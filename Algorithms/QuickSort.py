def partition(myArray,startIndex,endIndex):
	pivot = myArray[endIndex]
	boundary = startIndex - 1
	for i in range(startIndex, endIndex):
		if(myArray[i] < pivot):
			boundary = boundary + 1
			myArray[boundary], myArray[i] = myArray[i], myArray[boundary]
	boundary = boundary + 1
	myArray[boundary], myArray[endIndex] = myArray[endIndex], myArray[boundary]
	return boundary

def quickSort(myArray,startIndex = 0 ,endIndex = None):
	if(not endIndex):
		endIndex = len(myArray) - 1

	if(startIndex < endIndex):
		pivotPosition = partition(myArray,startIndex,endIndex)
		quickSort(myArray,startIndex,pivotPosition-1)
		quickSort(myArray,pivotPosition+1,endIndex)

myArray= [2,8,7,1,3,5,6,4]
quickSort(myArray)
print myArray