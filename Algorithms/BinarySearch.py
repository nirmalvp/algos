sortedNum = map(int,raw_input("Enter the list").split())
def binarySearch(low, high):
	
	if(low > high):
		return None
	mid = (low + high)/2
	
	if(key == sortedNum[mid]):
		return mid
	
	if(key < sortedNum[mid]):
		return binarySearch(low,mid-1)
	
	if(key > sortedNum [mid]):
		return binarySearch(mid+1, high)

while(1):
	key = int(raw_input("Key : "))
	print binarySearch(0,len(sortedNum)-1) 

