#9) Given an array, there is an element whose occurence is greater than the half of the array's length, find this element.
#https://stackoverflow.com/questions/7059780/find-the-element-repeated-more-than-n-2-times
def findMajorityElement(array):
	majorityElement = array[0]
	count = 1
	for element in array[1:]:
		if element == majorityElement :
			count += 1
		else:
			count = count - 1
		if count == 0 :
			majorityElement = element
			count = 1
	return majorityElement
def main():
	array = map(int,raw_input("Enter the elements of array : ").split())
	print findMajorityElement(array)
main()