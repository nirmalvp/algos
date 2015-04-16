# 32) Given a capacity value N, and a set of different Item types with values v1, v2, ...,vn
#          1) Existence Check: check whether N can be filled with a certain combination of items
#          2) All Combinations: get all the combinations of items that fills N
#          3) Minimum Combination: get the minimum number of items that fills N 

def fitElements(capacity,itemWeights): #Existence Check
	if capacity==0:
		return True
	for pos,itemWeight in enumerate(itemWeights):
		if itemWeight <= capacity :
			newItemWeights = itemWeights[:pos]+itemWeights[pos+1: ]
			isPossible = fitElements(capacity - itemWeight, newItemWeights)
			if isPossible:
				return True
	return False

distinctPath=list()
def fitElementsCombinations(capacity,itemWeights,path=[]): #Existence Check
	path = list(path)
	if capacity==0:
		sortedPath = sorted(path)
		if( sortedPath not in distinctPath):
			distinctPath.append(sortedPath)
			print path,
			print
	for pos,itemWeight in enumerate(itemWeights):
		if itemWeight <= capacity :
			newItemWeights = itemWeights[:pos]+itemWeights[pos+1: ]
			path.append(itemWeight)
			fitElementsCombinations(capacity - itemWeight, newItemWeights,path)
			path.pop()

def fitElementsMinCombinations(capacity,itemWeights):
	if capacity==0 :
		return 0
	for pos,itemWeight in enumerate(sorted(itemWeights,reverse=True)):
		if itemWeight <= capacity :
			newItemWeights = itemWeights[:pos] + itemWeights[pos+1 : ]
			minComb = fitElementsMinCombinations(capacity - itemWeight,newItemWeights)
			if minComb != None :
				return 1 + minComb
	return None 














