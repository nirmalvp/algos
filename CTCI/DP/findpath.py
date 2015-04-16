x,y  = map(int,raw_input("Enter x and y :").split())

def findPath(x,y,path):
	q = path[:]
	q.append((x,y))
	if(x==0 and y==0):
		print q
		print "_"*10
		return 1
	if(x < 0 or y < 0):
		return 0
	count = findPath(x-1,y,q) + findPath(x,y-1,q)
	return count

print findPath(x,y,[])