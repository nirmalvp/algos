#Given a set of coin denominators, find the minimum number of coins to give a certain amount of change
from collections import Counter
coins = map(int,raw_input("Enter Available coins : ").split())
coinCount = Counter(coins)
def findMinCoins(sumTotal,coinCount):
	if sumTotal == 0:
		return 0
	for coin in sorted(coinCount,reverse=True):
		if coin <= sumTotal and coinCount[coin] > 0 :
			tempDict = dict(coinCount)
			tempDict[coin] -= 1
			numCoins = findMinCoins(sumTotal-coin, tempDict)
			if numCoins != None:
				return 1+numCoins
	return None
sumTotal = input("Sum Total")
print findMinCoins(sumTotal,coinCount) or "None Found"

                                    
	


