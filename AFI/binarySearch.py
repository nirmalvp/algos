def binarySearchRange(myArray,num):
	high = 0
	exp = 0
	try:
		while myArray[high]<=num :
			if myArray[high] == num :
				return "Found", high                                                        
			high = 2 ** exp
			exp += 1
	except IndexError:
		pass
	return (high/2, high)

def binarySearch(myArray,num,low,high):
	while(low<=high):
		mid = (low + high)/2
		try:
			if myArray[mid] == num :
				return mid
			elif num > myArray[mid]:
				low = mid + 1
			else:
				high = mid - 1
		except IndexError:
			print "IndexError at ", high
			high = mid - 1
	return -1

myArray = map(int,raw_input("enter List").split())
num = input("Search element")

low, high = binarySearchRange(myArray,num)
if(low == "Found"):
	print "During range fnd"
	print "%s found as %s"%(num,high)
else:
	print low,high
	index = binarySearch(myArray,num,low,high)
	if index == -1:
		print "%s not found"%num
	else:
		print "%s found at %s "%(num,index)



