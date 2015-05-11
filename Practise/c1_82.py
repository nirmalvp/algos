#82) There are N gas stations along a circular route, where the amount of gas at station i is gas[i]. [LeetCode]
#        You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). 
#        You begin the journey with an empty tank at one of the gas stations.
#        Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

def findStartingPoint(gas,cost):
	numberOfStops = len(gas)
	for index,_ in enumerate(gas):
		currentStop = index
		gas = 0
		count = 0
		while gas + gas[currentStop] >= cost[currentStop]:
			count +=1
			gas += gas[currentStop] - cost[currentStop]
			currentStop = (currentStop+1) % numberOfStops
		if count == numberOfStops:
			return index
	return -1
