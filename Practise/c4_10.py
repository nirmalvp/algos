#10) Given an m*n grid, how many paths are there from the left bottom corner to the up right corner.

def memoize(f):
	memo = dict()
	def wrapper(row,column):
		if memo.get((row,column)) == None:
			result = f(row,column)
			memo[(row,column)] = result
		return memo.get((row,column))
	return wrapper

@memoize
def countPathToTopLeft(row,column):
	if row < 0 or column < 0 :
		return 0
	if row==0 and column == 0 :
		return 1
	return countPathToTopLeft(row-1,column) + countPathToTopLeft(row ,column - 1)

def main():
	x,y = map(int,raw_input("Enter the number of rows and columns of the grid").split())
	print "Number of paths from (%s, %s) t0 (0, 0) = %s "%(x-1,y-1,countPathToTopLeft(x-1,y-1))
main()