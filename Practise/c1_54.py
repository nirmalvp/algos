def isAboveOneAnother(rect1TopLeftY,rect1BottomRightY,rect2TopLeftY,rect2BottomRightY):
	return rect1TopLeftY < rect2BottomRightY or rect2TopLeftY < rect1BottomRightY 
def isAsideOneAnother(rect1TopLeftX,rect1BottomRightX,rect2TopLeftX,rect2BottomRightX):
	return rect1TopLeftX > rect2BottomRightX or rect1BottomRightX < rect2TopLeftX 

def overlap(rect1,rect2):
	rect1TopLeftPoint, rect1BottomRightPoint = rect1
	rect1TopLeftX, rect1TopLeftY = rect1TopLeftPoint
	rect1BottomRightX , rect1BottomRightY = rect1BottomRightPoint
	rect2TopLeftPoint, rect2BottomRightPoint = rect2
	rect2TopLeftX, rect2TopLeftY = rect2TopLeftPoint
	rect2BottomRightX , rect2BottomRightY = rect2BottomRightPoint
	if (isAboveOneAnother(rect1TopLeftY,rect1BottomRightY,rect2TopLeftY,rect2BottomRightY) 
		or isAsideOneAnother(rect1TopLeftX,rect1BottomRightX,rect2TopLeftX,rect2BottomRightX)):
		return "Rectangles don't overlap"
	else:
		return "Rectangles Overlap"

def main():
	rects=list()
	for i in range(2):
		topleft = tuple(map(int,raw_input("Enter Top Left cordinate for Rect %s:"%(i+1)).split()))
		bottomright = tuple(map(int,raw_input("Enter Bottom Right cordinate for Rect %s:"%(i+1)).split()))
		rect=(topleft,bottomright)
		rects.append(rect)
	print overlap(*rects)
main()










