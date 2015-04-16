myStr="( ((X)) (((Y))) )"
maxSoFar = 0
currentMax = 0
balancedFlag = True
for x in myStr:
	if x == '(':
		currentMax += 1
		maxSoFar = max(maxSoFar,currentMax)
	if(x == ')'):
		if(currentMax <= 0): #Unbalamced
			balancedFlag = False
			break
		currentMax -= 1

if(balancedFlag):
	print "Max Depth parenthesis = ", maxSoFar
else:
	print "Unbalacced"



