class Node(object):
    def __init__(self,data):
        if(data!=None):
            self.data=data
        self.nextItem=None


class LinkedList(object):
    def __init__(self):
        self.first=None


    def insert(self,data):
        item=Node(data);
        item.nextItem=self.first
        self.first=item

    def delete (self,data):
        if (self.first is None):
            print "Nothing to delete"
            return
        current=self.first 
        
        if(self.first.data == data):
            self.first=self.first.nextItem
            return

        while current.data !=data:
            prev=current
            current=current.nextItem
        
        prev.nextItem=current.nextItem
        
    def display(self):
        current=self.first

        while current is not None:
            print current.data," ",
            current=current.nextItem
        print "\n"

    def reverse(self):
        current = self.first
        prev=None
        nextItem = current.nextItem
        while(nextItem != None):
            current.nextItem = prev
            prev = current
            current=nextItem
            nextItem = current.nextItem
        current.nextItem = prev
        self.first = current
        

    def reverseEveryK(self,k):
        traversalNode = self.first
        if( traversalNode == None ):
            return
        def reverseKElements():
            current = traversalNode
            prev = None
            nextItem = current.nextItem
            iter = k 
            while(nextItem != None and iter != 1):
                current.nextItem = prev
                prev = current
                current=nextItem
                nextItem = current.nextItem
                iter -= 1
            current.nextItem = prev
            #Original first element moved to last position. So, link it with the first element of the next sublist to continue traversal
            traversalNode.nextItem = nextItem 
            return current #Return the new first element of sublist

        self.first = reverseKElements()
        while traversalNode.nextItem != None :
            lastListTail = traversalNode 
            traversalNode = traversalNode.nextItem
            #Store the tail of the last subList and link it with the first element of the sublist created after reversal
            lastListTail.nextItem= reverseKElements()
            
            
myList=LinkedList();
insertArray= [1,2,3,4,5,6,7,8]
for i in insertArray:
    myList.insert(i)
myList.display()
myList.reverse()
myList.display()
myList.reverseEveryK(3)
myList.display()
