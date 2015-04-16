class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __str__(self):
		return "( %s, %s )"%(self.x,self.y)
	def subtract(self,point):
		return Point(self.y - point.y , self.x - point.x)

class Line:
	def  __init__(self,yc,xc,c):
		
		self.yc = yc
		self.xc = xc
		self.c= c 

def  createLine(point1,point2):
	yc = point1.x - point2.x
	xc = point2.y - point1.y
	c = yc * point1.y + xc * point1.x
	return Line(yc,xc,c)


def findIntersection(line1,line2):
	det= line2.xc * line1.yc - line1.xc * line2.yc
	if(det == 0 ):
        return None;
	x = (line2.xc * line1.c - line1.xc * line2.c)/det
	y = (line1.yc * line2.c - line2.xc * line1.c) / det
	return Point(x,y)
 
 def findReflection(line,point):
 	perpYc = line.xc
 	perpXc = - line.yc
 	perpC = point.y * perpYc + point.x * perpXc
 	perpendicular = Line(perpYc, perpXc, perpC)
 	midpoint = findIntersection(line,perpendicular)
 	return midpoint.subtract( point.subtract(midpoint) )

points= []
for i in range(4):
	p=raw_input("Point %s:" %(i+1))
	x,y = tuple(int(i) for i in p.replace(" ","").split(','))
	points.append(Point(x,y))

line1= createLine(points[0],points[1])
line2= createLine(points[2],points[3])

print (findIntersection(line1,line2) or "Parallel Lines")







