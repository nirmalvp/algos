myStr = raw_input("enter string :")
i=0
compStr=""
while( i+1 < len(myStr)):
	char = myStr[i]
	count =1
	while(i+1 < len(myStr) and myStr[i+1] == myStr[i]):
		count += 1
		i += 1
	compStr += char + str(count)
	i +=1

print compStr
