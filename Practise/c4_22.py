#22) Given an int array a[], find the two numbers A and B so that the absolute value |A-B| is the smallest. 
# The time complexity should be O(NlogN).
def findClosest(array):
	array.sort()
	shortestDistance = abs(array[1] - array[0]) 
	closestPair = (array[0],array[1])
	for element,nextElement in zip(array,array[1:]):
		distance = abs(nextElement - element)
		if distance < shortestDistance:
			closestPair = (element,nextElement)
			shortestDistance = distance
	return closestPair
def main():
	array = map(int,raw_input("Enter the array").split())
	if len(array) < 2 :
		print "Not enough elements"
	else:
		print "closestPair = %s,%s "%findClosest(array)
main()
	