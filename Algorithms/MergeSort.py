def mergeArrays(left,right,myArray):
	leftLength = len(left)
	rightLength = len(right)
	i = j =k=0
	while(i< leftLength and j <rightLength):
		if(left[i] < right[j]):
			myArray[k] = left[i]
			i += 1
		else :
			myArray[k] = right[j]
			j += 1
		k += 1
	while(i<leftLength):
		myArray[k] = left[i]
		i += 1
		k += 1
	while (j<rightLength):
		myArray[k] = right[j]
		j += 1
		k += 1


def mergeSort(myArray):
	arrayLength = len (myArray)
	if( arrayLength<2 ):
		return
	left=myArray[ : arrayLength/2]
	right = myArray[ arrayLength/2 : arrayLength ]
	mergeSort(left)
	mergeSort(right)
	mergeArrays(left,right,myArray)

myArray = map(int, raw_input().strip().split())
mergeSort(myArray)
print myArray
