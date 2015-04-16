#18.10
import string
from collections import defaultdict
with open("wordsEn.txt") as f:
	a=f.read()
myDict=set(a.split())

def createGraph():
	wordCombinations = defaultdict(list)
	for word in myDict:
		for pos,_ in enumerate(word):
			for char in string.ascii_lowercase:
				oneLetterChanged = word[:pos] + char + word[pos+1:]
				if oneLetterChanged in myDict	and oneLetterChanged != word :
					wordCombinations[word].append(oneLetterChanged)
	return wordCombinations

def findPath(wordGraph,source,destination):
	if( wordGraph.get(source) == None or wordGraph.get(destination) ==None ) :
		print startWord," or ",endWord," doesnt exist in the dictionary"
	discovered =set()
	parent = dict()
	queue = []
	queue.append(startWord)
	discovered.add(startWord)
	while(queue):
		element =queue.pop(0)
		for adj in  wordGraph.get(element):
			if(adj not in discovered):
				parent[adj] = element
				discovered.add(adj)
				queue.append(adj)
				if(adj == destination):
					return parent
	return None

wordGraph = createGraph()
startWord = raw_input("startWord")
endWord = raw_input("endWord")
parent = findPath(wordGraph,startWord,endWord)
#print parent
if parent:
	path = list()
	curr = endWord
	while curr:
		path.append(curr)
		curr = parent.get(curr)
	while path:
		print "%s--->"%path.pop(),
else :
	print "No path found"





