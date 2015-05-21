# 75) Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below. [LeetCode]
#         For example, given the following triangle
#         [
#              [2],
# #            [3,4],
# #           [6,5,7],
# #          [4,1,8,3]
# #        ]
# #        The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
def memoize(f):
	memo = dict()
	def wrapper(row,col,triangle,maxrow):
		if memo.get((row,col)) is None:
			memo[(row,col)] = f(row,col,triangle,maxrow)
		return memo.get((row,col))
	return wrapper

@memoize	
def findSmallestPath(row,col,triangle,maxrow):
	element = triangle[row][col]
	if row == maxrow:
		return ((triangle[row][col],),triangle[row][col]) #(Route,minimumSum)
	else :
		left = findSmallestPath(row+1,col,triangle,maxrow)
		right = findSmallestPath(row+1,col+1,triangle,maxrow)
		bestRoute = min(left,right,key = lambda x : x[1])
		return ((element,) + bestRoute[0] , bestRoute[1] + element) #(Route,minimumSum)
def main():
	triangle = [[2],[-3,4],[6,5,-7],[4,1,8,3]]
	numberofRows = len(triangle) - 1
	route,minimumSum = findSmallestPath(0,0,triangle,numberofRows)
	print "Route = ",route, ", minimum Sum = ",minimumSum
main()


