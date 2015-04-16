#Ex18.7
def canMakeWordFromMyStr(word):
	for pos,_ in enumerate(word,1):
		left = word[:pos]
		right = word[pos:]
		#print word,left,right
		if myDict.has_key(left) and myDict.has_key(right):
			return True
		if myDict.has_key(left) and canMakeWordFromMyStr(right) :
			return True
	return False

myStr = ["cat","bananaeater","dog","bana","eat","na","walk","er","dogwalker"]
myDict = {word:True for word in myStr}

def findLongest(myStr):
	for word in sorted(myStr,key=len,reverse=True):
		result = canMakeWordFromMyStr(word)
		if result==True :
			return word

print findLongest(myStr)




