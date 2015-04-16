from Heap import Heap
from random import randrange
def findMedian(num):
	numTillNow.append(num)
	if(maxHeap.isEmpty() and minHeap.isEmpty()):
		maxHeap.heapPush(num)
	elif num <= maxHeap.top():
		maxHeap.heapPush(num)
		if(maxHeap.heapSize > minHeap.heapSize + 1):
			minHeap.heapPush(maxHeap.heapPop())
	else :
		minHeap.heapPush(num)
		if(minHeap.heapSize > maxHeap.heapSize):
			maxHeap.heapPush(minHeap.heapPop())
	if maxHeap.heapSize == minHeap.heapSize:
		median = ( maxHeap.top() + minHeap.top() )/ 2
	else :
		median = maxHeap.top()	
	print "Median of %s = %s"%(sorted(numTillNow), median ) 

maxHeap = Heap(max)
minHeap = Heap(min)
numTillNow = list()

while True:
	num = randrange(0,1000)
	findMedian(num)
	if raw_input("Press enter for next iteration, q To quit ") == 'q' :
		break
