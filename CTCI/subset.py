def findSubsets(mySet):
	if len(mySet) == 1 :
		yield mySet
	else :
		currentList = [ mySet[0] ]
		yield currentList
		for previousSubset in findSubsets( mySet[1:] ) :
			yield previousSubset
			yield currentList+previousSubset