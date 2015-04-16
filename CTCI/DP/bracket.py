memo={}
def printBrackets(num):
	if(num==1):
		return ["()"]
	if(memo.get(num)!=None):
		return memo.get(num)
	prevSets = printBrackets(num-1)
	allCombs = []
	for element in prevSets:
		allCombs+=["()"+element,element+"()","("+element+")"]
	allCombs=list(set(allCombs))
	memo[num]=allCombs
	return allCombs

for comb in printBrackets(int(raw_input("enter no of brackets : "))):
	print "%s \t"%comb
