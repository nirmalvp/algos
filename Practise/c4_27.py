#27) Given a rotated sorted array, the element might appears in the order 3,4,5,6,7,1,2. 
#How would you find the minimum element

def findMinElement(array,low,high):
	while low <= high :
		if low == high :
			return array[low]
		mid = (low + high) >> 1
		if array[mid] < array[mid-1]: # Check if middle element is the smallest 
			return array[mid]
		if array[mid+1] < array[mid]: # CHeck if the next to middle element is the smallest. 
		#Ex : [4 5 6 1 2 3]-> mid = 2 ,if we dont check this condition, we end up with [1 2 3]
		#in next iteration and wont get the result
			return array[mid+1]
		if array[high] < array[mid] : # Check if transition has happened between mid and high
			low = mid+1
		else :
			high = mid - 1
def main():
	array = map(int,raw_input("Enter sorted rotated array").split())
	print findMinElement(array,0,len(array)-1)
main()

