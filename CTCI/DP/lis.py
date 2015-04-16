def lis(myArr):
	maxLength=0
	for pos,element in enumerate(myArr):
		dp[pos] = 1
		prev=None
		for j in range(pos):
			if(myArr[j]<myArr[pos] and dp[j]+1>dp[pos]):
				dp[pos] = dp[j]+1
				prev=myArr[j]
		if (dp[pos] > maxLength):
			endElement  = element
			maxLength = dp[pos]
			print prev or "",
	print endElement
	return maxLength
myArr=map(int,raw_input("Enter List:").split())
dp=myArr[:]
print lis(myArr)