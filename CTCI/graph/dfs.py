from graph import Graph, Vertex
Vertex.discTime = 0
Vertex.finalTime =0
time =0 
def dfs():
	for key in graph.vertices.keys():
		vertex = graph.getVertex(key)
		if(vertex.color == 'white'):
			dfs_visit(vertex)

def dfs_visit(vertex):
	global time
	time =time+1
	vertex.discTime = time
	vertex.color = 'grey'
	for adj in vertex.adjacent :
		if(adj.color == 'white'):
			adj.parent = vertex
			dfs_visit(adj)
	vertex.color='black'
	time+=1
	vertex.finalTime=time
	print "Name=%s , parent = %s , time = %s/%s"%(vertex.name,vertex.parent and vertex.parent.name,vertex.discTime,vertex.finalTime)



graphMap ={
	'u' : ['v','x'],
	'v' : ['y'],
	'x' : ['v'],
	'y' : ['x'],
	'w': ['y','z'],
	'z' :['z']
}

graph=Graph(graphMap)
dfs()
