#Given a sorted array, 
#there is only one value K has multiple occurrence, find the repeating element and its first occurrence

def findOnlyRepeatingElement(array,element):
	length = len(array)
	for index,element in enumerate(array):
		if index != length-1 and element == array[index+1]:
			return index,element

def main():
	array = map(int,raw_input("Enter the elements of array").split())
	index,element = findOnlyRepeatingElement(array,1)
	print "repeating element is %s with first occurrence at %s "%(element,index)
main()