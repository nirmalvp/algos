class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
	def __repr__(self):
		return self.data

class LinkedList:
	def __init__(self):
		self.first = None

	def insertNode(self,data):
		newNode=Node(data)
		if(self.first==None):
			self.first = newNode
		else :
			temp=self.first
			while(temp.next != None):
				temp = temp.next
			temp.next = newNode

	def deleteNode(self,data):
		if(self.first == None):
			print "Empty Link List"
			return 
		if(data == self.first.data):
			self.first = self.first.next
			return
		temp =self.first
		while(temp.next!=None):
			if(temp.next.data == data):
				temp.next= temp.next.next
			else:
				temp = temp.next
	
	def reverse(self):
		current = self.first
		previous = None
		while(current.next != None):
			nextItem = current.next
			current.next = previous
			previous = current
			current = nextItem
		current.next = previous
		self.first = current

	def display(self):
		if(self.first == None):
			return
		temp = self.first
		while(temp != None):
			print "%s "%(temp.data),
			temp=temp.next
		print 
                



