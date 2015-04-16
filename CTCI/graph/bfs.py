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



def bfs(source):
	queue=[]
	sourceVertex = graph.getVertex(source)
	sourceVertex.color = 'grey'
	sourceVertex.d = 0
	queue.append(sourceVertex)
	while (queue):
		vertex = queue.pop(0)
		for adj in vertex.adjacent:
			#print vertex.name ,adj.name
			if(adj.color == 'white'):
				adj.color = 'grey'
				adj.parent = vertex
				adj.d = vertex.d + 1
				queue.append(adj)
		vertex.color = 'black'
		print "Name=%s , parent = %s , depth = %s"%(vertex.name,vertex.parent and vertex.parent.name,vertex.d)
		

graph= Graph(graphInput)
bfs('s')

