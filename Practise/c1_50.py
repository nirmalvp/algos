def isOrthogonal(pointOne, pointTwo, pointThree) :
	x1, y1 = pointOne
	x2, y2 = pointTwo
	x3, y3 = pointThree
	if (y2-y1) * (y3-y2) == (x2-x3) * (x2 - x1) : #m1m2 = -1
		return True
	return False

def isRectangle(pointa, pointb, pointc, pointd):
	return isOrthogonal(pointa,pointb,pointc) and isOrthogonal(pointb,pointc,pointd) and isOrthogonal(pointc,pointd,pointa)

def isRectangleAnyOrder(pointa, pointb, pointc, pointd):
	#Keeping d constant, all valid distinct orthogonal combinations of a,b,c.
	#ie ab Pr bc , ac Pr bc , ac Pr ab ; Pr = Perpendicular
	return isRectangle(pointa,pointb,pointc,pointd) or isRectangle(pointa,pointc,pointb,pointd) or isRectangle(pointc,pointa,pointb,pointd)

def calculateDistance(cm,point):
	cmx,cmy = cm
	x,y = point
	return (cmx-x)**2 + (cmy-y)**2

def isRectangleUsingCentreOfMass(pointOne, pointTwo, pointThree, pointFour):
	x1, y1 = pointOne
	x2, y2 = pointTwo
	x3, y3 = pointThree
	x4, y4 = pointFour
	centreOfMass =( (x1+x2+x3+x4) / 4.0 , (y1+y2+y3+y4 ) / 4.0 )
	if ( calculateDistance(centreOfMass,pointOne) == calculateDistance(centreOfMass,pointTwo) 
		== calculateDistance(centreOfMass,pointThree) == calculateDistance(centreOfMass,pointFour) ) :
		return True
	return False



def main():
	points = list()
	for i in range(4):
		pointList = map(int,raw_input("Enter x y separeted by spaces").split())
		points.append(tuple(pointList))
	print isRectangleAnyOrder(*points) , " Using isRectangleAnyOrder fn"
	print isRectangleUsingCentreOfMass(*points) , " Using CentreOfMass fn"
main()