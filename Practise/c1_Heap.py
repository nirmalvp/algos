#13) Numbers are randomly generated and stored in an array. How would you keep track of the median.

class Heap():
	def __init__(self,heapProperty):
		self.f = heapProperty
		self.data = list()
		self.heapSize = 0
	def get(self,index):
		return self.data[index]
	def isEmpty(self):
		return self.heapSize == 0
	def heapPush(self,num):
		self.data.insert(0,num)
		self.heapSize += 1
		self.siftDown(0)
	def heapPop(self):
		if(self.heapSize == 0):
			return
		if(self.heapSize == 1):
			temp =self.get(0)
			self.data=list()
			self.heapSize=0
		else:
			temp = self.get(0)
			self.swap(0,self.heapSize - 1)
			self.heapSize -= 1
			self.siftDown(0)
		return temp
	def top(self):
		return self.get(0)
	def showElements(self):
		print self.data[:self.heapSize]

	def swap(self,firstIndex,secondIndex):
		self.data[firstIndex],self.data[secondIndex] = self.data[secondIndex], self.data[firstIndex]
	def leftChild(self,index):
		return (index<<1)+ 1
	def rightChild(self,index):
		return (index<<1) + 2
	def siftDown(self,parent):
		leftChild = self.leftChild(parent)
		rightChild = self.rightChild(parent)
		maxOrMinElementIndex = parent
		if(leftChild < self.heapSize):
			maxOrMinElementIndex = self.f( maxOrMinElementIndex,leftChild, key = self.get )
		if(rightChild < self.heapSize):
			maxOrMinElementIndex = self.f(maxOrMinElementIndex, rightChild, key = self.get )
		if(maxOrMinElementIndex != parent):
			self.swap(parent,maxOrMinElementIndex)
			self.siftDown(maxOrMinElementIndex)
	
			

		