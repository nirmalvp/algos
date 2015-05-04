#62) Given N point in two dimentional space, find the closest two points.
#Wont Work Needs Adjustments
def findElementsToBeConsidered(minLeftSide,minRightSide,middlePointX):
	selementsToBeConsidered = [(x,y) for (x,y) in points if abs(x - middlePointX) <= minTillNow]
	return elementsToBeConsidered

def findDistance(pointOne,PointTwo):
	x1, y1 = pointOne
	x2, y2 = PointTwo
	return ( (y2-y1)**2 + (x2-x1)**2 ) ** 0.5

def minAcrossMedian(elementsToBeConsidered,minTillNow):
	elementsToBeConsidered.sort(key = lambda point : point[1]) #Sort by Y co-ordinate
	minAcrossMedian = minTillNow
	for index, point in enumerate(elementsToBeConsidered) :
		j = index+1
		while True :
			nextPointY = elementsToBeConsidered[j][1]
			if nextPointY - point[1] >= minTillNow:
				break
			distance = findDistance(point,nextPointY)
			if distance < minAcrossMedian:
				minAcrossMedian = distance
			j += 1

def findShortestDistance(pointList,startIndex,endIndex):
	mid = (startIndex + endIndex) / 2
	middlePointX = pointList[mid][0]
	minLeftSide = findShortestDistance(startIndex,mid)
	minRightSide = findShortestDistance(mid+1,endIndex)
	minTillNow = min(minLeftSide,minRightSide)
	elementsToBeConsidered = findElementsToBeConsidered(minTillNow,middlePointX,pointList)
	minAcrossMedian = findMinAcrossMedian(elementsToBeConsidered, minTillNow)
	return min(minTillNow,minAcrossMedian)

def main():
	points = raw_input("Enter set of points seperated by spaces eg : 1,2 3,4 :").split()
	pointList = [ tuple( map(int,point.split(',')) ) for point in points ]
	pointList.sort()
	print findDistance(pointList,0,len(pointList)-1)
	
	
