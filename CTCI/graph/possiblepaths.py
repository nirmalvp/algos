from graph import Graph
graphInput={
	'r' : ['s','v'],
	's' : ['r','w'],
	't' : ['u','w','x'],
	'u' : ['t','x','y'],
	'v' : ['r'],
	'w' : ['s','t','x'],
	'x' : ['t','u','w','y'],
	'y' : ['u','x']
}

graph=Graph(graphInput)

def bfs_possiblePath(start,end):
	startVertex = graph.getVertex(start)
	possiblePath = []
	possiblePath.append([startVertex])
	while possiblePath:
		path = possiblePath.pop(0)
		lastNodeInPath = path[-1]
		if(lastNodeInPath.name == end):
			print "valid path : ",path #path directly print vertex.name because Vertex.__repr__() is overriden to return self.name
		for adj in lastNodeInPath.adjacent:
			if adj not in path:
				newPath = list(path)
				newPath.append(adj)
				possiblePath.append(newPath)
bfs_possiblePath('t','w')


