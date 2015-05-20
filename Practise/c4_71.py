#71) Given an array, find the max K element in the array.
#http://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/
import random
class MinHeap(object):
	def __init__(self,iterable):
		self.data = iterable[:]
		self.heapsize = len(self.data) 
	def siftDown(self,parent):
		left = (parent << 1) + 1
		right = (parent >> 1) + 2
		indexOfMinNumber = parent
		if left < self.heapsize:
			indexOfMinNumber = min(parent,left,key = lambda x : self.data[x])
		if right < self.heapsize:
			indexOfMinNumber = min(indexOfMinNumber,right,key = lambda x : self.data[x])
		if indexOfMinNumber != parent :
			self.data[parent],self.data[indexOfMinNumber] = self.data[indexOfMinNumber],self.data[parent]
			self.siftDown(indexOfMinNumber)
	def heapify(self):
		for index in reversed(xrange(0,self.heapsize/2)):
			self.siftDown(index)
#Logic : Create a temp array the same size of k. If any element found which is greater than the least element in the
#temp array,replace it with the element
def main():
	array = map(int,raw_input("Enter the array").split())
	k = input("Enter K (K max elements will be returned) : 1")
	minHeap = MinHeap(array[:k])
	minHeap.heapify()
	for element in  array[k:] :
		if element > minHeap.data[0]:
			minHeap.data[0] = element
			minHeap.siftDown(0)
	print k," largest element of",array," = ",minHeap.data
main()

