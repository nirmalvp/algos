def findPerm(myStr):
	if(len(myStr)==1):
		return [myStr]
	currentChar = myStr[0]
	prevPerms = findPerm(myStr[1:])
	newPerms = list()
	for perm in prevPerms:
		newPerms.append(perm+currentChar)
		for pos,_ in enumerate(perm):
			newPerms.append(perm[:pos]+currentChar+perm[pos:])
	return newPerms
print findPerm(raw_input("Enter word : "))