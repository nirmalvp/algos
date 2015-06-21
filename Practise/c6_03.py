#3) Print the minimum spanning tree of a graph

class DisjointSet(object):
	def __init__(self):
		self.parent = self
		self.rank = 0

def findSet(node):
	if node.parent != node :
		node.parent = findSet(node.parent)
	return node.parent

def union(elementOne,elementTwo):
	#Find the parent(representative element) of the disjoint set and then combine them into one.
	merge(findSet(elementOne), findSet(elementTwo))

def merge(setOneRoot,setTwoRoot):
	if setOneRoot.rank > setTwoRoot.rank :
		setTwoRoot.parent = setOneRoot
	else :
		setOneRoot.parent = setTwoRoot
		if setTwoRoot.rank == setOneRoot:
			setTwoRoot.rank += 1
def MST(edges, disjointSet):
	for edge in sorted(edges,key = lambda x : x[2]) :
		getVertex =  lambda vertexOne, vertexTwo,_ : (disjointSet.get(vertexOne), disjointSet.get(vertexTwo))
		vertexOne, vertexTwo = getVertex(*edge) 
		if findSet(vertexOne) != findSet(vertexTwo):
			yield edge
			union(vertexOne,vertexTwo)

def main():
	vertices = "abcdefghi"
	disjointSet = {vertex:DisjointSet() for vertex in vertices}
	edges = ([('a','b',4), ('a','h',8),('b','c','8'),('b','h',11),('c','d',7),('c','f',4),('c','i',2),('d','e',9),
		('d','f',14),('e','f',10),('f','g',2), ('g','i',6),('g','h',1),('h','i',7)])
	print list(MST(edges,disjointSet))

main()
	
	

