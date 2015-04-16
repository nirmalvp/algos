from heap import Heap
from random import randint

maxHeap = Heap(max)
minHeap = Heap(min)
numTillNow = list()
def findMedian(num):
    numTillNow.append(num)
    if minHeap.isEmpty() and maxHeap.isEmpty(): #First element
        maxHeap.heappush(num)
    elif num < maxHeap.peek():
        maxHeap.heappush(num)
        if maxHeap.heapSize > minHeap.heapSize+1 :
            minHeap.heappush(maxHeap.heappop())
    else:
        minHeap.heappush(num)
        if minHeap.heapSize > maxHeap.heapSize:
            maxHeap.heappush(minHeap.heappop())
    
    print "minHeap",minHeap.showElements(),minHeap.heapSize
    print "maxHeap",maxHeap.showElements(),maxHeap.heapSize
    print "Numbers TillNow",numTillNow
    if(maxHeap.heapSize == minHeap.heapSize):
        median = (maxHeap.peek()+minHeap.peek())/2
    else:
        median = maxHeap.peek()
    print "median of",sorted(numTillNow), " = ",median

while True:
    num = randint(1,1000)
    print "randNum",num
    findMedian(num)
    h=raw_input()



