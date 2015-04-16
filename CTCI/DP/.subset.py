inputSet = map(int, raw_input("Enter Set elements :").split())
inputSet = list(set(inputSet))
def powerSet(base):
	if(base==-1):
		return list()
	prevsubsets = powerSet(base-1)
	element = { inputSet[base] } #Set
	newSubsets = map(lambda eachSet: eachSet.union(element), prevsubsets)
	newSubsets += prevsubsets
	newSubsets.append(element)
	return newSubsets

print powerSet(len(inputSet)-1)




