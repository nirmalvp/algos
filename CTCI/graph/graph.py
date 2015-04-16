class Graph:
	def __init__(self,graphList):
		self.vertices = {}
		for vertexName in graphList.keys():
			self.createVertex(vertexName)
		for vertexName in graphList.keys():
			source = self.getVertex(vertexName)
			for adj in graphList[vertexName]:
				source.adjacent.append(self.getVertex(adj))
	
	def createVertex(self,vertexName):
		vertex = Vertex(vertexName)
		self.vertices[vertex.name] = vertex
	
	def getVertex(self,name):
		return self.vertices.get(name)


class Vertex:
	def __init__(self, name):
		self.parent = None
		self.d = None
		self.color = 'white'
		self.name = name
		self.adjacent = []
	def __str__(self):
		return self.name
	def __repr__(self):
		return self.name
