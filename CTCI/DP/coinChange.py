memo=dict()
def minCoin(money):
	if(money==0):
		return 0
	if (memo.get(money)):
		return memo.get(money)
	minNumOfCoins=None
	for i,change in enumerate(changeList):
		if(change<=money):
			if (minNumOfCoins==None):
				minNumOfCoins = minCoin(money-change)
			else:
				minNumOfCoins = min(minNumOfCoins,minCoin(money-change))
		else:
			break
	memo[money]=1+minNumOfCoins
	return 1+minNumOfCoins

changeList=sorted(map(int,raw_input("List of change : ").split()))
money=input("Enter money :")
print minCoin(money)



