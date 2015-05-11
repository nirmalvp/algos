def findShortestPath(array,index):
	if index == len(array) - 1:
		return 0
	if index >= len(array):
		return None
	jumpLength = array[index]
	if jumpLength == 0:
		return
	shortestPath = len(array)
	isPathExist = False
	for length in range(1,jumpLength+1):
		shortestPathfromIndexPlusLength = findShortestPath(array,index+length)
		if shortestPathfromIndexPlusLength != None:
			isPathExist = True
			shortestPath = min(shortestPath,shortestPathfromIndexPlusLength)
	if isPathExist:
		return 1+shortestPath
	return None


def main():
	array = map(int, raw_input("Enter the array").split())
	print findShortestPath(array,0) or "No path to last element"

main()
