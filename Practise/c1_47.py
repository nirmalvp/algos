 #47) Given N points, every line go through 2 point, write code to find the line with largest slope.

def findMaxSlope(points):
	maxSlope = 0
	for index,firstPoint in enumerate(points):
		(x1,y1) = firstPoint
		for secondPoint in points[index+1 : ]:
			(x2,y2) = secondPoint
			diffY = y2-y1
			diffX = x2- x1
			if diffX == 0 :
				print "Slope of %s and %s is undefined "%(firstPoint, secondPoint)
				continue 
			slope = diffY / float(diffX) 
			print "Slope of %s and %s = %s "%(firstPoint, secondPoint, slope) 
			if slope > maxSlope:
				maxSlope = slope
				pointsContainingMaxSlope = (firstPoint,secondPoint)
	return (maxSlope,pointsContainingMaxSlope)

def main():
	numberOfPoints = input("Number of points")
	points = list()
	for i in range(numberOfPoints):
		(x,y) = map(int,raw_input("Enter the x,y cordinates").split())
		points.append((x,y))
	maxSlope, pointsContainingMaxSlope = findMaxSlope(points)
	print "MaxSlope = %s, Points are %s and %s "%(maxSlope, pointsContainingMaxSlope[0], pointsContainingMaxSlope[1]) 

main()






