#ven an int array a[], find two numbers A and B so that the absolute value |A-B| is the biggest. 
#The time complexity should be O(N).

def findFarthestPair(array):
	smallestNum = array[0]
	largestNum = array[0]
	for element in array[1:]:
		if element < smallestNum:
			smallestNum = element
		if element > largestNum :
			largestNum = element
	return smallestNum,largestNum

def main():
	array = map(int,raw_input("Enter the array").split())
	if len(array) < 2 :
		print "Not enough elements"
	else :
		print "Farthest pair = %s, %s"%findFarthestPair(array)
main()