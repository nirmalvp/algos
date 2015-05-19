#58) Given an array, write code to find how many increasing sub array could generated from it. [MS]
#        such as: Given {1,2,3}, it could generate {1,2}, {1,3}, {2,3}, {1,2,3}, 4 increasing sub array.

def findIncreasingSubarray(array):
	if not array :
		return
	firstElement = array[0]
	yield (firstElement,)
	for prevIncreasingSubarray in findIncreasingSubarray(array[1:]):
		yield prevIncreasingSubarray
		length = len(prevIncreasingSubarray)
		index = 0 
		while index < length and firstElement > prevIncreasingSubarray[index]: #Find the location where firstElement
		#can be inserted into the previous set
			index += 1
		yield prevIncreasingSubarray[:index] + (firstElement,) + prevIncreasingSubarray[index:]
def main():
	array = map(int,raw_input("enter the array").split())
	print [element for element in findIncreasingSubarray(array) if len(element)>1]
main()

