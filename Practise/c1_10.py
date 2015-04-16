#Given a set of ranges, find the two ranges with the greatest overlap.
tuples = raw_input().split()
tempRanges=map(lambda x : ( int(x.split(",")[0]), int(x.split(",")[1] )), tuples)
ranges=list()
START = 0
END =1
for listRange in tempRanges:
	start =  listRange[0]
	end = listRange[1]
	if start > end :
		start,end = end, start
	ranges.append( (start,end) )
ranges = sorted(ranges,key = lambda x : x[0])
current = ranges[0]
maxOverLapLength = 0
for nextRange in ranges[1:] :
	overlap = range ( nextRange[START] , min(current[END],nextRange[END]) + 1)
	overlapLength = len(overlap)
	if(overlapLength > maxOverLapLength):
		maxOverLapLength = overlapLength
		range1 = current
		range2 = nextRange
	if nextRange[END] > current[END]:
		current = nextRange
print range1," --> ", range2


