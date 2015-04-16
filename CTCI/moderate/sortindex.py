#Question 17.6
myArray = map(int, raw_input("enter the list : ").split())
#Find the point where unsorted elements start
for startIndex,startItem in enumerate(myArray):
	if(startItem > myArray[startIndex+1]):
		break

for index,item in enumerate(myArray[startIndex:],startIndex):
	if(item<=startItem):
		endItem = item
		endIndex = index

for index,item in enumerate(myArray):
	if(item >= endItem):
		startIndex = index
		startItem = item
		break

print "startIndex = %s, startItem = %s \nendIndex = %s, endItem = %s"%(startIndex,startItem,endIndex,endItem)







