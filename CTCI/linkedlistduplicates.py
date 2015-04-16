from linkedlist import LinkedList

def removeDup(self):
	myDict={}
	temp = self.first
	myDict[temp.data] =1
	while(temp.next!=None):
		val = temp.next.data
		if(myDict.get(val)!=None):
			temp.next = temp.next.next
		else :
			myDict[val] = 1
		temp= temp.next
		
LinkedList.removeDup = removeDup
myList = LinkedList()
myList.insertNode(1)
myList.insertNode(1)
myList.insertNode(2)
myList.insertNode(1)
myList.insertNode(3)

myList.removeDup()
myList.display()



