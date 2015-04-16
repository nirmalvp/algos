#Implementing Heap Sort
def leftNode(index):
	return (index << 1) + 1

def rightNode(index):
	return (index<<1) + 2


def maxHeapify(myArray,parent,heapSize):
	left = leftNode(parent)
	right = rightNode(parent)
	biggest = parent
	if(left < heapSize and myArray[left] > myArray[biggest]):
		biggest = left
	if(right < heapSize and myArray[right] > myArray[biggest]):
		biggest = right
	if(biggest != parent):
		myArray[parent], myArray[biggest] = myArray[biggest], myArray[parent]
		maxHeapify(myArray,biggest,heapSize)
	

def buildMaxHeap(myArray):
	for i in reversed( range(len(myArray)/2) ):
		maxHeapify(myArray,i,len(myArray))
		

def heapSort(myArray):
	heapSize = len(myArray)  
	buildMaxHeap(myArray)
	for i in reversed( range( 1,len(myArray) ) ):
		myArray[i], myArray[0] = myArray[0], myArray[i]
		heapSize = heapSize - 1
		maxHeapify(myArray,0,heapSize)
	return myArray

print heapSort([4,1,3,2,16,9,10,14,8,7])





