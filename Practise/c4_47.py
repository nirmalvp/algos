#47) Given an sorted array of integer, write code to find the occurrences of a given number.

def findFirstOccurence(low,high,array,element):
	while(low <= high):
		mid = (low+high) >> 1
		if array[mid] == element and (mid==0 or array[mid-1] != element):
			return mid
		if element <= array[mid]:
			high = mid-1
		else :
			low = mid+1
def findLastOccurence(low,high,array,element):
	length  = len(array)
	while(low <= high):
		mid = (low+high) >> 1
		if array[mid] == element and (mid==length-1 or array[mid+1] != element):
			return mid
		if element < array[mid]  :
			high = mid-1
		else :
			low = mid+1
def main():
	array = map(int,raw_input("Enter the array").split())
	element = input("Enter the element who occurrences is to be counted")
	print (findLastOccurence(0,len(array)-1,array,element) - findFirstOccurence(0,len(array)-1,array,element) + 1 )

main()