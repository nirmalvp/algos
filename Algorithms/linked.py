class Node(object):
	def __init__(self,data = None):
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
		nextItem = None
		while(current != None):
			nextItem = current.nextItem
			current.nextItem = prev
			prev = current
			current=nextItem
		self.first=prev
	
	def reverseEveryN(self,n):
		saveFirst = True
		if(self.first == None):
			return
		if(n<2):
			return
		lastNode = self.first
		current = self.first
		while (current !=None) :
			firstNode=current
			count = 0
			prev = None
			while (current != None and count < n):
				nextItem = current.nextItem
				current.nextItem = prev
				prev = current
				current = nextItem
				count += 1
			if(saveFirst):
				lastNode=firstNode
				saveFirst = False
				self.first= prev
			else:
				lastNode.nextItem = prev
			firstNode.nextItem = current




			

myList=LinkedList();
myList.insert(1);
myList.insert(2);
myList.insert(3);
myList.insert(4)
myList.insert(5)
myList.insert(6)
myList.insert(7)
myList.display()
myList.reverse()
myList.display()
myList.reverseEveryN(3)
myList.display()








