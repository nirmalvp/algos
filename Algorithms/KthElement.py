#Find kth smallest and Largest element in an unsorted list
def quickSelectSmallest(myArr,k):
	pivot=myArr[0]
	smallArr = [x for x in myArr if x < pivot]
	largeArr = [x for x in myArr if x > pivot]


	if(k <= len(smallArr)):
		return quickSelectSmallest(smallArr,k)
	elif(k > len(smallArr)+1 ):
		return quickSelectSmallest( largeArr, k - (len(smallArr)+1) )
	else :
		return pivot

def quickSelectLargest(myArr,k):
	pivot=myArr[0]
	smallArr = [x for x in myArr if x < pivot]
	largeArr = [x for x in myArr if x > pivot]


	if(k <= len(largeArr)):
		return quickSelectLargest(largeArr,k)
	elif(k > len(largeArr) + 1 ):
		return quickSelectLargest(smallArr, k - (len(largeArr)+1))
	else :
		return pivot

myArr = map(int,raw_input("Enter the list :").strip().split())
k =int(raw_input("Enter value of k(Kth smallest and largest)"))
print "List sorted for output verification: ", (sorted(myArr))
print "Kth Smallest: ",quickSelectSmallest(myArr,k)
print "Kth Largest: ",quickSelectLargest(myArr,k)


