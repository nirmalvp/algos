#56) A round road have N station, A0..AN-1,
# given an array D contains the distance between each neighborhood station, 
#        D1 = distance(A0-A1), D2 = distance(A1, A2), D0 = distance(AN-1, A0)
#        Write code to most effective to find the shortest distance between two station Ai and Aj.Space O(N) most

def shortestDistance(distances,stationOne,stationTwo):
	for index,distance in enumerate(distances):
		if stationOne < index <=stationTwo :
			forwardDistance += distance
		totalCircularDistance +=distance
	backwardDistance = totalCircularDistance - forwardDistance
	return min(forwardDistance,backwardDistance)


