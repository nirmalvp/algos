def findPermutation(permString):
	if(len(permString) == 1):
		return permString
	letterToInsert = permString[0]
	perms = findPermutation(permString[1:])
	listOfPerms=[]
	for perm in perms:
		for i in range(len(perm)+1):
			listOfPerms.append(perm[:i]+letterToInsert+perm[i:])
	return listOfPerms

permString = raw_input("Enter the string :")
print findPermutation(permString)
	

