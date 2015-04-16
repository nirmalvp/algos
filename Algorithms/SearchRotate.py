#Search for an element in sorted and rotated array in less than O(n) time
myArr = [4,5,1,2,3]
searchElement = int(raw_input())

def search(low,high):
	print myArr[low:high+1]
	mid= ( low+high )/2
	if(myArr[mid] == searchElement):
		return mid
	if(low > high):
		return
	if(myArr[low]<=myArr[mid]): #sorted half?
		if(myArr[low] <= searchElement <= myArr[mid]):
			return search(low,mid-1)
		else:
			return search(mid+1,high)
	elif(myArr[mid+1] <= searchElement <= myArr[high]):
		return search(mid+1,high)
	else:
		return search(low,mid-1)

print search(0,len(myArr)-1)
