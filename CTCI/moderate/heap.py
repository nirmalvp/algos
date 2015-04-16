class Heap():
    
    def __init__(self,heapProperty):
        self.data = list()
        self.heapSize = 0
        self.f = heapProperty
    
    def heappush(self,num):
        self.data.insert(0,num)
        self.heapSize +=1
        self.siftDown(0)
    
    def swap(self,firstIndex,secondIndex):
        self.data[firstIndex],self.data[secondIndex] = self.data[secondIndex], self.data[firstIndex]
    
    def heappop(self):
        if(self.heapSize==0):
            print "No element to pop"
            return
        if(self.heapSize==1):
            temp = self.get(0)
            self.data = list()
            self.heapSize=0
        else:
            temp = self.get(0)
            self.swap(self.heapSize-1,0)
            self.heapSize -=1
            self.siftDown(0)
        return temp
    
    def leftNode(self,index):
        return (index << 1) + 1
    
    def rightNode(self,index):
        return (index<<1) + 2

    def get(self,index):
        if index < self.heapSize:
            return self.data[index]
        return None
    
    def isEmpty(self):
        return self.heapSize == 0
    
    def peek(self):
        return self.data[0]
    
    def showElements(self):
        return self.data[:self.heapSize]

    def siftDown(self,parent):
        leftChild = self.leftNode(parent)
        rightChild = self.rightNode(parent)
        smallestOrLargest = parent
        if leftChild < self.heapSize:
            smallestOrLargest = self.f(parent,leftChild, key = self.get)
        if rightChild < self.heapSize:
            smallestOrLargest = self.f(smallestOrLargest,rightChild, key = self.get)
        if(parent != smallestOrLargest):
            self.swap(parent,smallestOrLargest)
            self.siftDown(smallestOrLargest)

