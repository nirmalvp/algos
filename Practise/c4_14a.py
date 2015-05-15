#14.1) Given a set S, find all possible subsets
def findAllSubsets(inputSet):
	if not inputSet:
		return
	firstElement = (inputSet[0],)
	yield firstElement
	for prevSets in findAllSubsets(inputSet[1:]):
		yield prevSets
		yield firstElement + prevSets
print list(findAllSubsets([1,2,3]))

