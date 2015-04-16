def findCoin(sum):
	if(sum == 0):
		return 0
	result=findCoin(sum-1)
	if(sum>=3):
		result=min(result,findCoin(sum-3))
	if(sum>=5):
		result=min(result,findCoin(sum-5))
	return 1+ result

print findCoin(14)
